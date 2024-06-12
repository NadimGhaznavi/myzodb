#!/usr/bin/python3

"""
Mining/P2PoolDaemon/P2PoolDaemon.py

A class to model the P2Pool daemon, part of the Monero XMR mining operation.
This class will monitor the P2Pool log file and create database entries based
on those log messages in the backend ZODB database.

A standalone script that can be invoked to start monitoring the P2Pool daemon
log. Suitable for being run in the same script that starts the P2Pool daemon,
thereby ensuring that all relevant log messages are written to the DB.
"""

import time
import os
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
from Db4eStorage.Db4eStorage import Db4eStorage
from Db4eRoot.Db4eRoot import Db4eRoot

sm_tab = "-" * 8 + " "

class P2PoolDaemon():
  
  

  def __init__(self, db4e_root, log_file):
    """
    Constructor.
    """
    self._log_file = log_file
    self._root = db4e_root
    self._log_handle = None

    """
    Function to monitor the P2Pool logfile. This function has no exit, but instead
    goes into an infinite loop. Operationally, this loop gets killed when the script
    that started this process gets killed.

    This function is a generator function. It reads each new line from the P2Pool
    log and makes it available. The consumer decides if the log message is noteworthy
    and if so then it writes the log message into a ZODB database.
    """

  def mon_log(self):
    self._log_handle = open(self._log_file)
    p2log = self._log_handle
    p2log.seek(0, os.SEEK_END) # End-of-file
    count = 0
    while True:
      line = p2log.readline()
      if not line:
        time.sleep(5)
        continue
      
      # Parse line, call record_db_event if needed
      # 2024-06-12 09:41:31.7115 StratumServer SHARE FOUND: mainchain height 3169532, sidechain height 0, diff 100000, client 192.168.1.11:40600, user kermit, effort 100.001%
      print(f"NEW LINE (#{count}): {line}")
      count = count + 1

  def __del__(self):
    if self._log_handle:
      self._log_handle.close()

  def interactive_menu(self):
    while True:
      print(f'{sm_tab}P2PoolDaemon')
      print(f"{sm_tab}1. Monitor log file")
      print(f"{sm_tab}2. Exit")
      choice = input("Enter your choice: ")
      if choice == "1":
        self.mon_log()
      elif choice == "2":
        sys.exit(0)
      else:
        print("Invalid choice. Please try again.")

  def write_db_record(self):
    pass

def main():
  # Parse command line args, read INI file
  myStartup = Db4eStartup()
  
  zodb_file = myStartup.zodb_file()
  environ = myStartup.environ()

  myStorage = Db4eStorage(zodb_file, environ)
  myDb4eRoot = Db4eRoot(myStorage.root())
  
  p2pool_log = myStartup.p2pool_log()
  myP2Pool = P2PoolDaemon(myDb4eRoot, p2pool_log)
  myP2Pool.interactive_menu()


if __name__ == "__main__":
  main()