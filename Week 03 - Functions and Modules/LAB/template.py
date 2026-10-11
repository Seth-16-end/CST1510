"""
RECORD CHECK  -  my version
===========================

Name  : sufyan 
Lane  :  IT      (delete two)
Date  : 11/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
# 1. Write a function called status_of(percent) that returns "OVER LIMIT"
def status_of(percent):
    """return a status based on the percentage"""
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return"WARNING"
    else:
        return "OK"

def check(value, limit):
    """"return the free amount and percentage used"""
    difference = limit - value
    percent = (value / limit) * 100
    return difference, percent
def print_report(label, value, limit, difference, percent, status):
    """"Print the record check report"""
    print()
    print("="*34)
    print(f" RECORD CHECK - {label}")
    print("=" *34)
    print(f"used  : {value:>10.2f}")
    print(f"total  :{limit:>10.2f}")
    print(f"free  :{difference:>10.2f}")
    print(f"percent  :{percent:>10.2f} %")
    print(f"status  : {status:>10}")
    print("="*34)


# ================================================================== PROCESS
over_count = 0 
while True:
    label = input("Enter a hostname, or type quit to stop: ")

    if label == "quit":
        break

    value = float(input("Enter GB used: "))
    limit = float(input("Enter total GB: "))

    difference, percent = check(value, limit)
    status = status_of(percent)
# =================================================================== OUTPUT
# 4. Print the report.
    print_report(label, value, limit, difference, percent, status)

    if status == "OVER LIMIT":
       over_count = over_count + 1

print("Records over limit", over_count)


# ==========================================================================
