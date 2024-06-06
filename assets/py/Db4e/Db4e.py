
class Db4e(MyZODBRoot):
  """
  This is the brains of the db4e application. It initializes the application
  by reading the INI file and opening a connection to the backend database files.
  """
  
  ini_file = "db4e.ini"

  def __init__(self, root, name, value):
    super().__init__(root, name)
    self.value = value

    
