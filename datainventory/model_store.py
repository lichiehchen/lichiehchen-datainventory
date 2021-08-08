# Copyright © 2021 by IoT Spectator. All rights reserved.

"""Store for machine learning models."""

import sqlite3

from typing import Tuple

from datainventory import _internal_store


class ModelStore(_internal_store.InternalStore):

    def __init__(
        self, create_key, device_id: str, connection: sqlite3.Connection
    ) -> None:
        _internal_store.InternalStore.__init__(self, create_key, device_id, connection)

    def get_model(self, name: str, version: str) -> Tuple:
        """Retrieve the model according to the name and version from database."""
        raise NotImplementedError("The function is not implemented.")
