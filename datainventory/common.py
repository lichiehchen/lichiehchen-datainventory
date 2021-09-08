import datetime
import enum
import sqlalchemy

from typing import NewType, Tuple, Union


Start = NewType("Start", datetime.datetime)
End = NewType("End", datetime.datetime)
Interval = NewType("Interval", datetime.timedelta)

Range = Union[None, Tuple[Start, Interval], Tuple[Start, End]]


class ColumnType(enum.Enum):
    """Supported custom data type."""

    Binary = sqlalchemy.LargeBinary
    Boolean = sqlalchemy.Boolean
    DateTime = sqlalchemy.DateTime
    Float = sqlalchemy.Float
    Integer = sqlalchemy.Integer
    String = sqlalchemy.String
