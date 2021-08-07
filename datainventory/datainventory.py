import pathlib
import shutil
import sqlite3

from typing import Optional

from datainventory import _internal_store
from datainventory import model_store
from datainventory import media_store
from datainventory import simple_store


class DataInventory:
    def __init__(
        self, device_id: str, inventory: Optional[pathlib.Path] = None
    ) -> None:
        self._device_id = device_id

        self._inventory: Optional[pathlib.Path] = None
        if inventory:
            self._inventory = inventory
            self._database_name = self._inventory.name + ".db"
            self._database = self._inventory / self._database_name

            if not self._inventory.exists():
                self._inventory.mkdir()
            self._connection = sqlite3.connect(str(self._database))
        else:
            self._connection = sqlite3.connect(":memory:")

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
        raise NotImplementedError("Export is not implemented")

    def destroy(self) -> None:
        if self._inventory:
            shutil.rmtree(self._inventory)
