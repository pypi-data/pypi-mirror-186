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

from typing import TYPE_CHECKING

from requests import Response

from gitlabracadabra.auth_info import AuthInfo
from gitlabracadabra.containers.authenticated_session import AuthenticatedSession
from gitlabracadabra.containers.const import DOCKER_HOSTNAME, DOCKER_REGISTRY
from gitlabracadabra.containers.scope import Scope


if TYPE_CHECKING:
    from typing import Optional

    from requests.auth import AuthBase

    from gitlabracadabra.containers.authenticated_session import Data, Params


class RegistrySession(object):
    """Container registry HTTP methods."""

    def __init__(self, hostname: str, auth_info: Optional[AuthInfo] = None) -> None:
        """Instantiate a registry connection.

        Args:
            hostname: fqdn of a registry.
            auth_info: Authentication information.
        """
        self._session = AuthenticatedSession()
        self._hostname = hostname
        if hostname == DOCKER_HOSTNAME:
            self._session.connection_hostname = DOCKER_REGISTRY
        else:
            self._session.connection_hostname = hostname
        self._session.auth_info = auth_info or AuthInfo()
        # Cache where blobs are present
        # dict key is digest, value is a list of manifest names
        # Used in WithBlobs
        self._blobs: dict[str, list[str]] = {}
        self._sizes: dict[str, int] = {}

    def __del__(self) -> None:  # noqa:WPS603
        """Destroy a registry connection."""
        self._session.close()

    @property
    def hostname(self) -> str:
        """Get hostname.

        Returns:
            The registry hostname.
        """
        return self._hostname

    def request(
        self,
        method: str,
        url: str,
        *,
        scopes: Optional[set[Scope]] = None,
        params: Params = None,  # noqa: WPS110
        data: Optional[Data] = None,  # noqa: WPS110
        headers: Optional[dict[str, str]] = None,
        content_type: Optional[str] = None,
        accept: Optional[tuple[str, ...]] = None,
        auth: Optional[AuthBase] = None,
        stream: Optional[bool] = None,
        raise_for_status: bool = True,
    ) -> Response:
        """Send an HTTP request.

        Args:
            method: HTTP method.
            url: Either a path or a full url.
            scopes: An optional set of scopes.
            params: query string params.
            data: Request body stream.
            headers: Request headers.
            content_type: Uploaded MIME type.
            accept: An optional list of accepted mime-types.
            auth: HTTPBasicAuth.
            stream: Stream the response.
            raise_for_status: Raises `requests.HTTPError`, if one occurred.

        Returns:
            A Response.
        """
        if headers:
            headers = headers.copy()
        else:
            headers = {}
        if accept:
            headers['Accept'] = ', '.join(accept)
        if content_type:
            headers['Content-Type'] = content_type

        self._session.connect(scopes)
        response = self._session.authenticated_request(
            method,
            url,
            params=params,
            data=data,
            headers=headers,
            auth=auth,
            stream=stream,
        )
        if raise_for_status:
            response.raise_for_status()
        return response
