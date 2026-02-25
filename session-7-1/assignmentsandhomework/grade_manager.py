# grade_manager.py
# Complete grade management system using CSV DictWriter/DictReader

import csv

# 1) Sample data
students = [
    {"name": "Alice", "math": 95, "english": 92},
    {"name": "Bob", "math": 87, "english": 90}
]

input_file = "students_grades.csv"
output_file = "students_grades_with_avg.csv"

# 2) Save to CSV (DictWriter)
fieldnames = ["name", "math", "english"]

with open(input_file, "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(students)

# 3) Read back from CSV (DictReader)
loaded_students = []
with open(input_file, "r", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        # Convert numeric fields from strings to ints
        row["math"] = int(row["math"])
        row["english"] = int(row["english"])
        loaded_students.append(row)

# 4) Calculate average for each student
for s in loaded_students:
    s["average"] = (s["math"] + s["english"]) / 2

# 5) Write results to new CSV: name, math, english, average
output_fields = ["name", "math", "english", "average"]

with open(output_file, "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=output_fields)
    writer.writeheader()
    for s in loaded_students:
        writer.writerow({
            "name": s["name"],
            "math": s["math"],
            "english": s["english"],
            "average": f"{s['average']:.2f}"
        })

# 6) Print summary report
class_avg_total = 0
top_student = None

for s in loaded_students:
    class_avg_total += s["average"]
    if top_student is None or s["average"] > top_student["average"]:
        top_student = s

class_avg = class_avg_total / len(loaded_students) if loaded_students else 0

print("=" * 68)
print("GRADE MANAGER SUMMARY REPORT")
print("=" * 68)
print(f"Input CSV:   {input_file}")
print(f"Output CSV:  {output_file}")
print("-" * 68)

print(f"{'Name':<10} {'Math':>6} {'English':>8} {'Average':>10}")
print("-" * 68)
for s in loaded_students:
    print(f"{s['name']:<10} {s['math']:>6} {s['english']:>8} {s['average']:>10.2f}")

print("-" * 68)
print(f"Class average: {class_avg:.2f}")

if top_student:
    print(f"Top student:   {top_student['name']} ({top_student['average']:.2f})")

print("=" * 68)