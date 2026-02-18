# grade_processor.py
# Real Gradebook Analysis (loops + conditionals + counting)

scores = [95, 45, 87, 62, 55, 92, 78, 88, 73, 51, 94, 68]

# 1) Categorize into passing / failing
passing = []
failing = []

for s in scores:
    if s >= 60:
        passing.append(s)
    else:
        failing.append(s)

# 2) Convert each to letter grade (A/B/C/D/F)
def to_letter(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

letter_grades = []
for s in scores:
    letter_grades.append(to_letter(s))

# 3) Count each letter grade
counts = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
for lg in letter_grades:
    counts[lg] += 1

# 4) Find highest and lowest passing scores (handle edge case: no passing scores)
if len(passing) > 0:
    highest_passing = passing[0]
    lowest_passing = passing[0]
    for s in passing:
        if s > highest_passing:
            highest_passing = s
        if s < lowest_passing:
            lowest_passing = s
else:
    highest_passing = None
    lowest_passing = None

# 5) Calculate pass rate (percentage)
pass_rate = (len(passing) / len(scores)) * 100

# Print detailed report
print("=" * 60)
print("GRADE PROCESSOR REPORT")
print("=" * 60)

print(f"All scores:      {scores}")
print(f"Passing (>=60):  {passing}")
print(f"Failing (<60):   {failing}")

print("\n--- Letter Grades ---")
print(f"Letters: {letter_grades}")

print("\n--- Letter Grade Counts ---")
print(f"A: {counts['A']}")
print(f"B: {counts['B']}")
print(f"C: {counts['C']}")
print(f"D: {counts['D']}")
print(f"F: {counts['F']}")

print("\n--- Passing Score Stats ---")
if highest_passing is not None:
    print(f"Highest passing score: {highest_passing}")
    print(f"Lowest passing score:  {lowest_passing}")
else:
    print("No passing scores to analyze.")

print("\n--- Pass Rate ---")
print(f"Pass rate: {pass_rate:.2f}% ({len(passing)} out of {len(scores)})")

print("=" * 60)
