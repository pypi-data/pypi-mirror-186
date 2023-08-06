import os
import shutil
import sys
from pathlib import Path

import bupytest
import cookiedb
from _client import Client

sys.path.insert(0, './')

from cookiedbserver.config import configure
from cookiedbserver.server import Server

HOST = '127.0.0.1'
USER_PW = '12345678'


class TestServer(bupytest.UnitTest):
    def __init__(self):
        super().__init__()

        self._database = 'Market'
        self._temp_database = 'TempDatabase'

        self._database_data = {
            'banana': {
                'id': 1,
                'name': 'banana',
                'price': 1.50,
                'inStock': True
            },
            'cookie': {
                'id': 2,
                'name': 'cookie',
                'price': 2.75,
                'inStock': False
            }
        }

        home_dir = Path.home()
        server_dir = os.path.join(home_dir, '.cookiedbserver')

        if os.path.isdir(server_dir):
            shutil.rmtree(server_dir)

        # configure server
        configure(USER_PW)

        # run server
        server = Server()
        server.run()

        self.db = Client()
        self.db.connect('127.0.0.1', USER_PW)

    def test_create_database(self):
        self.db.create_database(self._database)
    
    def test_create_temp_database(self):
        self.db.create_database(self._temp_database)
    
    def test_list_databases(self):
        databases = self.db.list_databases()
        self.assert_expected(databases, [self._database, self._temp_database])

    def test_delete_database(self):
        self.db.delete_database(self._temp_database)

    def test_create_same_database(self):
        try:
            self.db.create_database(self._database)
        except cookiedb.exceptions.DatabaseExistsError:
            self.assert_true(True)
        else:
            self.assert_true(False, message='Expected a DatabaseExistsError exception')

    def test_list_databases_2(self):
        databases = self.db.list_databases()
        self.assert_expected(databases, [self._database])

    def test_open_database(self):
        try:
            self.db.open(self._database)
        except cookiedb.exceptions.DatabaseNotFoundError:
            self.assert_true(False, message='Unexpected DatabaseNotFoundError exception')
        else:
            self.assert_true(True)

    def test_add_item(self):
        self.db.add('products', self._database_data)

    def test_get_item(self):
        items = self.db.get('products')
        self.assert_expected(items, self._database_data)

    def test_delete_item(self):
        self.db.delete('products/banana')
        self._database_data.pop('banana')

    def test_get_item_2(self):
        items = self.db.get('products')
        self.assert_expected(items, self._database_data)

    def test_update_item(self):
        self.db.update('products/cookie/price', 3.50)
        self._database_data['cookie']['price'] = 3.50

    def test_get_item_3(self):
        items = self.db.get('products')
        self.assert_expected(items, self._database_data)

    def test_update_each_data(self):
        # bool
        self.db.update('products/cookie/inStock', True)
        self._database_data['cookie']['inStock'] = True

        # int
        self.db.update('products/cookie/id', 3)
        self._database_data['cookie']['id'] = 3

        # float
        self.db.update('products/cookie/price', 3.75)
        self._database_data['cookie']['price'] = 3.75

        # string
        self.db.update('products/cookie/name', 'Cookie')
        self._database_data['cookie']['name'] = 'Cookie'

    def test_check_datatype_get(self):
        # bool type
        in_stock = self.db.get('products/cookie/inStock')
        self.assert_expected(in_stock, self._database_data['cookie']['inStock'])

        # float
        price = self.db.get('products/cookie/price')
        self.assert_expected(price, self._database_data['cookie']['price'])

        # int
        p_id = self.db.get('products/cookie/id')
        self.assert_expected(p_id, self._database_data['cookie']['id'])

        # string
        name = self.db.get('products/cookie/name')
        self.assert_expected(name, self._database_data['cookie']['name'])


if __name__ == '__main__':
    bupytest.this()
