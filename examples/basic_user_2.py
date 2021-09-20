"""An example shows how to use Data Inventory."""
import pathlib

from datainventory import common
from datainventory import inventory
from datainventory import media_store


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

# Generate random binary files
test_video_name = pathlib.Path("video.mp4")
test_video: pathlib.Path = inventorydir / test_video_name
test_video.write_bytes(b"Video file contents")

test_audio_name = pathlib.Path("audio.mp3")
test_audio: pathlib.Path = inventorydir / test_audio_name
test_audio.write_bytes(b"Audio file contents")

test_image_name = pathlib.Path("image.jpg")
test_image: pathlib.Path = inventorydir / test_image_name
test_image.write_bytes(b"Video file contents")

media = my_inventory.get_media_store()
media.insert_media(
    file_path=test_video, media_type=media_store.MediaType.Video, copy=False
)
media.insert_media(
    file_path=test_audio, media_type=media_store.MediaType.Audio, copy=False
)
media.insert_media(
    file_path=test_image, media_type=media_store.MediaType.Image, copy=False
)

# Use export() method to dump the inventory
my_inventory.export(dest_filename=pathlib.Path("archive"))
