#!/usr/bin/python3
"""
Infrastructure/Db4eStorage/Db4eStorage.py
"""
from ZODB.FileStorage import FileStorage
from ZODB.DB import DB

class Db4eStorage():

  def __init__(self, storage_file, environ):
    self._storage_file = storage_file
    self._environ = environ

    # Get some backend storage
    self._storage = FileStorage(storage_file)
    # Get a database that's using the storage
    self._db = DB(self._storage)
    # Get a connectionto the database
    self._conn = self._db.open()
    # Get the root object out of the database
    self._root = self._conn.root()

  def connection(self):
    return self._connection

  def root(self):
    return self._root
  
  def storage(self):
    return self._storage
  
  def zodb_file(self):
    return self._zodb_file

  def environ(self):
    return self._environ
  
  def print_status(self):
    print(f"---------- Storage Status ----------------")
    print(f"Environment  : {self._environ}")
    print(f"Storage file : {self._zodb_file}")
    print(f"Connection   : {self._connection}")
    print(f"Root         : {self._root}")

  def __del__(self):
    # Close the ZODB when this object is about to be destroyed
    if self._connection:
      self._connection.close()
