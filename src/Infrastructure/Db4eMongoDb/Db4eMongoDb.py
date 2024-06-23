#!/usr/bin/python3
"""
Infrastructure/Db4eMongoDb.py
"""
import sys
from pymongo import MongoClient

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

class Db4eMongoDb():

  def __init__(self):
    startup = Db4eStartup()

    self._mongodb_server = startup.mongodb_server()
    self._mongodb_port = startup.mongodb_port()
    self._db_name = startup.db_name()

    self.init_db()

  def db_name(self):
    return self._db_name

  def init_db(self):
    db = self.db()
    if 'common' not in db.list_collection_names():
      common_col = db["common"]
      common_col.insert_one({'history': {}})
    if 'mining' not in db.list_collection_names():
      mining = db["mining"]

  def history(self):
    db = self.db()
    common_col = db['common']
    return common_col

  def mongodb_port(self):
    return self._mongodb_port

  def mongodb_server(self):
    return self._mongodb_server

  def print_status(self):
    print("\n---------- Db4eMongoDb Status -------------")
    print(f"  MongoDb server : {self._mongodb_server}")
    print(f"  MongoDb port   : {self._mongodb_port}")
    print("----------- History -----------------------")
    history = self.history()
    for doc in history.find():
      print(doc)
      
        

  def db(self):
    mongodb_server = self.mongodb_server()
    mongodb_port = str(self.mongodb_port())
    db_name = self.db_name()
    try:
      my_client = MongoClient(f"mongodb://{mongodb_server}:{mongodb_port}/")
    except:
      print("FATAL ERROR: Could not connecto to MongoDb ({mongodb_server}:{mongodb_port})")
      sys.exit(1)

    return my_client[db_name]
  
def main():
  db = Db4eMongoDb()
  db.print_status()

if __name__ == '__main__':
  main()