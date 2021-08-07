# Copyright © 2021 by IoT Spectator. All rights reserved.

"""Store for multimedia data such as video, audio, and image."""

import enum
import pathlib
import sqlite3

from datainventory import _internal_store


class MediaType(enum.Enum):
    Audio = enum.auto()
    Image = enum.auto()
    Video = enum.auto()


class MediaStore(_internal_store.InternalStore):

    def __init__(
        self, create_key, device_id: str, connection: sqlite3.Connection
    ) -> None:
        _internal_store.InternalStore.__init__(self, create_key, device_id, connection)

    def insert_video(self, file_path: pathlib.Path) -> None:
        raise NotImplementedError("This function is not implemented")
