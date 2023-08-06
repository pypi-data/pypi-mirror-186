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

import socket
import threading

from .dmp import DMP
from .auth import Auth
from .database import DBHandle


def log(log_type: str, message: str) -> None:
    if log_type == 'error':
        print(f'[\033[1;31m{log_type.upper()}\033[m] {message}')
    else:
        print(f'[\033[1m{log_type.upper()}\033[m] {message}')


class Server:
    def __init__(self, host: str = '127.0.0.1') -> None:
        self._auth = Auth()
        self._address = (host, 2808)

        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self._socket.bind(self._address)
        self._socket.listen(5)

    def _handle_database(self, client: socket.socket, conn_id: str) -> None:
        client_db = DBHandle()

        while True:
            message = client.recv(5024)

            if not message:
                self._auth.logout(conn_id)
                break

            request = DMP.parse_request(message)
            response = client_db.analyze_request(request)

            client_response = DMP.parse_response(
                status=response['status'],
                message=response['message'],
                data=response.get('data')
            )

            client.send(client_response)

    def _run(self) -> None:
        while True:
            client, addr = self._socket.accept()
            password = client.recv(1024).decode()
            conn_id = self._auth.login(addr, password)

            if conn_id:
                log('info', f'Client {addr[0]}:{addr[1]} logged')
                response = DMP.parse_response('OKAY', 'login_successfully')
                client.send(response)
                self._handle_database(client, conn_id)
            else:
                log('error', f'Incorrect password to {addr[0]}:{addr[1]} login')
                response = DMP.parse_response('FAIL', 'invalid_password')
                client.send(response)
                client.close()

    def run(self) -> None:
        server_th = threading.Thread(target=self._run)
        server_th.setDaemon(True)
        server_th.start()

        log('info', f'Server started in {self._address[0]}:{self._address[1]}')

    def stop(self) -> None:
        self._socket.close()
        log('info', 'Server closed')
