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

# DMP - Database Manipulation Protocol
# 
# Protocol Request Structure:
# ACTION PATH:<DATABASE NAME> (required if requested "action" is GET, ADD, DEL, or UPD)
# <datatype> <data (required if requested "action" is GET, ADD, DEL, or UPD)>
# 
# Protocol Response Structure:
# STATUS MESSAGE
# <datatype> <data (required if requested "action" is GET, ADD, DEL, or UPD)>

import json
import struct

from typing import Any


class DMP:
    @staticmethod
    def parse_request(message: bytes) -> dict:
        request = {}

        action_field = message[:3]
        action = struct.unpack(f'3s', action_field)
        action = action[0].decode()

        splited_msg = message.split(b'\n')
        remaining_fields = splited_msg[0][3:]
        fields = struct.unpack(f'{len(remaining_fields)}s', remaining_fields)

        if action in ('GET', 'ADD', 'UPD', 'DEL'):
            path, database = fields[0].split(b':')
            request['database'] = database.decode()

            if action in ('ADD', 'UPD'):
                data = splited_msg[1]
                rdata = data[4:]
                datatype, = struct.unpack('4s', data[:4])

                if datatype == b'json':
                    _data = json.loads(rdata)
                elif datatype == b'stri':
                    _data = rdata.decode()
                elif datatype == b'intg':
                    _data = int.from_bytes(rdata, byteorder='big')
                elif datatype == b'flot':
                    _data, = struct.unpack('f', rdata)
                elif datatype == b'bool':
                    _data, = struct.unpack('?', rdata)

                request['data'] = _data
        elif action in ('CDB', 'LDB', 'DDB', 'ODB'):
            path = fields[0]

        request['path'] = path.decode()
        request['action'] = action

        return request

    @staticmethod
    def parse_response(status: str, message: str, data: Any = None) -> bytes:
        status = status.upper().encode()
        message = message.upper().encode()
        packed = struct.pack(f'4s {len(message)}s', status, message)

        if data is not None:
            if isinstance(data, (list, dict, tuple)):
                json_data = json.dumps(data, separators=(',', ':'))
                datatype = struct.pack('4s', b'json')
                _encoded_data = json_data.encode()
            elif isinstance(data, str):
                datatype = struct.pack('4s', b'stri')
                _encoded_data = data.encode()
            elif isinstance(data, bool):
                datatype = struct.pack('4s', b'bool')
                _encoded_data = struct.pack('?', data)
            elif isinstance(data, int):
                datatype = struct.pack('4s', b'intg')
                _encoded_data = data.to_bytes(2, byteorder='big')
            elif isinstance(data, float):
                datatype = struct.pack('4s', b'flot')
                _encoded_data = struct.pack('f', data)

            packed += b'\n'
            packed += datatype + _encoded_data

        return packed


if __name__ == '__main__':
    request_data = struct.pack('3s 14s', b'CDB', b'MyDatabaseName')
    print(DMP.parse_request(request_data))

    request_data = struct.pack('3s 11s', b'ADD', b'users/:mydb')
    request_data += b'\n' + (json.dumps({'name': 'Jaedson'})).encode()
    print(DMP.parse_request(request_data))

    response = DMP.parse_response('OKAY', 'this_ok', data=14)
    print(response)
