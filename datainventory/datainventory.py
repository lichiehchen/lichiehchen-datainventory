# Copyright © 2021 by IoT Spectator. All rights reserved.

"""The main module of Data Inventory."""

import pathlib
import shutil
import sqlalchemy

from sqlalchemy.orm import sessionmaker

from datainventory import _internal_store
from datainventory import model_store
from datainventory import media_store
from datainventory import table_store


class DataInventory:
    """Data Inventory."""

    def __init__(self, device_id: str, inventory: pathlib.Path) -> None:
        self._device_id = device_id
        self._inventory = inventory
        self._database_name = self._inventory.name + ".db"
        self._database = self._inventory / self._database_name

        if not self._inventory.exists():
            self._inventory.mkdir()
        self._engine = sqlalchemy.create_engine(f"sqlite:///{self._inventory}")
        self._metadata = sqlalchemy.MetaData(bind=self._engine)

    def get_media_store(self) -> media_store.MediaStore:
        """Return an instance of the media store."""
        Session = sessionmaker(bind=self._engine)
        return media_store.MediaStore(
            create_key=_internal_store.CREATE_KEY,
            device_id=self._device_id,
            metadata=self._metadata,
            session=Session(),
            connection=self._engine.connect()
        )

    def get_model_store(self) -> model_store.ModelStore:
        """Return an instance of the model store."""
        Session = sessionmaker(bind=self._engine)
        return model_store.ModelStore(
            create_key=_internal_store.CREATE_KEY,
            device_id=self._device_id,
            session=Session(),
        )

    def get_table_store(self) -> table_store.TableStore:
        """Return an instance of the table store."""
        Session = sessionmaker(bind=self._engine)
        return table_store.TableStore(
            create_key=_internal_store.CREATE_KEY,
            device_id=self._device_id,
            metadata=self._metadata,
            session=Session(),
        )

    def export(self, dest: pathlib.Path) -> None:
        """Export the entire data inventory."""
        raise NotImplementedError("Export is not implemented")

    def destroy(self) -> None:
        """Destory the entire data inventory."""
        if self._inventory:
            shutil.rmtree(self._inventory)
