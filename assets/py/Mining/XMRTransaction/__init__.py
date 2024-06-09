import os
import ZODB, ZODB.FileStorage

# Define the ZODB file path
zodb_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), '../../data/myzodb.fs')

# Set up the ZODB database
storage = ZODB.FileStorage.FileStorage(zodb_file)
db = ZODB.DB(storage)

# Connect to the ZODB database and store the root object
with db.open() as connection:
    root = connection.root()

