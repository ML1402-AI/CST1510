
def parse_line(raw_line):
    """Parse a raw record into a cleaned dictionary."""
    line = raw_line.strip()
    survey_part,rest = line.split(',',1)
    survey = survey_part.strip().lower()

    fields = {}
    for piece in rest.split(","):
        key, value = piece.split("=")
        fields[key.strip()] = int(value.strip())
    fields["survey year"] = survey

    return fields
def status_of(rating):
    """Return a status based on the rating."""
    if rating >= 7:
        return "FLAGGED"
    elif rating >= 5:
        return "WARNING"
    else:
        return "OK"

filename = "labfile.txt"
with open(filename) as f:
    file = f.readlines()

total_records = 0

flagged_records = 0

for line in file:
    record = parse_line(line)
    status = status_of(record["rating"])

    print(record,status)
    total_records += 1
    if status == "FLAGGED":
        flagged_records += 1
print("The total number of records is",total_records)
print("The number of records flagged is",flagged_records)