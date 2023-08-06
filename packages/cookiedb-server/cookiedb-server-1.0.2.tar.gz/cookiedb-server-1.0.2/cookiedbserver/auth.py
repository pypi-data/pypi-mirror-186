# Copyright 2023 Jaedson Silva
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#   http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import hashlib
from typing import Union

from .config import PASSWORD_PATH


class Auth:
    def __init__(self) -> None:
        self._logged_users = []

    @staticmethod
    def _check_password(password: str) -> bool:
        with open(PASSWORD_PATH, 'r') as file:
            hashed_pw = file.read()

        for salt in range(0, 11):
            pw_and_salt = (password + str(salt)).encode()
            try_pw_hash = hashlib.sha256(pw_and_salt).hexdigest()

            if hashed_pw == try_pw_hash:
                # password match
                return True

        return False

    @staticmethod
    def _get_connection_id(address: tuple) -> str:
        address_str = f'{address[0]}:{address[1]}'.encode()
        connection_id = hashlib.md5(address_str).hexdigest()
        return connection_id

    def login(self, address: tuple, password: str) -> Union[bool, str]:
        if self._check_password(password):
            connection_id = self._get_connection_id(address)
            self._logged_users.append(connection_id)
            return connection_id
        else:
            return False

    def logout(self, connection_id: str) -> bool:
        try:
            self._logged_users.remove(connection_id)
        except ValueError:
            return False
        else:
            return True
