import csv
from datetime import datetime
from typing import List

class ZMRPayment:
  def __init__(self, payment_amount, timestamp):
    self.payment_amount = payment_amount
    self.timestamp = timestamp

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
