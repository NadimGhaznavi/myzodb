"""
* Infrastructure/Db4eApp/Db4eApp.py

This code provides a user interface to the top level Database 4 Everything application. It manages adding, removing and 
engaging with domain specific applications. The Db4eApp class is responsible for adding and removing domains to and from
the db4e backend object storage.
"""

# Append the Infrastructure directory to the Python path
project_dirs = [ 
  "/opt/prod/db4e/assets/py/Infrastructure", 
  "/opt/prod/db4e/assets/py/Mining", 
  "/opt/prod/db4e/assets/py/Reports"
]
for project_dir in project_dirs:
  sys.path.append(project_dir)

from Db4eTree.Db4eTree import Db4eTree

class Db4eApp():

  def __init__(self, db4eRoot):
    self._root = db4eRoot

  def interactive_menu(self):
    while True:
      self.print_status()
      self.print_choices()
      self.do_choice(input("Enter your choice: "))

  def print_choices(self):
    
