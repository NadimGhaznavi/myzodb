#!/usr/bin/python3
"""
Infrastructure/Db4eApp/Db4eApp.py
"""

import sys

from ZODB.FileStorage import FileStorage
from ZODB.DB import DB
from ZODB.PersistentMapping import PersistentMapping
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
from Db4eStartup.Db4eStartup import Db4eStartup
from Db4eZOE.Db4eZOE import Db4eZOE
from P2Pool.P2Pool import P2Pool

class Db4eApp():
  def __init__(self):
    pass

  def menu(self):
    keep_looping = True
    while keep_looping:
      print("\n---------- App Menu -----------------------")
      print("  Menu options:")
      print("    (S)tatus")
      print("    (D)atabase 4 Everything")
      print("    (P)2Pool Menu")
      print("    E(x)it")
      choice = input("  Enter your choice [SDPX]: ")

      if choice == "S" or choice == "s":
        startup = Db4eStartup()
        startup.print_status()
        db = Db4eZOE()
        db.print_status()

      elif choice == "D" or choice == "d":
        db = Db4eZOE()
        db.print_status()

      elif choice == "P" or choice == "p":
        pool = P2Pool()
        pool.menu()
      
      elif choice == "X" or choice == "x":
        keep_looping = False

      else:
        print("Invalid choice, try again")
  
def main():
  app = Db4eApp()
  app.menu()

if __name__ == '__main__':
  main()