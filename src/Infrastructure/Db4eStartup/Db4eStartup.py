#!/usr/bin/python3
"""
scripts/db4e.py
"""
import argparse
import configparser

"""
Global Variables

This module uses two global variables shown below with their default
values.

* ini_file (/opt/prod/db4e/src/scripts/db4e.ini)
* environment (dev)

"""

ini_file = '/opt/prod/db4e/src/scripts/db4e.ini'
environment = 'dev'

class Db4eStartup():

  def __init__(self):
    parser = argparse.ArgumentParser(description='db4e application')  
    parser.add_argument('-a', '--action', type=str, default=None, help='Action to perform')
    parser.add_argument('-e', '--environ', type=str, default=environment, help='The operating environment e.g. prod, qa, dev')
    parser.add_argument('-i', '--ini_file', type=str, default=ini_file, help='Configuration file for the system')
    
    # Parse arguments
    args = parser.parse_args()
    self._args = args
  
    # prod, qa or dev
    self._environ = args.environ
    
    # Get the location of the zodb file from the zodb.ini file
    config = configparser.ConfigParser()
    config.read(args.ini_file)
    self._storage_file = config[args.environ]['storage_path']
    self._p2pool_log = config[args.environ]['p2pool_log']

  def print_status(self):
    print(f"---------- Db4eStartup Status -------------")
    print(f"Config file  : {ini_file}")
    print(f"Environment  : {self._environ}")
    print(f"Storage file : {self._storage_file}")
    print(f"P2P log      : {self._p2pool_log}")
  
  def p2pool_log(self):
    return self._p2pool_log

  def storage_file(self):
    return self._storage_file
  
  def environ(self):
    return self._environ

  def args(self):
    """
    Get method.
    """
    return self._args

def main():
  startup = Db4eStartup()
  startup.print_status()

if __name__ == '__main__':
  main()