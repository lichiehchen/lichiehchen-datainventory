import pathlib

from datainventory import datainventory
from datainventory import simple_store

myinventory = pathlib.Path("myinventory")
inventory = datainventory.DataInventory(device_id="mydevice", inventory=myinventory)

simple = inventory.get_simple_store()
simple.insert_temperature(simple_store.Scale.Fahrenheit, 3.0)

simple.create_custom_table(table="abc", columns={"key": "Integer", "key2": "Integer"})
simple.insert_custom_data(table="abc", data={"key": 123, "key2": 234})

# inventory.destroy()
