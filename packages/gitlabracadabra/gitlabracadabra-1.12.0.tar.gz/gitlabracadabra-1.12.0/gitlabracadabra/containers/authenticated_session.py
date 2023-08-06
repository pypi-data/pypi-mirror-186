# -*- coding: utf-8 -*-
#
# Copyright (C) 2019-2022 Mathieu Parent <math.parent@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from __future__ import annotations

from time import time
from typing import TYPE_CHECKING
from urllib.parse import urlparse
from urllib.request import parse_http_list, parse_keqv_list

from requests import PreparedRequest, Response, codes
from requests.structures import CaseInsensitiveDict

from gitlabracadabra import __version__ as gitlabracadabra_version
from gitlabracadabra.auth_info import AuthInfo
from gitlabracadabra.containers.scope import Scope
from gitlabracadabra.session import Session


if TYPE_CHECKING:
    from typing import Any, Iterable, MutableMapping, Optional, Union

    from requests.auth import AuthBase

    Params = Optional[  # noqa: WPS110
        MutableMapping[
            str,
            Union[str, list[str]],
        ]
    ]
    Data = Iterable[bytes]  # noqa: WPS110
    _SimpleParams = dict[str, Union[str, list[str]]]
    _TokenKey = tuple[str, str, Optional[int], Optional[str]]


class Token(object):
    """JWT Token."""

    def __init__(
        self,
        token: str,
        expires_in: int,
    ) -> None:
        """Instantiate a token.

        Args:
            token: Token.
            expires_in: Expires in x seconds.
        """
        minimum_token_lifetime_seconds = 60

        self._token = token
        self._expires_in = expires_in
        if self._expires_in < minimum_token_lifetime_seconds:
            self._expires_in = minimum_token_lifetime_seconds

        # We ignore issued_at property, and use local time instead
        self._issued_at = time()

    @property
    def token(self) -> str:
        """Get token.

        Returns:
            The token.
        """
        return self._token

    @property
    def expiration_time(self) -> float:
        """Get expiration time.

        Returns:
            Expiration time.
        """
        return self._issued_at + self._expires_in

    def is_expired(self) -> bool:
        """Check if token is expired.

        Returns:
            True if token is expired.
        """
        return time() >= self.expiration_time


class AuthenticatedSession(Session):
    """Session with auth per-host."""

    def __init__(self, *args: list[Any], **kwargs: dict[str, Any]) -> None:
        """Instantiate a session.

        Args:
            args: Positional arguments.
            kwargs: Named arguments.
        """
        super().__init__(*args, **kwargs)
        self.headers = CaseInsensitiveDict({
            'User-Agent': 'gitlabracadabra/{0}'.format(gitlabracadabra_version),
            'Docker-Distribution-Api-Version': 'registry/2.0',
        })

        # Added attributes
        self.scheme = 'https'
        self.connection_hostname = ''
        self.auth_info = AuthInfo()
        # Tokens, by set of scheme, host, port and scopes (as query string or None for all scope)
        self._tokens: dict[_TokenKey, Token] = {}
        self._current_scopes: Optional[set[Scope]] = None

    def authenticated_request(
        self,
        method: str,
        url: str,
        params: Optional[Params] = None,  # noqa: WPS110
        data: Optional[Data] = None,  # noqa: WPS110
        headers: Optional[dict[str, str]] = None,
        auth: Optional[AuthBase] = None,
        stream: Optional[bool] = None,
    ) -> Response:
        """Send an HTTP request.

        Args:
            method: HTTP method.
            url: Either a path or a full url.
            params: query string params.
            data: Request body stream.
            headers: Request headers.
            auth: HTTPBasicAuth.
            stream: Stream the response.

        Returns:
            A Response.
        """
        if url.startswith('/'):
            url = '{0}://{1}{2}'.format(self.scheme, self.connection_hostname, url)
        token = self._get_token(url, self._current_scopes)
        if token:
            if headers is None:
                headers = {}
            headers['Authorization'] = 'Bearer {0}'.format(token.token)
        return self.request(
            method,
            url,
            params=params,
            data=data,
            headers=headers,
            auth=auth,
            stream=stream,
        )

    def rebuild_auth(self, prepared_request: PreparedRequest, response: Response) -> None:
        """Override Session method to inject bearer tokens.

        Args:
            prepared_request: Prepared request.
            response: Response.
        """
        super().rebuild_auth(prepared_request, response)  # type: ignore
        token = self._get_token(prepared_request.url or '', self._current_scopes)
        if token:
            prepared_request.headers['Authorization'] = 'Bearer {0}'.format(token.token)

    def connect(self, scopes: Optional[set[Scope]]) -> None:
        """Connect.

        Args:
            scopes: An optional set of scopes.
        """
        self._current_scopes = scopes
        url = '{0}://{1}/v2/'.format(self.scheme, self.connection_hostname)
        token = self._get_token(url, scopes)
        if token:
            return
        token = self._get_token(url, None)
        if token:
            return
        response = self.authenticated_request('get', url)
        if response.history:
            self.connection_hostname = urlparse(response.url).hostname or self.connection_hostname
        if response.status_code == codes['ok']:
            one_hour = 3600
            self._set_token(response, None, Token('no_auth', one_hour))
            return
        if response.status_code == codes['unauthorized']:
            if response.headers['Www-Authenticate'].startswith('Bearer '):
                self._get_bearer_token(response)
                return
        response.raise_for_status()

    def _get_bearer_token(self, response: Response) -> None:
        if self._current_scopes is None:
            raise ValueError
        challenge_parameters = self._get_challenge_parameters(response)
        get_params: _SimpleParams = {}
        if 'service' in challenge_parameters:
            get_params['service'] = challenge_parameters.get('service', 'unknown')
        get_params['scope'] = []
        for scope in sorted(self._current_scopes):
            get_params['scope'].append(  # type: ignore
                'repository:{0}:{1}'.format(scope.remote_name, scope.actions),
            )
        challenge_response = self.authenticated_request(
            'get',
            challenge_parameters['realm'],
            params=get_params,
            headers=self.auth_info.headers,
            auth=self.auth_info.auth,
        )
        challenge_response.raise_for_status()
        json = challenge_response.json()
        self._set_token(
            response,
            self._current_scopes,
            Token(
                str(json.get('token', json.get('access_token', ''))),
                int(json.get('expires_in', 0)),
            ),
        )

    def _get_challenge_parameters(self, response: Response) -> dict[str, str]:
        _, _, challenge = response.headers['Www-Authenticate'].partition('Bearer ')
        return parse_keqv_list(parse_http_list(challenge))

    def _get_token(self, url: str, scopes: Optional[set[Scope]]) -> Optional[Token]:
        parsed = urlparse(url)
        key = (
            parsed.scheme,
            parsed.hostname or '',
            parsed.port,
            self._scopes_hash(scopes),
        )
        token = self._tokens.get(key)
        if token and token.is_expired():
            self._tokens.pop(key)
            return None
        return token

    def _set_token(self, response: Response, scopes: Optional[set[Scope]], token: Token) -> None:
        parsed = urlparse(response.url)
        key = (
            parsed.scheme,
            parsed.hostname or '',
            parsed.port,
            self._scopes_hash(scopes),
        )
        self._tokens[key] = token

    def _scopes_hash(self, scopes: Optional[set[Scope]]) -> Optional[str]:
        if scopes is None:
            return None
        return ','.join(map(str, sorted(scopes)))
