import sqlite3

from typing import Dict, Tuple


CREATE_KEY = "0x4352454154455f4b4559"  # CREATE_KEY ASCII Code


class InternalStore:
    def __init__(
        self, create_key, device_id: str, connection: sqlite3.Connection
    ) -> None:
        if create_key is not CREATE_KEY:
            raise RuntimeError("This method should not be called from outside")
        self._device_id = device_id
        self._connection = connection
        self._cursor = self._connection.cursor()

    def create_table(self, table: str, columns: Dict) -> None:

        columns_string = "device_id TEXT, "
        for column_name, column_type in columns.items():
            columns_string += f"{column_name} {column_type}, "
        columns_string += "timestamp TEXT"

        sql_creates_table = f"CREATE TABLE IF NOT EXISTS {table} ({columns_string});"
        self._cursor.execute(sql_creates_table)

    def insert(self, table: str, columns: Tuple, values: Tuple) -> None:
        # Generic insert method
        # add device_id and timestamp
        columns_string = "device_id, "
        column_counter = 1
        for column in columns:
            columns_string += f"{column}, "
            column_counter += 1
        columns_string += "timestamp"

        value_string = "("
        for _ in range(column_counter):
            value_string += "?,"
        value_string += "?)"

        sql_insert = f"INSERT INTO {table}{columns_string} VALUES{value_string}"
        self._cursor.execute(sql_insert, values)
        self._connection.commit()
