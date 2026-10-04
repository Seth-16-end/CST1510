"""
RECORD CHECK  -  my version
===========================

Name  :sufyan
Lane  :IT      
Date  :04/10/2026

Run it:   python template.py
"""

# ==================================================================== INPUT
over_limit_count = 0
while True:
    label = input("Hostname (or quit to finish): ")

    if label.lower() == "quit":
        break

    value = float(input("GB used:  "))  
    limit = float(input("GB total:  "))

# ================================================================== PROCESS
difference = limit - value
percent = (value / limit) * 100

if percent >= 100:
    status = "OVER LIMIT"
    over_limit_count += 1
elif percent >= 90:
    status = "WARNING"
else:
    status = "OK"

# =================================================================== OUTPUT
print()
print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)
print(f"used : {value:>10.2f}")
print(f"Total: {limit:>10.2f}")
print(f"free : {difference:>10.2f}")
print(f"Percent: {percent:>9.2f} %")
print(f"Status: {status:>10}")
print("=" * 34)

print()
print(f"records OVER LIMIT: {over_limit_count}")


