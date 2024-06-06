#!/usr/bin/python3
"""
This script, db4e.py, is the entry point of the "Database 4 Everything" application. 
It is responsible for initializing the database, managing connections, and running the 
application.
"""

import os
import sys

# Add the Db4eRoot directory to the system path
sys.path.append(os.path.join(os.getcwd(), "Db4eRoot"))
sys.path.append(os.path.join(os.getcwd(), "Chart"))
sys.path.append(os.path.join(os.getcwd(), "Wallet"))
sys.path.append(os.path.join(os.getcwd(), "P2Pool"))
sys.path.append(os.path.join(os.getcwd(), "Db4eStorage"))
sys.path.append(os.path.join(os.getcwd(), "Db4eStartup"))

from Db4eRoot import Db4eRoot as Db4eRoot
from Chart import Chart as Chart
from Wallet import Wallet as Wallet
from Db4eStorage import Db4eStorage
from Db4eStartup import Db4eStartup

"""
Global Variables

The myzodb.py script uses two global variables:
* ini_file 

The configuration file for the db4e application. The default value for this global 
is db4e.ini. The configuraiton file should be in the same directory as this db4e.sh
script. This default is coded into the application

See command line arguments for information on overriding this coded value.
"""
ini_file = "db4e.ini"

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

  # Get a ZODB handle
  myRoot = Db4eStorage(zodb_file, environ)

  # Create a db4e ZODB root object instance
  myDb4e = Db4eRoot()
  myDb4e.db(myRoot)

  # See if an action was specified 
  if args.action == 'status':
    myDb4e.print_status()
  
  elif args.action == 'loadxmrearningsfromcsv':
    myChart = EarningsChart()
    myChart.updateCsv()
  
  elif args.action == 'monp2poollog':
    p2pool = P2Pool()
    p2pool.monitor_log()

  elif args.action == None:
    myDb4e.interactive_menu()
    
if __name__ == "__main__":
  main()
