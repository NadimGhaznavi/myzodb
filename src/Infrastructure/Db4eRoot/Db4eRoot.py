#!/usr/bin/python3
"""
Infrastructure/Db4eRoot/Db4eRoot.py
"""
import sys

# Append the Infrastructure directory to the Python path
project_dirs = [ 
  "/opt/prod/db4e/src/Infrastructure", 
  "/opt/prod/db4e/src/Mining", 
  "/opt/prod/db4e/src/Reports"
]
for project_dir in project_dirs:
  sys.path.append(project_dir)

# Import "Database 4 Everything modules"
from Db4eStartup.Db4eStartup import Db4eStartup
from Db4eMining.Db4eMining import Db4eMining

# Db4eRoot is a child of the persistent class
from persistent import Persistent

# The backend storage is implemented with the ZODB
from ZODB.FileStorage import FileStorage
from ZODB.DB import DB
from ZODB.PersistentMapping import PersistentMapping
import transaction

class Db4eRoot(Persistent):

  def __init__(self):
    self._db = None
    self._conn = None
    self._root = None
    self._storage_file = None
    self.init_app()
  
  def init_app(self):
    # Get the storage file location, based on how this
    # was launched (e.g. --environ qa)
    startup = Db4eStartup()
    self._storage_file = startup.storage_file()
    
    # Cpnfigure a stprage pbkect to use the storage file we found
    storage = FileStorage(self._storage_file)
    # Create a database and associate it with the storage
    self._db = DB(storage)
    self.init_db()

  def init_db(self):
    root = self.root()
    if not hasattr(root, 'mining'):

      root['mining'] = PersistentMapping
      transaction.commit()
  
  def db(self):
    return self._db
  
  def conn(self):
    if not self._conn:
      self._conn = self._db.open()
    return self._conn
  
  def root(self):
    if not self._root:
      conn = self.conn()
      self._root = conn.root()
    return self._root

  def __del__(self):
    if self._db:
      self._db.close()

  def print_status(self):
    print("---------- Db4eRoot Status ----------------")
    print(f"Storage file   : {self._storage_file}")
    print(f"DB             : {self._db}")
    print(f"DB connection  : {self._conn}")
    print(f"DB root object : {self._root}")

  def interactive_menu(self):
    while True:
      print("---------- Db4eRoot Menu ------------------")
      print("  (S) - Status information")
      print("  (M) - Mining menu")
      print("  (X) - Exit application")
      choice = input("Enter your choice: ")

      if choice == "S" or choice == "s":
        self.print_status()

      elif choice == "M" or choice == "m":
        mining = Db4eMining(self.db())
        mining.interactive_menu()

      elif choice == "X" or choice == "x":
        sys.exit(0)

      else:
        print("Invalid choice, please try again")
    
def main():
  db4eRoot = Db4eRoot()
  db4eRoot.interactive_menu()

if __name__ == '__main__':
  main()