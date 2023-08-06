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

from requests import Session as RequestSession
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


class Session(RequestSession):
    """Session with retry backoff."""

    def __init__(self) -> None:
        """Instantiate a session."""
        super().__init__()
        # retry after 0.0s, 0.2s, 0.4s, 0.8s, 1.6s
        # retry at    0.0s, 0.2s, 0.6s, 1.4s, 3.0s
        self.mount('http://', HTTPAdapter(max_retries=Retry(total=5, backoff_factor=0.1)))
        self.mount('https://', HTTPAdapter(max_retries=Retry(total=5, backoff_factor=0.1)))
