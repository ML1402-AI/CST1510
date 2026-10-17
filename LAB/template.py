"""
RECORD CHECK  -  my version
===========================

Name  : Maliha
Lane  :  AI   (delete two)
Date  : 16th october 2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
def check_record(value, limit):
    """Calculate difference, percent and status of a record."""
    difference = value - limit
    percent =(difference / limit) * 100

    if value > limit:
        status = "OVER LIMIT"
    else:
        status = "OK"
    return difference, percent, status


def print_report(label, value, limit, difference, percent, status):
    """Prints the report for a record."""
    print(f" {label:<10} {value:<10} {limit:<10} {difference:<10} {percent:>10.1f}% {status:<10}")

def load_records(path):
        """Load records from a file and returns a list of dictionaries."""
        records = []
        try:
            with open(path, "r") as f:
                for line in f:
                    line = line.strip()
                    label, value, limit = line.split(",")
                    records.append({
                        "label": label,
                        "value": float(value),
                        "limit": float(limit)
                    })
        except FileNotFoundError:
            print(f"Error: The file '{path}' was not found.")
        return records



records = load_records("records_sample.txt")

over_limit_count = 0

with open("report.txt", "w") as f:
    for record in records:
        difference, percent, status = check_record(record["value"], record["limit"])
        print_report(record["label"], record["value"], record["limit"], difference, percent, status)

        # Write to the report file
        f.write(f"{record['label']}, {status}\n")

        if status == "OVER LIMIT":
            over_limit_count += 1

print("over limit count: ", over_limit_count)
