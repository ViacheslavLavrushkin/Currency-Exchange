import csv
import json
import sqlite3

import os


class TXTWriter:

    def __init__(self):
        self.file = open('./results.txt', 'w')

    def write(self, item: dict):
        self.file.write(f"{item}\n")


class CSVWriter:
    def __init__(self):
        self._file = open('results.csv', 'w')
        self.writer = csv.writer(self._file)
        self._headers = None

    def write(self, item: dict):

        if self._headers is None:
            # write the header
            self.writer.writerow(list(item.keys()))

        # write the data
        self.writer.writerow(list(item.values()))


class DBWriter:
    def __init__(self, db_name=None, table_name=None):
        if not db_name:
            db_name = 'results.sqlite3'

        if not table_name:
            table_name = 'jobs'

        if os.path.exists(db_name):
            os.remove(db_name)

        self._connection = sqlite3.connect(db_name)
        self._cursor = self._connection.cursor()
        self._headers = None
        self._table_name = table_name

    def _create_table(self, headers):
        if self._headers is None:
            self._headers = headers
            columns = ',\n'.join(f'{column_name} text' for column_name in headers)

            sql = f'''
            CREATE TABLE IF NOT EXISTS {self._table_name} (
                {columns}
            );
            '''
            self._cursor.execute(sql)
            self._connection.commit()

    def write(self, item):
        if self._headers is None:
            self._create_table(item.keys())

        keys = ', '.join(f':{column_name}' for column_name in item)

        sql = f"INSERT INTO {self._table_name} VALUES ({keys})"
        self._cursor.execute(sql, item)
        self._connection.commit()

    def destruct(self):
        self._connection.commit()
        self._connection.close()


class JSONWriter:
    def __init__(self, filename=None):
        if not filename:
            filename = 'results.json'

        self._file = open(filename, 'w', encoding='utf-8')
        self._file.write('[\n]\n')
        self._first_write = True

    def write(self, item: dict):
        self._file.seek(self._file.tell() - 2, os.SEEK_SET)

        if self._first_write:
            self._first_write = False
        else:
            self._file.write(',\n')

        json.dump(item, self._file, sort_keys=True, indent=4)
        self._file.write('\n]')

    def destruct(self):
        self._file.close()