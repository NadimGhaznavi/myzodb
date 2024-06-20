#!/usr/bin/python3
"""
scripts/db4e.py
"""

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
from Db4eApp.Db4eApp import Db4eApp

def main():
  app = Db4eApp()
  app.menu()

if __name__ == '__main__':
  main()

