# student_database.py
# Project: Student Database (nested dicts + dict methods + reporting)

students = {
    "S001": {"name": "Alice", "grades": [95, 87, 92, 88], "attendance": 92},
    "S002": {"name": "Bob",   "grades": [88, 90, 85, 92], "attendance": 78},
    "S003": {"name": "Carol", "grades": [92, 88, 94, 90], "attendance": 96},
    "S004": {"name": "David", "grades": [78, 85, 80, 88], "attendance": 67},
    "S005": {"name": "Eve",   "grades": [55, 61, 58, 60], "attendance": 85},
}

def avg(nums):
    return sum(nums) / len(nums) if nums else 0

# Calculate average for each student + track highest performer + count passing
highest_id = None
highest_avg = None
passing_count = 0

# Store computed averages inside each student record (database-style enrichment)
for student_id, record in students.items():
    grades = record.get("grades", [])
    record["average"] = avg(grades)

    # Highest performer
    if highest_avg is None or record["average"] > highest_avg:
        highest_avg = record["average"]
        highest_id = student_id

    # Count students passing (>= 60 average)
    if record["average"] >= 60:
        passing_count += 1

# Overall class average (all scores)
all_scores = []
for record in students.values():
    for g in record.get("grades", []):
        all_scores.append(g)

class_avg = avg(all_scores)

# Generate report
print("=" * 76)
print("STUDENT DATABASE REPORT")
print("=" * 76)

print(f"Total students:        {len(students)}")
print(f"Students passing (>=60): {passing_count}")
print(f"Class average (all scores): {class_avg:.2f}")
print("-" * 76)

print(f"{'ID':<6} {'Name':<10} {'Avg':>7} {'Att%':>7} {'Grades':>30}")
print("-" * 76)

for student_id, record in students.items():
    name = record.get("name", "UNKNOWN")
    attendance = record.get("attendance", "N/A")
    average = record.get("average", 0)
    grades = record.get("grades", [])
    print(f"{student_id:<6} {name:<10} {average:>7.2f} {attendance:>7} {str(grades):>30}")

print("-" * 76)

# Highest performer details (safe access)
top_student = students.get(highest_id, {})
top_name = top_student.get("name", "UNKNOWN")
print(f"Highest performer: {top_name} ({highest_id}) with average {highest_avg:.2f}")

print("=" * 76)
