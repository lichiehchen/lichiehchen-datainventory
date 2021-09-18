"""An example shows how to use Data Inventory."""
import pathlib

from datetime import date
from datetime import timedelta

from datainventory import common
from datainventory import inventory


# The inventory directory location
inventorydir = pathlib.Path("inventorydir")
my_inventory = inventory.Inventory(device_id="device_id", inventory=inventorydir)

# Get the table store from the inventory
store = my_inventory.get_table_store()

# Create a temperature table
TABLE = "temperature"

SCHEMA = {"scale": common.ColumnType.String, "value": common.ColumnType.Float}
store.create_table(table_name=TABLE, columns=SCHEMA)

# Insert temperature data
data = [{"scale": "F", "value": 97.9}, {"scale": "C", "value": 23.7}]
store.insert(table_name=TABLE, values=data)

# Query the data
range = common.Range(date.today(), interval=timedelta(days=1))
output = store.query_data(TABLE, range=range)
print(output)

# Use export() method to dump the inventory
my_inventory.export(dest_filename=pathlib.Path("archive"))

# Use destroy() method to clean the inventory
my_inventory.destroy()
