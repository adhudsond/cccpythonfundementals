# grade_manager.py
# A simple grade book using lists (Session 2.1 - Lists Fundamentals)

# 1) Create empty list
grades = []

# 2) Add these grades: 95, 87, 92, 78, 88
grades.append(95)
grades.append(87)
grades.append(92)
grades.append(78)
grades.append(88)

# 3) Calculate and print stats
num_grades = len(grades)
highest = max(grades)
lowest = min(grades)
average = sum(grades) / num_grades

print("----- Grade Book Summary -----")
print(f"Number of grades: {num_grades}")
print(f"Highest grade:    {highest}")
print(f"Lowest grade:     {lowest}")
print(f"Average grade:    {average:.2f}")

# 4) Sort grades from high to low
grades.sort(reverse=True)

# 5) Print final sorted list
print("------------------------------")
print(f"Sorted grades (high → low): {grades}")
