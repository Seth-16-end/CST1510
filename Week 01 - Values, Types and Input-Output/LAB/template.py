"""
RECORD CHECK  -  my version
===========================

Name  :sufyan ahamudally
Lane  :IT      
Date  :27/09/2026
"""

# ==================================================================== INPUT
# 1. Ask the user for your three values.
hostname = input("Enter a hostname: ")
gb_used = float(input("Enter GB used: "))
gb_total = float(input("Enter GB total: "))

# ================================================================== PROCESS
# 2. Work out what you were NOT given.       [Typical and above]

gb_free = gb_total - gb_used
percent_used = (gb_used / gb_total) * 100

percent_free =(gb_free / gb_total) * 100


# =================================================================== OUTPUT
# 3. Print the report.
print()
print("=" * 34)
print(f"  RECORD CHECK  -  {hostname}")
print("=" * 34)

# : your report lines go here
print(f"used : {gb_used:>10.2f}")
print(f"Total : {gb_total:>10.2f}")
print(f"Free : {gb_free:>+10.2f}")
print(f" Percent : {percent_used:>10.2f} %")
print(f"Free % : {percent_free:>10.2f} %")

print("=" * 34)


# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and write the error in your journal
#    [ ] Check every variable name says what it holds
#    [ ] Show it to the person next to you
