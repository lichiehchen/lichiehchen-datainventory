# Copyright © 2021 by IoT Spectator. All rights reserved.

"""Internal module that defines common class and definitions."""

import datetime
import sqlalchemy

from typing import Dict, List

from datainventory import common

CREATE_KEY = "0x4352454154455f4b4559"  # CREATE_KEY ASCII Code


class InternalStore:
    def __init__(
        self, create_key, device_id: str, sql_engine: sqlalchemy.engine.Engine
    ) -> None:
        if create_key is not CREATE_KEY:
            raise RuntimeError("This method should not be called from outside")
        self._device_id = device_id
        self._sql_engine = sql_engine
        self._connection = self._sql_engine.connect()
        self._sql_metadata = sqlalchemy.MetaData(bind=sql_engine)

    def create_table(
        self, table_name: str, columns: Dict[str, common.ColumnType]
    ) -> None:

        columns["device_id"] = common.ColumnType.String
        columns["timestamp"] = common.ColumnType.DateTime

        table = sqlalchemy.Table(
            table_name,
            self._sql_metadata,
            *(
                sqlalchemy.Column(column_name, column_type.value)
                for column_name, column_type in columns.items()
            ),
        )
        table.create(bind=self._sql_engine, checkfirst=True)

    def insert(self, table_name: str, values: List[Dict]) -> None:

        for item in values:
            item["device_id"] = self._device_id
            item["timestamp"] = datetime.datetime.utcnow()

        table = self._sql_metadata.tables[table_name]
        self._connection.execute(table.insert().values(values))
