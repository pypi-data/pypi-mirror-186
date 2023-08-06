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
from typing import Any

import cookiedb
from .config import DATABASES_PATH
from .config import PASSWORD_PATH


class DBHandle:
    def __init__(self) -> None:
        with open(PASSWORD_PATH, 'r') as file:
            key = file.read()

        self._db = cookiedb.CookieDB(key, DATABASES_PATH)

    @staticmethod
    def _list_databases() -> list:
        db_files = os.listdir(DATABASES_PATH)
        db_files = [f.replace('.cookiedb', '') for f in db_files]
        return dict(status='okay', message='database_listed', data=db_files)

    @staticmethod
    def _delete_database(name: str) -> dict:
        db_file = os.path.join(DATABASES_PATH, f'{name}.cookiedb')

        if os.path.isfile(db_file):
            os.remove(db_file)

        return dict(status='okay', message='database_deleted')

    def _create_database(self, name: str) -> dict:
        try:
            self._db.create_database(name)
        except cookiedb.exceptions.DatabaseExistsError:
            response = dict(status='fail', message='database_exists')
        else:
            response = dict(status='okay', message='database_created')

        return response

    def _add_item(self, database: str, path: str, item: Any) -> dict:
        self._db.open(database)
        self._db.add(path, item)
        return dict(status='okay', message='item_added')

    def _update_item(self, database: str, path: str, item: Any) -> dict:
        self._db.open(database)
        try:
            self._db.update(path, item)
        except cookiedb.exceptions.ItemNotExistsError:
            response = dict(status='fail', message='item_not_exists_error')
        else:
            response = dict(status='okay', message='item_updated')

        return response

    def _get_item(self, database: str, path: str) -> dict:
        self._db.open(database)
        result = self._db.get(path)
        return dict(status='okay', message='item_obtained', data=result)

    def _delete_item(self, database: str, path: str) -> dict:
        self._db.open(database)
        self._db.delete(path)
        return dict(status='okay', message='item_deleted')

    def analyze_request(self, request: dict) -> dict:
        action = request['action']
        path = request['path']

        # Server Operations: Create database (CDB),
        # delete database (DDB), open database (ODB)
        # and list database (LDB).
        # 
        # Database Operations: Add item (ADD), get item (GET),
        # delete item (DEL), update (UPD). 
        # 
        # Database operations must follow the database name
        # in the "action" field. Example: MyDatabase:GET

        if action == 'CDB':
            response = self._create_database(path)
        elif action == 'DDB':
            response = self._delete_database(path)
        elif action == 'LDB':
            response = self._list_databases()
        else:
            try:
                database = request['database']
            except ValueError:
                response = dict(status='fail', message='invalid_action')
            else:
                if action == 'GET':
                    response = self._get_item(database, path)
                elif action == 'ADD':
                    item = request['data']
                    response = self._add_item(database, path, item)
                elif action == 'DEL':
                    response = self._delete_item(database, path)
                elif action == 'UPD':
                    item = request['data']
                    response = self._update_item(database, path, item)

        return response
