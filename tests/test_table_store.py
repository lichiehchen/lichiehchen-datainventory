import sqlalchemy

from datainventory import _internal_store
from datainventory import common
from datainventory import table_store


def test_simple_case():
    engine = sqlalchemy.create_engine(
        "sqlite+pysqlite:///:memory:", echo=True, future=True
    )
    metadata = sqlalchemy.MetaData(bind=engine)

    store = table_store.TableStore(
        create_key=_internal_store.CREATE_KEY,
        device_id="test_device",
        metadata=metadata,
        connection=engine.connect(),
    )

    schema = {"scale": common.ColumnType.String, "value": common.ColumnType.Float}
    store.create_table(table_name="temperature", columns=schema)

    data = [{"scale": "F", "value": 97.9}, {"scale": "C", "value": 23.7}]
    store.insert(table_name="temperature", values=data)

