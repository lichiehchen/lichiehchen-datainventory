import enum
import pathlib


class MediaType(enum.Enum):
    Audio = enum.auto()
    Image = enum.auto()
    Video = enum.auto()


class MultimediaStore:
    def __init__(self) -> None:
        pass

    def insert(
        self, filename: str, media_type: MediaType, location: pathlib.Path, **kwargs
    ) -> None:
        pass

