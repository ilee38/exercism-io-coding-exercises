from datetime import datetime
from datetime import timedelta

GIGASEC = 1000000000

def add(moment):
  if moment is None:
    raise ValueError("No time passed")
  return moment + timedelta(seconds=GIGASEC)
