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

import os
import hashlib
import random
from pathlib import Path

HOME_USER = Path.home()
COOKIEDB_PATH = os.path.join(HOME_USER, '.cookiedbserver')
PASSWORD_PATH = os.path.join(COOKIEDB_PATH, 'password')
DATABASES_PATH = os.path.join(COOKIEDB_PATH, 'databases')


def check_config() -> None:
    return all([
        os.path.isdir(COOKIEDB_PATH),
        os.path.isfile(PASSWORD_PATH),
        os.path.isdir(DATABASES_PATH)
    ])


def configure(password: str) -> None:
    os.mkdir(COOKIEDB_PATH)
    os.mkdir(DATABASES_PATH)

    salt = random.randint(0, 10)
    pw_with_salt = (password + str(salt)).encode()
    hashed_pw = hashlib.sha256(pw_with_salt).hexdigest()

    with open(PASSWORD_PATH, 'w') as file:
        file.write(hashed_pw)
