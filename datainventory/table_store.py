# Copyright © 2021 by IoT Spectator. All rights reserved.

"""Store for structured data."""

import enum
import sqlalchemy
import sqlite3

import pandas as pd

from typing import Dict, Tuple

from datainventory import _internal_store
from datainventory import common


class TableStore(_internal_store.InternalStore):

    def __init__(
        self, create_key, device_id: str, connection: sqlite3.Connection
    ) -> None:
        _internal_store.InternalStore.__init__(self, create_key, device_id, connection)

    def add_table(self, table: str, columns: Dict[str, common.ColumnType]) -> None:

        column_definition = dict()
        for column, column_type in columns.items():
            column_definition[column] = column_type.value
        _internal_store.InternalStore.create_table(
            self, table=table, columns=column_definition
        )

    def insert_data(self, table: str, data: Dict) -> None:

        columns = list()
        values = list()
        for column, value in data.items():
            columns.append(column)
            values.append(value)

        try:
            _internal_store.InternalStore.insert(
                self, table=table, columns=tuple(columns), values=tuple(values)
            )
        except sqlite3.OperationalError as error:
            print(error)

    def query_data(self, table: str, range: common.Range) -> pd.DataFrame:
        pass
