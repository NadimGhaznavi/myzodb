#!/usr/bin/python3
"""
This script, db4e.py, is the entry point of the "Database 4 Everything" application. 
It is responsible for initializing the database, managing connections, and running the 
application.
"""

import os
import sys
import argparse
import configparser

sys.path.append(os.path.join(os.getcwd(), "Db4eRoot"))
from Db4eRoot import Db4eRoot


# import Db4e classes
"""
Include supporting modules:
* os
* sys
"""

# Global variables
# INI filename
ini_file = "db4e.ini"

"""
Global Variables

The myzodb.py script uses two global variables:
* ini_file 

The configuration file for the db4e application. The default value for this global 
is db4e.ini. The configuraiton file should be in the same directory as this db4e.sh
script. This default is coded into the application

See command line arguments for information on overriding this coded value.
"""

# Deal with command line args
parser = argparse.ArgumentParser(description='My ZODB Application')
parser.add_argument('-i', '--ini_file', type=str, default=ini_file, help='Path to the INI file')
parser.add_argument('-a', '--action', type=str, default=None, help='Action to perform')
parser.add_argument('-c', '--csv_file', type=str, default=None, help='Path to the CSV file')
"""
Command Line Arguments

The myzodb.py script supports the following command line arguments:
* [-i | --ini_file] : Path to the configuration file for the db4e application
* [-a | --action] : An action. See function documentation for supported actions.
* [-c | --csv_file] : The path to a CSV file. This is used by some actions to import or export data.
"""

def main(args: argparse.Namespace) -> None:
  """
  This is the main() function for the MyZODB application. It parses the
  command line arguments and executes the specified actions. If no command
  line arguments were provided, then an interactive menu is printed instead.
  """
  # Get the location of the zodb file from the zodb.ini file
  config = configparser.ConfigParser()
  config.read(args.ini_file)
  zodb_file_path = config['db4e']['file_path']
  
  myDb4e = Db4eRoot.Db4eRoot(zodb_file_path)

  # See if an action was specified 
  if args.action == 'status':
    myDb4e.print_status()
  
  elif args.action == 'loadxmrearningsfromcsv':
    pass
    #myChart = EarningsChart.EarningsChart()
    #myChart.updateCsv()
  
  elif args.action == 'monp2poollog':
    pass
    #myP2pool = P2Pool()
    #myP2Pool.monitor_log()  

  elif args.action == None:
    myDb4e.interactive_menu()
    
if __name__ == "__main__":
  args = parser.parse_args()
  try:
    main(args)
  except Exception as e:
    # Handle any errors and shutdown gracefully
    print(f"An error occured: {str(e)}")
