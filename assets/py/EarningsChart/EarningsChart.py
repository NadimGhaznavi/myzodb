import csv
from datetime import datetime
from typing import List

class EarningsChart:
  def __init__(self):
    self.csv_file_name = None

def read_csv_to_payments(filename: str) -> List[ZMRPayment]:
  payments = []
  with open(filename, mode='r') as file:
    reader = csv.DictReader(file)
    next(reader)  # Skip the header row
    for row in reader:
      payment_amount = float(row['amount'])
      timestamp = datetime.strptime(row['date'], '%Y-%m-%d %H:%M:%S')
      payment = ZMRPayment(payment_amount, timestamp)
      payments.append(payment)

return payments

  if not csv_file:
    # Try and get the CSV file location from the commandline arguments
    csv_file = args.csv_file
    if not csv_file:
      print("ERROR: Missing mandatory -c switch")
      exit_app(1)

  if not os.path.isfile(file_path):
    print("ERROR: CSV does not exist, exiting...")
    exit_app(1)

  if not os.access(csv_file, os.R_OK):
    print(f"ERROR: CSV file ({csv_file}) exists, but is not readable, exiting...")
    exit_app(1)
