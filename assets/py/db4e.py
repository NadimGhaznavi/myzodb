#!/usr/bin/python3
"""
This script, db4e.py, is the entry point of the "Database 4 Everything" application. 
It is responsible for initializing the database, managing connections, and running the 
application.
"""

import os
import sys
import ZODB, ZODB.FileStorage
import argparse
import configparser
"""
Include supporting modules:
* os
* sys
* ZODB, ZODB.FileStorage
* argparse
* configparser
"""

ini_file = "db4e.ini"
"""
Global Variables

The myzodb.py script uses two global variables:
* ini_file : The configuration file for the db4e application. The default value for this global 
is db4e.ini. The configuraiton file should be in the same directory as this db4e.sh
script. This default is hard-coded into the application

See command line arguments for information on overriding this at runtime.
"""

# Deal with command line args
parser = argparse.ArgumentParser(description='My ZODB Application')
parser.add_argument('-i', '--ini_file', type=str, default=ini_file, help='Path to the INI file')
parser.add_argument('-a', '--action', type=str, help='Action to perform')
parser.add_argument('-c', '--csv_file', type=str, default=None, help='Path to the CSV file')
"""
Command Line Arguments

The myzodb.py script supports the following command line arguments:
* [-i | --ini_file] : Path to the configuration file for the db4e application
* [-a | --action] : An action. See function documentation for supported actions.
* [-c | --csv_file] : The path to a CSV file. This is used by some actions to import or export data.
"""

class Db4e(Db4eRoot):
  """
  This class is at the center of this control script. The script, db4e.py, that contains this 
  class definition should be invoked directly to interact with the db4e application.
  """
  pass

    def load_xmr_earnings_from_csv(csv_file: str) -> None:
    """
    Import appropriate xmr_mining functions and classes, and execute the code to import XMR mining data from a CSV file.
  Args:
  * csv_file (str): Path to the CSV file containing the XMR mining data
  Returns:
  * None
  """

  if not csv_file:
    # Try and get the CSV file location from the commandline arguments
    csv_file = args.csv_file
    if not csv_file:
      print("ERROR: Missing mandatory -c switch")
      exit_app(1)

  if not os.path.isfile(file_path):
    print("ERROR: CSV does not exist, exiting...")
    exit_app(1)

  if not os.access(csv_file, os.R_OK):
    print(f"ERROR: CSV file ({csv_file}) exists, but is not readable, exiting...")
    exit_app(1)

  setup_zodb(zodb_file_path)
  print("TBD... not yet loading CSV data from: ", csv_file)        

def print_status() -> None:
  """
  Print the status of the MyZODB application. Currently this is the following:
  * Path to the backend ZODB object database
  * Path to the configuration (INI) file zodb_file_path,for the MyZODB application
  Returns:
  * None
  """
  print("\n========== Status =====")
  print("ZODB file location: ", zodb_file_path)
  print("INI file location: ", ini_file_path)
    
def execute_load_xmr_earnings_from_csv() -> None:
  """
  This function is called from the interactive MyZODB menu. If a user chooses
  the option to load XMR earnings from a CSV file, then the user needs to 
  specify where that CSV file is located. This functionality is implemented here.
  Once the CSV file has been provided this function calls the 
  load_xmr_earnings_from_csv(csv_file) function. 
  """
  csv_file = input("Enter CSV location: ")
  load_xmr_earnings_from_csv(csv_file)

def exit_app(return_code) -> None:
  """
  Exit gracefully. Close the ZODB database if it is open. Exits with a return 
  code of zero unless a return code was passed in.
  """
  if zodb_handle != None:
    zodb_handle.close()
    
  if return_code == None:
    exit(0)
  else:
    exit(return_code)

def interactive_menu() -> None:
  """
  Print an interactive menu, providing the user with a menu interface for executing
  MyZODB functions. Also, process the user's choice.
  """
  while True:
    print("========== My ZODB Application ==========")
    print("")
    print("  1. Status")
    print("  2. Load XMR Earnings from CSV File")
    print("  3. Exit")
    print("")
    choice = input("Enter your choice: ")

    if choice == "1":
      print_status()

    elif choice == "2":
      execute_load_xmr_earnings()

    elif choice == "3":
      exit_app(0)

    else:
      print("Invalid choice. Please try again.")

def main(args: argparse.Namespace) -> None:
  """
  This is the main() function for the MyZODB application. It parses the
  command line arguments and executes the specified actions. If no command
  line arguments were provided, then an interactive menu is printed instead.
  """
  # Access global variables
  global ini_file_path
  # Get the location of the zodb file from the zodb.ini file
  config = configparser.ConfigParser()
  config.read(args.ini_file)
  zodb_file_path = config['ZODB']['file_path']
  ini_file_path = args.ini_file

  # See if an action was specified 
  if args.action == 'status':
    print_status()
    exit_app()

  elif args.action == 'loadxmrearningsfromcsv':
    execute_load_xmr_earnings()

  elif args.action == None:
    interactive_menu()
    
if __name__ == "__main__":
  args = parser.parse_args()
  try:
    main(args)
  except Exception as e:
    # Handle any errors and shutdown gracefully
    print(f"An error occured: {str(e)}")