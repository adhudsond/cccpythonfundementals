# grade_matrix.py
# Grade Matrix Analyzer (Nested Loops)

grades = [
    [95, 87, 92, 88],
    [88, 90, 85, 92],
    [92, 88, 94, 90],
    [78, 85, 80, 88]
]

num_students = len(grades)
num_subjects = len(grades[0])

# 1) Average for each student (row)
print("=" * 50)
print("GRADE MATRIX REPORT")
print("=" * 50)

print("\n1) Student Averages (by row)")
student_averages = []

for r in range(num_students):
    row_total = 0
    for c in range(num_subjects):
        row_total += grades[r][c]
    row_avg = row_total / num_subjects
    student_averages.append(row_avg)
    print(f"Student {r + 1}: Average = {row_avg:.2f}")

# 2) Average for each subject (column)
print("\n2) Subject Averages (by column)")
subject_averages = []

for c in range(num_subjects):
    col_total = 0
    for r in range(num_students):
        col_total += grades[r][c]
    col_avg = col_total / num_students
    subject_averages.append(col_avg)
    print(f"Subject {c + 1}: Average = {col_avg:.2f}")

# 3) Overall class average + 4) Highest grade + 5) Total A's (>= 90)
total_points = 0
count_scores = 0
highest_grade = grades[0][0]
a_count = 0

for r in range(num_students):
    for c in range(num_subjects):
        score = grades[r][c]
        total_points += score
        count_scores += 1

        if score > highest_grade:
            highest_grade = score

        if score >= 90:
            a_count += 1

overall_avg = total_points / count_scores

print("\n3) Overall Class Average")
print(f"Overall average: {overall_avg:.2f}")

print("\n4) Highest Grade in Entire Matrix")
print(f"Highest grade: {highest_grade}")

print("\n5) Total A's (>= 90)")
print(f"Total A grades: {a_count}")

print("=" * 50)
