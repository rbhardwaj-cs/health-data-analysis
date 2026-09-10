import re
import csv

# The record types we actually care about for this project
WANTED_TYPES = {
    "HKQuantityTypeIdentifierStepCount",
    "HKQuantityTypeIdentifierDistanceWalkingRunning",
    "HKQuantityTypeIdentifierActiveEnergyBurned",
    "HKQuantityTypeIdentifierBasalEnergyBurned",
    "HKQuantityTypeIdentifierWalkingSpeed",
    "HKQuantityTypeIdentifierWalkingStepLength",
}

def parse_record(line):
    """
    Given one line of the XML file, return (type, start_date, value)
    if it's a Record line with a type we want, otherwise return None.
    """
    type_match = re.search(r'type="([^"]*)"', line)
    if not type_match:
        return None
    record_type = type_match.group(1)

    # Step 2: is it a type we care about?
    if record_type not in WANTED_TYPES:
        return None

    # Step 3: pull the other two fields the same way
    start_match = re.search(r'startDate="([^"]*)"', line)
    value_match = re.search(r'value="([^"]*)"', line)

    if not start_match or not value_match:
        return None  # malformed line, missing a field — skip rather than crash

    start_date = start_match.group(1)
    value = value_match.group(1)

    return (record_type, start_date, value)
# --- driver code below, don't worry about this part yet ---
with open("export.xml", "r", encoding="utf-8") as infile, \
     open("raw_records.csv", "w", newline="") as outfile:

    writer = csv.writer(outfile)
    writer.writerow(["type", "start_date", "value"])

    count = 0
    for line in infile:
        result = parse_record(line)
        if result:
            writer.writerow(result)
            count += 1

    print(f"Extracted {count} records")