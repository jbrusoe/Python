#Function demo used with EnterTemperature.py
#Written by: Jeff Brusoe

def is_int(input):
  try:
    num = int(input)
  except ValueError:
    return False
  return True

def is_float(input):
  try:
    num = float(input)
  except ValueError:
    return False
  return True
