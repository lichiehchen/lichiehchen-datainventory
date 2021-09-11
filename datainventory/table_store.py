# Copyright © 2021 by IoT Spectator. All rights reserved.

"""Store for structured data."""

import datetime
import sqlalchemy

import pandas as pd

from typing import Dict, List

from sqlalchemy.orm import Session

from datainventory import _internal_store
from datainventory import common


class TableStore(_internal_store.InternalStore):
    def __init__(
        self,
        create_key,
        device_id: str,
        metadata: sqlalchemy.MetaData,
        session: Session
    ) -> None:
        _internal_store.InternalStore.__init__(
            self, create_key=create_key, device_id=device_id
        )
        self._session = session
        self._metadata = metadata

    def create_table(
        self, table_name: str, columns: Dict[str, common.ColumnType]
    ) -> None:

        columns["device_id"] = common.ColumnType.String
        columns["timestamp"] = common.ColumnType.DateTime

        table = sqlalchemy.Table(
            table_name,
            self._metadata,
            *(
                sqlalchemy.Column(column_name, column_type.value)
                for column_name, column_type in columns.items()
            ),
        )
        table.create(checkfirst=True)

    def insert(self, table_name: str, values: List[Dict]) -> None:

        for item in values:
            item["device_id"] = self._device_id
            item["timestamp"] = datetime.datetime.utcnow()

        table = self._metadata.tables[table_name]
        self._session.execute(table.insert().values(values))

    def query_data(self, table: str, range: common.Range) -> pd.DataFrame:
        table_obj: sqlalchemy.Table = self._metadata.tables[table]

        if range:
            return pd.DataFrame()
        else:
            results = self._session.query(table_obj).all()
            return pd.DataFrame(results, columns=table_obj.columns.keys())
