import ZODB, ZODB.FileStorage

class Db4eStorage():

  def __init__(self, zodb_file, environ):
    self._zodb_file = zodb_file
    self._environ = environ
    self._storage = ZODB.FileStorage.FileStorage(zodb_file)
    self._db = ZODB.DB(self._storage)
    self._db.open()
  
  def db(self):
    return self._db
  
  def storage(self):
    return self._storage
  
  def zodb_file(self):
    return self._zodb_file

  def environ(self):
    return self._environ
  
  def print_status(self):
    print(f"---------- Storage Status ----------------")
    print(f"Environment: {self._environ}")
    print(f"Storage file: {self._zodb_file}")

  def __del__(self):
    # Close the ZODB when this object is about to be destroyed
    if self._db:
      self._db.close()