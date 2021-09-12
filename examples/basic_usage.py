"""An example shows how to use Data Inventory."""
import pathlib

from datainventory import datainventory
from datainventory import simple_store

# The inventory directory location
inventorydir = pathlib.Path("inventorydir")
inventory = datainventory.DataInventory(device_id="device_id", inventory=inventorydir)

# Get the simple store from the inventory
simple = inventory.get_simple_store()

# Insert temperature data
simple.insert_temperature(simple_store.Scale.Fahrenheit, 3.0)

# Add customer table
simple.create_custom_table(
    table="my_table",
    columns={
        "column1": simple_store.CustomType.Integer,
        "column2": simple_store.CustomType.Text,
    },
)

# Insert custom data into the custom table
simple.insert_custom_data(
    table="my_table", data={"column1": 123, "column2": "text_data"}
)

# Use destroy() method to clean the inventory
# inventory.destroy()
