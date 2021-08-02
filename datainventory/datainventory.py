import pathlib
import sqlite3

from datainventory import _internal_store
from datainventory import model_store
from datainventory import media_store
from datainventory import simple_store


class DataInventory:
    def __init__(self, device_id: str, database: pathlib.Path) -> None:
        self._device_id = device_id
        self._connection = sqlite3.connect(str(database))

    def get_media_store(self) -> media_store.MediaStore:
        return media_store.MediaStore(
            create_key=_internal_store.CREATE_KEY,
            device_id=self._device_id,
            connection=self._connection,
        )

    def get_model_store(self) -> model_store.ModelStore:
        return model_store.ModelStore(
            create_key=_internal_store.CREATE_KEY,
            device_id=self._device_id,
            connection=self._connection,
        )

    def get_simple_store(self) -> simple_store.SimpleStore:
        return simple_store.SimpleStore(
            create_key=_internal_store.CREATE_KEY,
            device_id=self._device_id,
            connection=self._connection,
        )

    def export(self, dest: pathlib.Path) -> None:
        pass

    def destroy(self) -> None:
        pass
