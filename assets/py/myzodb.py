#!/usr/bin/python3

import os
import sys
import ZODB, ZODB.FileStorage
import argparse
import configparser

# Declare the location of the ZODB database file and the application INI files as globals
zodb_file_path = ""

ini_file_path = os.path.abspath("/opt/prod/websites/myzodb/data/myzodb.ini")

# Deal with command line args
parser = argparse.ArgumentParser(description='My ZODB Application')
parser.add_argument('-i', '--ini_file', type=str, default=ini_file_path, help='Path to the INI file')
parser.add_argument('-a', '--action', type=str, help='Action to perform')
parser.add_argument('-c', '--csv_file', type=str, default=None, help='Path to the CSV file')

def setup_zodb(zodb_file):
    storage = ZODB.FileStorage.FileStorage(zodb_file)
    db = ZODB.DB(storage)
    connection = db.open()
    root = connection.root()

def load_xmr_earnings_from_csv(csv_file):
    # Code to import appropriate xmr_mining functions and classes and execute 
    # the code to actually do the CSV import of the XMR mining data
    print("TBD... not yet loading CSV data from: ", csv_file)
            

def print_status():
    # Access global varables
    global zodb_file_path, ini_file_path
    print("\n========== Status =====")
    print("ZODB file location: ", zodb_file_path)
    print("INI file location: ", ini_file_path)

    
def print_menu():
    print("========== My ZODB Application ==========")
    print("")
    print("  1. Status")
    print("  2. Load XMR Earnings from CSV File")
    print("  3. Exit")
    print("")

def main(args):
    # Access global variables
    global zodb_file_path, ini_file_path
    # Get the location of the zodb file from the zodb.ini file
    config = configparser.ConfigParser()
    config.read(args.ini_file)
    zodb_file_path = config['ZODB']['file_path']
    ini_file_path = args.ini_file

    # See if an action was specified 
    if args.action == 'status':
        print_status()
        exit(0)

    elif args.action == 'loadxmrearningsfromcsv':
        csv_file = args.csv_file
        if csv_file == None:
            print("ERROR: Missing mandatory -c switch")
            exit(1)
        else:
            print("TBD")
        
    elif args.action == None:
        while True:
            print_menu()
            choice = input("Enter your choice: ")

            if choice == "1":
                print_status()

            elif choice == "2":
                setup_zodb(zodb_file_path)
                csv_file = input("Enter CSV location: ")
                load_xmr_earnings_from_csv(csv_file)

            elif choice == "3":
                exit(0)

            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    args = parser.parse_args()
    try:
        main(args)
    except Exception as e:
        # Handle any errors and shutdown gracefully
        print(f"An error occured: {str(e)}")
