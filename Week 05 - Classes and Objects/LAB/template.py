"""
RECORD CHECK  -  my version
===========================

Name  :sufyan ahamudally
Lane  :  IT      (delete two)
Date  : 29/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ====================================================================== CLASS
# 1. Define a class called Record.
#
 
class Record:
    """A record of a single item with a label and two numbers."""
    def __init__(self, label, value, limit):
        """Create a new record with the given label and numbers."""
        self.label = label
        self.value = value
        self.limit = limit

    def status(self):
        """Return this record's status based on its value and limit."""
        if self.value >= self.limit:
            return "OVER LIMIT"
        elif self.value >= self.limit * 0.9:
            return "WARNING"
        else:
            return "OK"

records = [
    Record("R-001", 87.0, 100.0),
    Record("R-002", 120.0, 100.0),
    Record("R-003", 95.0, 100.0),
]
for record in records:
    status = record.status()

    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {record.label}")
    print("=" * 34)
    print(f" value: {record.value}")
    print(f" limit: {record.limit}")
    print(f" status: {status}")
    print("=" * 34)
# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it and check every record's numbers by hand
#    [ ] Check every method only reads/changes its OWN object (self) -
#        nothing reaches outside itself
#    [ ] Check every method and __init__ has a one-line docstring
