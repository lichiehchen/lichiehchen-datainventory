# Copyright © 2021 by IoT Spectator. All rights reserved.

"""Store for multimedia data such as video, audio, and image."""

import enum
import pathlib
import sqlalchemy

from sqlalchemy.orm import Session

from datainventory import _internal_store
from datainventory import common


class MediaType(enum.Enum):
    """Supporte media type."""

    Audio = enum.auto()
    Image = enum.auto()
    Video = enum.auto()


class Video(common.Base):
    """Table definition for video."""

    __tablename__ = "video"

    filename = sqlalchemy.Column(sqlalchemy.String, primary_key=True)
    location = sqlalchemy.Column(sqlalchemy.String)


class MediaStore(_internal_store.InternalStore):
    """Media Store."""

    def __init__(self, create_key, device_id: str, session: Session) -> None:
        _internal_store.InternalStore.__init__(self, create_key, device_id)

    def insert_video(self, file_path: pathlib.Path) -> None:
        """Insert a video."""
        raise NotImplementedError("This function is not implemented")

    def get_video(self) -> pathlib.Path:
        """Retrieve the video."""
        raise NotImplementedError("This function is not implemented")
