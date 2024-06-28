#!/usr/bin/python3
"""
scripts/db4e.py
"""

import sys

# Append the Infrastructure directory to the Python path
project_dirs = [ 
  "./db4e/src/Infrastructure", 
  "./db4e/src/Mining", 
  "./db4e/src/Reports"
]
for project_dir in project_dirs:
  sys.path.append(project_dir)

# Import required db4e modules.
from Db4eStartup.Db4eStartup import Db4eStartup
from Db4eApp.Db4eApp import Db4eApp
from P2Pool.P2Pool import P2Pool

def main():
  startup = Db4eStartup()
  if startup.action():
    action = startup.action()

    if action == 'monitor_p2pool_log':
      p2pool = P2Pool()
      p2pool.monitor_log()

  app = Db4eApp()
  app.menu()

if __name__ == '__main__':
  main()

