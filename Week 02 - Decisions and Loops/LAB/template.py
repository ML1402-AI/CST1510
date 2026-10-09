"""
RECORD CHECK  -  my version
===========================

Name  : Maliha
Lane  :  AI    (delete two)
Date  : 1st October 2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ==================================================================== INPUT
# 1. Ask for your three values.
over_limit_count = 0
label = input("Please enter the name of the data set: ")
while label!="quit":

  value = float(input("Please enter the number of rows loaded: "))
  limit = float(input("Please enter the number of rows expected: "))

  difference = limit - value
  percent = (value/limit)*100

  if percent >= 100:
     status = "OVER LIMIT"
     over_limit_count += 1
  elif percent >= 90:
     status = "WARNING"
  else:
     status = "OK"

  print()
  print("=" * 34)
  print(f"  RECORD CHECK  -  {label}")
  print("=" * 34)
  print(f"{"Used":10}:{value:8.2f}")
  print(f"{"Total":10}:{limit:8.2f}")
  print(f"{"Free":10}:{difference:8.2f}")
  print(f"{"Percent":10}:{percent:8.2f}""%")
  print(f"{"Status":10}:{status:>8}")
  print("=" * 34)
  print("Number of records over limit is", over_limit_count)
  label = input("Please enter the name of the data set: ")



# ==========================================================================
# 5. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and note the error (do not fix it yet)
#    [ ] Check every variable name says what it holds
