import os
import sys
import persistent
import transaction
from BTrees.OOBTree import TreeSet

# Append the Infrastructure directory to the Python path
project_dirs = [ 
  "/opt/prod/db4e/assets/py/Infrastructure", 
  "/opt/prod/db4e/assets/py/Mining", 
  "/opt/prod/db4e/assets/py/Reports"
]
for project_dir in project_dirs:
  sys.path.append(project_dir)

from Db4eTree.Db4eTree import Db4eTree

class Db4eHistory(persistent.Persistent):

  def __init__(self, db_connection):
    self._connection = db_connection
    self._root = db_connection.root
    self._records = TreeSet()
    
  

  def print_status(self):
    print(f"---------- History -----------------------")
    print(f"---------- Share Found Events ------------")
    print(f"---------- Block Found Events ------------")
    print(f"---------- XMR Transactions --------------")

def main():
  printf("---------- Storage Status ----------------")