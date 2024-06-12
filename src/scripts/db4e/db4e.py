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
  "/opt/prod/db4e/assets/py/Infrastructure", 
  "/opt/prod/db4e/assets/py/Mining", 
  "/opt/prod/db4e/assets/py/Reports"
]
for project_dir in project_dirs:
  sys.path.append(project_dir)

# Import required db4e modules.
from Db4eRoot.Db4eRoot import Db4eRoot
from Db4eStorage.Db4eStorage import Db4eStorage
from Db4eStartup.Db4eStartup import Db4eStartup
from Report.Report import Report
from Wallets.Wallets import Wallets

def interactive_menu(db4eStorage, db4eRoot):
  """
  Print an interactive menu, providing the user with a menu interface for executing
  db4e functions. Also, process the user's choice.
  """
  while True:
    print("\n========== Database 4 Everything ========")
    print("")
    print("  1. Status")
    print("  2. Add Domain")
    print("  3. Exit\n")
    choice = input("Enter your choice: ")

    if choice == "1":
      print("\n========== Status ========================")
      db4eRoot.print_status()
      db4eStorage.print_status()

    elif choice == "2":
      print("\n  1. Mining Ops")
      print("  2. Shopping")
      print("  3. Budget\n")
      choice = input("Enter your choice: ")
      if choice == "1":
        db4eRoot.add_domain('mining')

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
    p2pool = myDb4eRoot.root['p2pools'].P2Pool()
    p2pool.monitor_log()

  elif args.action == None:
    interactive_menu(myStorage, myDb4eRoot)
    
if __name__ == "__main__":
  main()
