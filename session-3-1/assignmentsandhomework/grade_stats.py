# grade_stats.py
# Grade Statistics using loops (accumulators + counting)

grades = [95, 87, 78, 92, 88, 76, 94, 85, 90, 82]

# 1) Total of all grades (accumulator)
total = 0
for g in grades:
    total += g

# 2) Average grade
average = total / len(grades)

# 3) Number of grades >= 90 (A's)
a_count = 0
for g in grades:
    if g >= 90:
        a_count += 1

# 4) Number of grades < 70 (failing)
failing_count = 0
for g in grades:
    if g < 70:
        failing_count += 1

# 5) Highest grade (loop version)
highest = grades[0]
for g in grades:
    if g > highest:
        highest = g

# 6) Lowest grade (loop version)
lowest = grades[0]
for g in grades:
    if g < lowest:
        lowest = g

print("=" * 40)
print("GRADE STATS REPORT")
print("=" * 40)
print(f"Grades:           {grades}")
print(f"Total points:     {total}")
print(f"Average grade:    {average:.2f}")
print(f"A's (>= 90):      {a_count}")
print(f"Failing (< 70):   {failing_count}")
print(f"Highest grade:    {highest}")
print(f"Lowest grade:     {lowest}")
print("=" * 40)
