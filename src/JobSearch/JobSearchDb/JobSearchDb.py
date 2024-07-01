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
from Db4eDb.Db4eDb import Db4eDb

class JobSearchDb():

  def __init__(self):
    pass

  def add_job(self, title, company, agency, desc, url):
    new_job = {
      'doc_type' : 'job_application',
      'title' : title,
      'company' : company,
      'agency' : agency,
      'desc' : desc,
      'url' : url
    }
    db = self.db()
    jobs_col = db["job_search"]
    jobs_col.insert_one(new_job)

  def db(self):
    db = Db4eDb()
    return db.db()
    
