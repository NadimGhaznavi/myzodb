class Db4eStorage():

  def __init__(self, zodb_file, environ):
    self.zodb_file = zodb_file
    self.environ = environ
    self.storage = ZODB.FileStorage.FileStorage(zodb_file)
    self.db = ZODB.DB(self.storage)
    return self.db.open()
  
  def db(self):
    return self.db
  
  def storage(self):
    return self.storage
  
  def environ(self):
    return self.environ
  
  def print_status(self):
    print(f"Environment: {self.environ}")
    print(f"Storage file: {self.zodb_file}")