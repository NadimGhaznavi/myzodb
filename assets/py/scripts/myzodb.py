#!/usr/bin/python3

import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__)))
from . import root

def print_status():
    zodb_file = os.path.abspath(root.storage.path)
    print(f"ZODB File Location: {zodb_file}")

def print_menu():
    print("========== My ZODB Application ==========")
    print("1. Status")
    print("More options to be added as needed")

def main():
    print_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        print("\n===== Status =====")
        print_status()
    else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
