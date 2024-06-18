#!/usr/bin/python3
"""
Infrastructure/Db4eZODB/Db4eZODB.py
"""
import sys

from ZODB.FileStorage import FileStorage
from ZODB.DB import DB
from ZODB.PersistentMapping import PersistentMapping
import transaction, traceback
from BTrees.OOBTree import TreeSet

# Append the Infrastructure directory to the Python path
project_dirs = [ 
  "/opt/prod/db4e/src/Infrastructure", 
  "/opt/prod/db4e/src/Mining", 
  "/opt/prod/db4e/src/Reports"
]
for project_dir in project_dirs:
  sys.path.append(project_dir)

# Import required db4e modules.
from Db4eStartup.Db4eStartup import Db4eStartup

class Db4eZODB():

  def __init__(self):
    self._db = None
    self._conn = None
    self._root = None
    self._storage_file = None
    self.init_app()
    self.init_db()

  def __del__(self):
    if self._db and not self._conn:
      self._db.close()

  
  def commit(self):
    try:
      transaction.commit()
    except Exception as e:
      transaction.abort()
      traceback.print_exc()
    finally:
      self._db.close()

  def conn(self):
    if not self._conn:
      db = self.db()
      self._conn = db.open()
    return self._conn
  
  def db(self):
    if not self._db:
      storage_file = self.storage_file()
      storage = FileStorage(storage_file)
      self._db = DB(storage)
    return self._db
  
  def init_app(self):
    startup = Db4eStartup()
    self._storage_file = startup.storage_file()

  def init_db(self):
    root = self.root()
    if not hasattr(root, 'mining'):
      root.mining = PersistentMapping()
      self.commit()
    
    if not hasattr(root, 'history'):
      root.history = PersistentMapping()
      root.history['xmr_transactions'] = TreeSet()
      root.history['block_found_events'] = TreeSet()
      root.history['share_found_events'] = TreeSet()
      self.commit()

  def print_status(self):
    print("\n---------- Status -------------------------")
    print(f"  Database filename            : {self._storage_file}")
    print(f"  Database handle (_db)        : {self._db}")
    print(f"  Database connection (_conn)  : {self._conn}")
    
    # Make sure we're connected
    self.conn()
    print(f"  History")
    print(f"  XMR Transactions")
    print(f"  Block Found Events")
    for elem in self._root.history['block_found_events'].keys():
      print(f"  - {elem}")
    print(f"  Share Found Events")
    print(f"  Mining")
    
  def root(self):
    if not self._root:
      conn = self.conn()
      self._root = conn.root()
    return self._root
  
  def storage_file(self):
    if not self._storage_file:
      startup = Db4eStartup()
      self._storage_file = startup.storage_file()
    return self._storage_file
  
def main():
  db = Db4eZODB()
  db.print_status()

if __name__ == '__main__':
  main()