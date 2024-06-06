import argparse
import configparser

class Db4eStartup():

  def __init__(self, args):
    parser = argparse.ArgumentParser(description='db4e application')  
    parser.add_argument('-i', '--ini_file', type=str, default=ini_file, help='Path to the INI file')
    parser.add_argument('-a', '--action', type=str, default=None, help='Action to perform')
    parser.add_argument('-c', '--csv_file', type=str, default=None, help='Path to the CSV file')
    parser.add_argument('-e', '--environ', type=str, default=None, help='The operating environment e.g. prod, qa, dev')

    # Parse arguments
    args = parser.parse_args()
  
    # Get the location of the zodb file from the zodb.ini file
    config = configparser.ConfigParser()
    config.read(args.ini_file)
    self.zodb_file = config['db4e']['file_path']
    self.environ = config['db4e']['environment']
  
  def zodb_file(self):
    return self.zodb_file
  
  def environ(self):
    return self.environ