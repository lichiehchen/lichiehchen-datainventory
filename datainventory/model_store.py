# Copyright © 2021 by IoT Spectator. All rights reserved.

"""Store for machine learning models."""

import sqlalchemy

from typing import Tuple

from sqlalchemy.orm import Session

from datainventory import _internal_store
from datainventory import common


class Model(common.Base):
    __tablename__ = "model"

    name = sqlalchemy.Column(sqlalchemy.String)
    version = sqlalchemy.Column(sqlalchemy.String)


class ModelStore(_internal_store.InternalStore):

    def __init__(self, create_key, device_id: str, session: Session) -> None:
        _internal_store.InternalStore.__init__(self, create_key, device_id)

    def get_model(self, name: str, version: str) -> Tuple:
        """Retrieve the model according to the name and version from database."""
        raise NotImplementedError("The function is not implemented.")
