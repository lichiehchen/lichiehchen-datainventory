import enum
import sqlite3

from typing import Dict

from datainventory import _internal_store


class Scale(enum.Enum):
    Celsius = enum.auto()
    Fahrenheit = enum.auto()


class SimpleStore(_internal_store.InternalStore):

    _TEMPERATURE_TABLE = "temperature"

    def __init__(
        self, create_key, device_id: str, connection: sqlite3.Connection
    ) -> None:
        _internal_store.InternalStore.__init__(self, create_key, device_id, connection)
        _internal_store.InternalStore.create_table(
            self,
            table=SimpleStore._TEMPERATURE_TABLE,
            columns={"scale": "TEXT", "value": "REAL"},
        )

    def insert_temperature(self, scale: Scale, value: float) -> None:

        _internal_store.InternalStore.insert(
            self,
            table=SimpleStore._TEMPERATURE_TABLE,
            columns=("scale", "value"),
            values=(scale.name, value),
        )

    def create_custom_table(self, table: str, columns: Dict) -> None:
        _internal_store.InternalStore.create_table(self, table=table, columns=columns)

    def insert_custom_data(self, table: str, data: Dict) -> None:

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
