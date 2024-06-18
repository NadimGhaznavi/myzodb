#!/usr/bin/python3
"""
Location of this file in the db4e application deployment:
* scripts/db4e/db4e.py

This script, db4e.py, is the entry point of the "Database 4 Everything" application. 
It is responsible for initializing the database, managing connections, and running the 
application.
"""

import os
import sys
import argparse
import configparser
import pathlib

# Append the Infrastructure directory to the Python path
project_dirs = [ 
  "/opt/prod/db4e/src/Infrastructure", 
  "/opt/prod/db4e/src/Mining", 
  "/opt/prod/db4e/src/Reports"
]
for project_dir in project_dirs:
  sys.path.append(project_dir)

print("sys.path")
for aDir in sys.path:
  print(f"  {aDir}")

# Import required db4e modules.
from Db4eRoot.Db4eRoot import Db4eRoot

def interactive_menu(db4eStorage, db4eRoot):
  """
  Print an interactive menu, providing the user with a menu interface for executing
  db4e functions. Also, process the user's choice.
  """
  while True:
    # app = Db4eApp()
    # app.interactive_menu()
    print("\n========== Database 4 Everything ========\n")
    print("  1. Status")
    print("  2. Initialize")
    print("  3. Exit\n")
    choice = input("Enter your choice: ")

    if choice == "1":
      print("\n========== Status ========================")
      db4eRoot.print_status()
      db4eStorage.print_status()

    elif choice == "2":
      db4eRoot.init_schema()

    elif choice == "3":
      sys.exit(0)

    else:
      print("Invalid choice. Please try again.")
      interactive_menu(db4eStorage, db4eRoot)


def main():
  """
  This is the main() function for the MyZODB application. It parses the
  command line arguments and executes the specified actions. If no command
  line arguments were provided, then an interactive menu is printed instead.
  """
  
  # Parse command line args, read INI file
  myStartup = Db4eStartup()
  zodb_file = myStartup.zodb_file()
  environ = myStartup.environ()

  myStorage = Db4eStorage(zodb_file, environ)
  myDb4eRoot = Db4eRoot(myStorage.root())
  
  # Parse command line args if any
  args = myStartup.args()
  
  # See if an action was specified 
  if args.action == 'status':
    myStorage.print_status()
    myDb4eRoot.print_status()
  
  elif args.action == 'loadxmrearningsfromcsv':
    myReport = myDb4eRoot.root['reports'].EarningsReport()
    myReport.updateCsv()
  
  elif args.action == 'monp2poollog':
    myDb4eRoot.root.mining.p2pool.mon_log()

  elif args.action == None:
    interactive_menu(myStorage, myDb4eRoot)
    
if __name__ == "__main__":
  main()
