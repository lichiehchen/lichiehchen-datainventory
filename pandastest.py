from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, sql

import pandas as pd
import sqlalchemy

from datainventory import _internal_store
from datainventory import common


engine = create_engine("sqlite:///test.db", echo=True)

"""
print(common.ColumnType.Binary.value)
mystore = _internal_store.InternalStore(create_key=_internal_store.CREATE_KEY, device_id="deviceid", sql_engine=engine)

mystore.create_table("table1", {"time": common.ColumnType.String, "name": common.ColumnType.String, "device": common.ColumnType.String})

mystore.insert("table1", [{"time": "ttt", "name": "anme1", "device": "aaa"}])

exit()
"""


meta = MetaData(bind=engine)
meta.reflect()
print(meta.tables)
"""
students = meta.tables["students"]

ins = students.insert().values(name = 'abc', lastname = 'def')
conn = engine.connect()
result = conn.execute(ins)
"""


"""
students = Table(
   'students', meta, 
   Column('id', Integer, primary_key = True), 
   Column('name', String), 
   Column('lastname', String), 
)

#meta.create_all(bind=engine)

#ins = students.insert()


students.create(bind=engine, checkfirst=True)
ins = students.insert().values(name = 'Ravi', lastname = 'Kapoor')
conn = engine.connect()
result = conn.execute(ins)
"""


# df = pd.read_sql_table("students", engine.connect())
# print(df)

# attrs = ["time", "name", "device"]
# types = [sqlalchemy.TIMESTAMP, sqlalchemy.String, sqlalchemy.String]


# table = Table("table", meta, *(Column(col, ctype) for col, ctype in zip(attrs, types)))
# table.create(bind=engine, checkfirst=True)
# print(table)


# dict1 = {"time": sqlalchemy.TIMESTAMP, "name": sqlalchemy.String, "device": sqlalchemy.String}
dict1 = {
    "time": common.ColumnType.DateTime,
    "name": common.ColumnType.String,
    "device": common.ColumnType.String,
}

# dict1["device_id"] = common.ColumnType.String
# dict1["timestamp"] = common.ColumnType.DateTime

# table = Table("table2", meta, *(Column(col, ctype.value) for col, ctype in dict1.items()))
# table.create(bind=engine, checkfirst=True)
# print(table)

# for key, value in dict1.items():
#    print(key, value)


engine = create_engine("sqlite:///abc.db", echo=True)
meta = MetaData(bind=engine)

mystore = _internal_store.InternalStore(
    create_key=_internal_store.CREATE_KEY,
    device_id="deviceid",
    sql_metadata=meta,
    sql_connection=engine.connect(),
)

mystore.create_table("table1", dict1)
from datetime import datetime

mystore.insert(
    "table1", [{"time": datetime.now(), "name": "aaa", "device": "mydevice"}]
)
