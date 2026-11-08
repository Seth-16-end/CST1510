"""
RECORD CHECK  -  my version
===========================

Name  :sufyan ahamudally
Lane  :  IT      (delete two)
Date  : 09/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
from pathlib import Path
def parse_line(raw_line):
    """Clean one messy IT record and retun its fields as a dictionary."""
    line = raw_line.strip() 
    hostname_part, rest = line.split(",", 1)
    hostname = hostname_part.strip().lower()
    fields ={}
    for piece in rest.split(","):
        key, value = piece.split("=")
        fields[key.strip().lower()] = float(value.strip())

    return{
        "hostname": hostname,
        "used": fields["used"],
        "total": fields["total"],
    }

def status_of(used, total):
    percent = (used / total) * 100
    if percent >= 100:
        return "OVER LIMIT"
    if percent >= 90:
        return "WARNING"
    else:
        return "OK"


records = []
flagged = 0
data_file = Path(__file__).with_name("messy_lines.txt")
with open(data_file) as file:
    for raw_line in file:
        if raw_line.strip():
         record = parse_line(raw_line)
         status = status_of(record["used"], record["total"])
         records.append(record)
         print(record,status)
         if status != "OK":
             flagged += 1

print(f"\nRecords: {len(records)} | Flagged: {flagged}")
    


# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it against at least 5 genuinely messy raw records
#    [ ] Run it with a value that will not convert to a number - write the
#        error down
#    [ ] Check every function does one job, with a docstring
