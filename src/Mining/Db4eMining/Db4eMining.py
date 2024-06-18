#!/usr/bin/python3
"""
Mining/Db4eMining/Db4eMining.py
"""
import sys
from persistent.list import PersistentList
import transaction

# Append the Infrastructure directory to the Python path
project_dirs = [ 
  "/opt/prod/db4e/src/Infrastructure", 
  "/opt/prod/db4e/src/Mining", 
  "/opt/prod/db4e/src/Reports"
]
for project_dir in project_dirs:
  sys.path.append(project_dir)

# Import required db4e modules.
from P2Pool.P2Pool import P2Pool

class Db4eMining():

  def __init__(self, db):
    self._db = db
    self._conn = None
    self._root = None
    self.init_db()

  def init_db(self):
    root = self.root()
    mining = root['mining']
    if not hasattr(mining, 'p2pools'):
      mining.p2pools = PersistentList()
      transaction.commit()
    if not hasattr(mining, 'wallets'):
      mining.wallets = PersistentList()
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

  def interactive_menu(self):
    keep_looping = True
    while keep_looping:
      print(f"---------- Db4eMining Menu ----------------")
      print("  (S) - Status information")
      print("  (P) - P2Pools Menu")
      print("  (M) - Miners Menu")
      print("  (X) - Exit menu")
      choice = input("Enter your choice: ")

      if choice == "S" or choice == "s":
        self.print_status()
      
      if choice == "P" or choice == "p":
        self.p2pools_interactive_menu()

      elif choice == "X" or choice == "x":
        keep_looping = False

      else:
        print("Invalid choice, please try again")

  def p2pools_interactive_menu(self):
    print(f"---------- P2Pools Menu -------------------")
    print("  (A) - Add a new P2Pool")
    choice = input("Enter your choice: ")

    if choice == "A":
      self.add_p2pool()

  def add_p2pool(self):
    root = self.root()
    p2pool_name = input("Enter a name for the new P2Pool: ")
    p2pool = P2Pool(p2pool_name, self.db())
    p2pool.add_interactive_menu()

  def print_status(self):
    print("---------- Db4eMining Status --------------")
    root = self.root()
    print(f"{root.mining}")
    print("---------- P2Pools ------------------------")
    print(f"{root.mining.p2pools}")
    print("---------- Miners -------------------------")
  
def main():
  db4e = Db4eRoot()
  db = db4e.db()
  mining = Db4eMining(db)
  mining.print_status()

if __name__ == '__main__':
    main()