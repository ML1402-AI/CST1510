class Record:
    def __init__(self, label, value, limit):
        self.label = label
        self.value = value
        self.limit = limit
    def status(self):
        """Returns the status of the record"""
        p=self.value/self.limit
        """calculates the percentage of value to limit and returns the status"""
        if p<100:
            return"OVER LIMIT"
        elif p<90:
            return"WARNING"
        else:
            return"OK"
#
#    Threshold : __init__(self, label, value, limit) storing all three as
#                attributes. No methods yet.
#    Typical   : add a method status(self) that returns "OVER LIMIT" (100%+),
#                "WARNING" (90%+) or "OK", worked out from self.value and
#                self.limit. Give it a one-line docstring.
#    Excellent : also add over_limit_count as a class-level running total -
#                see the note below.

# your class goes here
class count:
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
    records=[]
    with open("labfile.txt", "r") as f:
        for line in f:
            label, value, limit = line.strip().split(",")
            records.append(Record(label, float(value), float(limit)))
    return records
#
#    Threshold : create at least 2 Record instances directly in the code.
#    Typical   : same, but now print each one's .status() as well.
#    Excellent : instead, write load_records(path) that reads label,value,limit
#                lines from a file and returns a list of Record objects. Make
#                your own data file, one record per line.

  # replace with your code


# ==================================================================== OUTPUT
# 3. Print a report for each record.
#
#    Threshold : label, value, limit, inside a border.
#    Typical   : add the result of .status().
#    Excellent : also keep a running count of how many came back OVER LIMIT
#                across every record, and print that once, after the loop.
#                (Simplest: a plain variable outside the loop, same pattern
#                as Week 4. If you want it to live ON the object instead,
#                that is a stretch worth trying - but a variable is enough.)

for record in load_records("labfile.txt"):
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {record.label}")
    print("=" * 34)
    print(f"  Value: {record.value}")
    print(f"  Limit: {record.limit}")
    print(f"  Status: {record.status()}")



    print("=" * 34)
print(f"OVER LIMIT COUNT is {count.over_limit_count}")


# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it and check every record's numbers by hand
#    [ ] Check every method only reads/changes its OWN object (self) -
#        nothing reaches outside itself
#    [ ] Check every method and __init__ has a one-line docstring
