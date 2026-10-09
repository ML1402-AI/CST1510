"""
RECORD CHECK  -  my version
===========================

Name  : Maliha
Lane  :  AI       (delete two)
Date  : 9th october 2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""


# STEP 1: FUNCTIONS

def status_of(percent):
    """Return the status based on the percentage."""
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"


def check(value, limit):
    """Calculate the difference and percentage."""
    difference = limit - value
    percent = (value / limit) * 100
    return difference, percent


def print_report(label, value, limit, difference, percent, status):
    """Print the formatted record report."""
    print("=" * 34)
    print(f"RECORD CHECK - {label}")
    print("=" * 34)
    print(f"Used    : {value:10.2f}")
    print(f"Total   : {limit:10.2f}")
    print(f"Free    : {difference:10.2f}")
    print(f"Percent : {percent:10.2f} %")
    print(f"Status  : {status:>10}")
    print("=" * 34)


# COUNT RECORDS OVER LIMIT
over_limit_count = 0
label = input("Enter a label (or quit to stop): ")

# LOOP TO CHECK MULTIPLE RECORDS
while label!="quit":

    # STEP 2: INPUT


    if label == "quit":
        break

    value = float(input("Enter number of rows loaded: "))
    limit = float(input("Enter number of rows expected: "))

    # STEP 3: PROCESS
    difference, percent = check(value, limit)
    status = status_of(percent)

    if status == "OVER LIMIT":
        over_limit_count += 1

    # STEP 4: OUTPUT
    print_report(label, value, limit, difference, percent, status)
    print(f"Number of records OVER LIMIT: {over_limit_count}")

    label = input("Enter a label (or quit to stop): ")


# ==========================================================================
# 5. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and note the error (do not fix it yet)
#    [ ] Check every function does one job - if a function both calculates
#        and prints, split it
