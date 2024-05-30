#!/usr/bin/python3

# my_zodb.py - Front-end for accessing the master ZODB

import ZODB, ZODB.FileStorage, transaction

zodbFileName = "/opt/prod/websites/myzodb/data/myzodb.fs"

storage = ZODB.FileStorage.FileStorage(zodbFileName)
db = ZODB.DB(storage)
connection = db.open()
root = connection.root


