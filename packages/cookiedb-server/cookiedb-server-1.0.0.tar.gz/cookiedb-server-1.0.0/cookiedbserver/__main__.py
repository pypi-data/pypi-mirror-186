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

import getpass
from time import sleep

from . import config
from . import server
from . import auth


def _run_server():
    sock = server.Server()
    sock.run()

    try:
        while True:
            sleep(10)
    except KeyboardInterrupt:
        sock.stop()


def main():
    if config.check_config():
        try:
            password = getpass.getpass('[?] Password: ')
            password = password.strip()

            while not auth.Auth._check_password(password):
                password = getpass.getpass('[?] Password (\033[31mTry Again\033[m): ')
                password = password.strip()
        except KeyboardInterrupt:
            print()
            return 0
        else:
            _run_server()
    else:
        print('\033[32mWelcome to CookieDB Server!\033[m')
        print('Set a password to access your database.')
        print('Connections will only be allowed if the password is correct.\n')
        
        try:
            password = getpass.getpass('[?] Set a password: ')
            password = password.strip()

            confirm_pw = getpass.getpass('[?] Confirm the password: ')
            confirm_pw = confirm_pw.strip()

            while password != confirm_pw:
                confirm_pw = getpass.getpass('[?] Confirm the password (\033[31mTry Again\033[m): ')
                confirm_pw = confirm_pw.strip()
        except KeyboardInterrupt:
            print()
            return 0

        config.configure(password)
        print('\n\u2705 All right! Now you can run the server smoothly.')
