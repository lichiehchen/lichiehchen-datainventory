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

        # Check table, create if does not exist

    def insert_temperature(self, scale: Scale, value: float) -> None:
        _internal_store.InternalStore.insert(
            self,
            table=SimpleStore._TEMPERATURE_TABLE,
            columns=("scale", "value"),
            values=(str(scale), value),
        )

    def insert_generic(self, name: str, data: Dict) -> None:
        pass
