"""
Mining/P2Pool/P2Pool.py
"""
import os, sys
import datetime
import time
from persistent.list import PersistentList
import transaction
import re

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
from BlockFoundEvent.BlockFoundEvent import BlockFoundEvent
from MiningZODB.MiningZODB import MiningZODB

class P2Pool():

  def __init__(self):
    self._name = None
    self._hostname = None
    self._ip_addr = None
    self._wallet = None
    self._miners = PersistentList

    startup = Db4eStartup()
    self._log_file = startup.p2pool_log()
  
  def config_menu(self):
    self._name = input("Enter a name for this P2Pool daemon: ")
    self._hostname = input("Enter the hostname where P2Pool is running: ")
    self._ip_addr = input("Enter IP address of the host where P2Pool is running: ")
    self._wallet = input("Enter the wallet def print_address for payouts:\n  ")
    self._log_file = input("Enter path to P2Pool logfile: ")
  
  def monitor_log(self):
    self._log_handle = open(self._log_file)
    p2log = self._log_handle
    p2log.seek(0, os.SEEK_END) # End-of-file
    
    while True:
      log_line = p2log.readline()
      if not log_line:
        time.sleep(5)
        continue

      print(f"P2Pool log: {log_line}"[0:-1])

      # 2024-06-12 10:06:28.0478 P2Pool BLOCK FOUND: main chain block at height 3169541 was mined by someone else in this p2pool
      pattern = r"^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d+) P2Pool BLOCK FOUND.*$"
      match = re.search(pattern, log_line)
      if match:
        # "Block Found" event
        timestamp_str = match.group(1)
        timestamp = datetime.datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S.%f")
        print("BLOCK FOUND EVENT")
        event = BlockFoundEvent(self._name, timestamp)
        miningDb = MiningZODB()
        miningDb.add_block_found_event(event)

  def menu(self):
    keep_looping = True
    while keep_looping:
      print(f"---------- P2Pool Menu ------------------")
      print("  Menu options:")
      print("    (M)onitor P2Pool Daemon Log")
      print("    (C)onfigure P2Pool")
      print("    E(x)it menu")
      choice = input("enter your choice: [MCX]: ")

      if choice == "M" or choice == "m":
        self.monitor_log()

      elif choice == "C" or choice == "c":
        self.config_menu()

      elif choice == "X" or choice == "x":
        keep_looping = False

      else:
        print("Invalid choice, please try again")

  def name(self, new_name=None):
    if new_name:
      self._name = new_name
    return self._name

  
