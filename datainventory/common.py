import datetime
import enum
import sqlalchemy

from typing import Optional

from sqlalchemy.ext import declarative

Base = declarative.declarative_base()


class Range:
    def __init__(
        self,
        start: datetime.datetime,
        end: Optional[datetime.datetime] = None,
        interval: Optional[datetime.timedelta] = None,
    ) -> None:
        self._start = start
        self._end = end
        if interval:
            self._end = self._start + interval

    def get_range(self):
        return self._start, self._end


class ColumnType(enum.Enum):
    """Supported custom data type."""

    Binary = sqlalchemy.LargeBinary
    Boolean = sqlalchemy.Boolean
    DateTime = sqlalchemy.DateTime
    Float = sqlalchemy.Float
    Integer = sqlalchemy.Integer
    String = sqlalchemy.String
