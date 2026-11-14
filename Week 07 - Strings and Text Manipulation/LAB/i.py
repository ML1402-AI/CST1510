def parse_line(raw_line):
    """Parse a raw record into a cleaned dictionary."""

    line = raw_line.strip()
    survey_part, rest = line.split(",", 1)

    survey = survey_part.strip().lower()

    fields = {}

    for piece in rest.split(","):
        key, value = piece.split("=")
        fields[key.strip().lower()] = int(value.strip())

    fields["year"] = survey

    return fields


def status_of(rating):
    """Return a warning or OK status based on the rating."""
    if rating >= 7:
        return "FLAGGED"
    elif rating <= 4:
        return "WARNING"
    else:
        return "OK"

filename = "umm.txt"

with open(filename, "r") as f:
    lines = f.readlines()

total_records = 0
flagged_records = 0

for line in lines:
    record = parse_line(line)

    status = status_of(record["rating"])

    print(record, status)

    total_records += 1

    if status == "FLAGGED":
        flagged_records += 1

print("Total records:", total_records)
print("Flagged records:", flagged_records)
