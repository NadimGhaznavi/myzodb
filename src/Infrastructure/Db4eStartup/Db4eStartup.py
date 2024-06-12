#!/usr/bin/python3

import argparse
import configparser

"""
Global Variables

The myzodb.py script uses two global variables:
* ini_file 

The configuration file for the db4e application. The default value for this global 
is db4e.ini. The configuraiton file should be in the same directory as this db4e.sh
script. This default is coded into the application

See command line arguments for information on overriding this coded value.
"""

ini_file = "/opt/prod/db4e/src/scripts/db4e/db4e.ini"

class Db4eStartup():

  def __init__(self):
    parser = argparse.ArgumentParser(description='db4e application')  
    parser.add_argument('-i', '--ini_file', type=str, default=ini_file, help='Path to the INI file')
    parser.add_argument('-a', '--action', type=str, default=None, help='Action to perform')
    parser.add_argument('-c', '--csv_file', type=str, default=None, help='Path to the CSV file')
    parser.add_argument('-e', '--environ', type=str, default=None, help='The operating environment e.g. prod, qa, dev')

    # Parse arguments
    args = parser.parse_args()
    self._args = args
  
    # Get the location of the zodb file from the zodb.ini file
    config = configparser.ConfigParser()
    config.read(args.ini_file)
    self._zodb_file = config['db4e']['storage_path']
    self._environ = config['db4e']['environment']
    self._p2pool_log = config['p2pool']['p2pool_log']
  
  def p2pool_log(self):
    return self._p2pool_log

  def zodb_file(self):
    return self._zodb_file
  
  def environ(self):
    return self._environ
  
  def args(self):
    """
    Get method.
    """
    return self._args
  