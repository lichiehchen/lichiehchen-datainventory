import sqlalchemy

from datainventory import _internal_store


def test_simple_case():
    engine = sqlalchemy.create_engine(
        "sqlite+pysqlite:///:memory:", echo=True, future=True
    )
    store = _internal_store.InternalStore(
        create_key=_internal_store.CREATE_KEY, device_id="unittest", sql_engine=engine
    )

    store.create_table(table="test_table", columns={})
