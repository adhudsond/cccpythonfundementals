# complete_grade_analyzer.py
# Student Grade Analyzer (lists + stats + counting + sorting + f-strings)

# Start with empty list
grades = []

# Add 10 different grades (edit these if you want your own)
grades.append(95)
grades.append(87)
grades.append(92)
grades.append(78)
grades.append(88)
grades.append(100)
grades.append(91)
grades.append(84)
grades.append(73)
grades.append(89)

# Calculate average, min, max
avg_grade = sum(grades) / len(grades)
min_grade = min(grades)
max_grade = max(grades)

# Count grades above 90 (A's)
num_as = sum(1 for g in grades if g >= 90)

# Sort and display all grades (high to low)
sorted_grades = sorted(grades, reverse=True)

print("=" * 42)
print("STUDENT GRADE ANALYZER REPORT")
print("=" * 42)

print(f"Grades entered: {grades}")
print(f"Total grades:   {len(grades)}")

print("\n--- Statistics ---")
print(f"Average grade:  {avg_grade:.2f}")
print(f"Highest grade:  {max_grade}")
print(f"Lowest grade:   {min_grade}")
print(f"A grades (90+): {num_as}")

print("\n--- Sorted Grades (High → Low) ---")
print(f"{sorted_grades}")

print("=" * 42)
