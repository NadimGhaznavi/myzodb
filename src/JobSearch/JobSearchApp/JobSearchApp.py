#!/usr/bin/python3
"""
JobSearch/JobSearchApp/JobSearchApp.py
"""

import sys

# Append the Infrastructure directory to the Python path
project_dirs = [ 
  "/opt/prod/db4e/src/Infrastructure", 
  "/opt/prod/db4e/src/Mining", 
  "/opt/prod/db4e/src/Reports",
  "/opt/prod/db4e/src/JobSearch"
]
for project_dir in project_dirs:
  sys.path.append(project_dir)

# Import required db4e modules.
from Db4eStartup.Db4eStartup import Db4eStartup
from JobSearchDb.JobSearchDb import JobSearchDb

class JobSearchApp():

  def __init__(self):
    pass

  def menu(self):
    keep_looping = True
    while keep_looping:
      print("\n---------- Job Search Menu ----------------")
      print("  Menu options:")
      print("    1. Status")
      print("    2. Enter Job Search Information")
      print("    x. Exit")
      choice = input("  Enter your choice: ")

      if choice == "1":
        self.print_status()

      if choice == "2":
        self.enter_job_info()

      if choice == "x" or choice == "X":
        keep_looping = False

  def enter_job_info(self):
    print("\n---------- Job Info -----------------------")
    title = input("  Enter the job title: ")
    company = input("  Enter the company name: ")
    agency = input("  If applicable, nter the agency name: ")
    desc = input("  Enter a description of the job:  ")
    url = input("  Enter a URL for the job posting: ")
    jobsDb = JobSearchDb()
    jobsDb.add_job(title, company, agency, desc, url)
  
def main():
  app = JobSearchApp()
  app.menu()

if __name__ == '__main__':
  main()