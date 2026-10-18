"""
RECORD CHECK  -  my version
===========================

Name  : sufyan
Lane  :  IT     
Date  : 10/18/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS


def check_record(value, limit):
    """Calculate the difference, percentage amd status for one record"""
    difference = value - limit
    percent = (value / limit) * 100

    if percent >= 100:
        status = "OVER LIMIT"
    elif percent >= 90:
        status ="WARNING"
    else:
        status = "OK"
    return difference, percent, status

def print_report(label, value, limit, difference, percent, status):
    """PRint one formatted record."""
    print()
    print("=" * 34)
    print(f" RECORD CHECK - {label}")
    print("=" * 34)
    print(f"used : {value:>10.2f} GB")
    print(f"total : {limit:>10.2f} GB")
    print(f"Difference : {difference:>+10.2f} GB")
    print(f"of total: {percent:>9.1f} %")
    print(f"status : {status:>10}")
    print("=" * 34)

records = [
    {"label":"srv-01", "value": 87.0, "limit": 120.0},
    {"label": "srv-02", "value": 118.0, "limit": 120.0},
    {"label": "srv-03", "value": 125.0, "limit": 120.0},
    ]
for record in records:
    difference, percent, status = check_record(
       record["value"],
       record["limit"],
    )
    print_report(
       record["label"],
       record["value"],
       record["limit"],
       difference,
       percent,
       status,

    )

