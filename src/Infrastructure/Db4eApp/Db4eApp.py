#!/usr/bin/python3
"""
Infrastructure/Db4eApp/Db4eApp.py
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

# Import required db4e modules.
from Db4eStartup.Db4eStartup import Db4eStartup
from Db4eMongoDb.Db4eMongoDb import Db4eMongoDb
from MiningApp.MiningApp import MiningApp

class Db4eApp():
  def __init__(self):
    pass

  def menu(self):
    keep_looping = True
    while keep_looping:
      print("\n---------- App Menu -----------------------")
      print("  Menu options:")
      print("    (S)tatus")
      print("    (M)ining Menu")
      print("    (E)xit")
      choice = input("  Enter your choice [SME]: ")

      if choice == "S" or choice == "s":
        startup = Db4eStartup()
        startup.print_status()
        db = Db4eMongoDb()
        db.print_status()
        
      elif choice == "M" or choice == "m":
        mining_app = MiningApp()
        mining_app.menu()
      
      elif choice == "E" or choice == "e":
        keep_looping = False

      else:
        print("Invalid choice, try again")
  
def main():
  app = Db4eApp()
  app.menu()

if __name__ == '__main__':
  main()