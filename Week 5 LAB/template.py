"""
RECORD CHECK  -  my version
===========================

Name  : Maliha
Lane  :  AI / Cyber / IT      (delete two)
Date  : October 21st, 2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ====================================================================== CLASS
# 1. Define a class called Record.
class Record:
    def __init__(self, label, value, limit):
        """ Initializes a record with a label, value and limit"""
        self.label = label
        self.value = value
        self.limit = limit
    def status(self):
        """Calculates and returns the status of the record"""
        p=(self.value/self.limit)*100
        if p>100:
            return"OVER LIMIT"
        elif p>90:
            return"WARNING"
        else:
            return"OK"

class count(Record):
    """Initializes a record and updates the over-limit counter"""
    over_limit_count = 0
    def __init__(self, label, value, limit):
        self.label = label
        self.value = value
        self.limit = limit
        if self.status() == "OVER LIMIT":
            count.over_limit_count += 1

# ==================================================================== RECORDS
# 2. Create your records.
def load_records(path):
    """Loads records from a text file"""
    records=[]
    with open(path, "r") as f:
        for line in f:
            label, value, limit = line.strip().split(",")
            records.append(count(label, float(value), float(limit)))
        return records
records=load_records("labfile.txt")


# ==================================================================== OUTPUT


for line in records:
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {line.label}")
    print("=" * 34)
    print(f"  Value: {line.value}")
    print(f"  Limit: {line.limit}")
    print(f"  Status: {line.status()}")
    print("=" * 34)


print(f"OVER LIMIT COUNT is {count.over_limit_count}")


