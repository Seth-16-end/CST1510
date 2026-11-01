"""
RECORD CHECK  -  my version
===========================

Name  :sufyan ahamudally
Lane  :   IT      (delete two)
Date  :11/22026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

import pandas as pd
from pathlib import Path

# ==================================================================== LOAD
# load the storage records
df = pd.read_csv(Path(__file__).with_name("storage_records.csv")) 

#calculate the percent of storage used
df["percent"] = (df["used_gb"] / df["total_gb"]) * 100

#assign a status to each server
df["status"] = df["percent"].apply(lambda p: "OVERLIMIT" if p >= 100
                                   else "WARNING" if p >= 90
                                   else "OK")

print(df)


print("\nServers that need attention:")
print(df[df["status"] != "OK"])


# ==========================================================================
# 4. Before you finish:
#    [ ] Run it and check the percent/status columns by hand for one row
#    [ ] Check you used & (not "and") if you combined more than one condition
#    [ ] Check every column your code refers to actually exists - watch case
