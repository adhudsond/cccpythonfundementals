# student_manager.py
# Project: Student Management System
# - Store students with grades + attendance
# - Validate data (types, ranges)
# - Filter by criteria (honors, probation)
# - Calculate statistics
# - Generate a clean, categorized report

students = [
    {"name": "Alice", "grades": [95, 87, 92, 88], "attendance": 92},
    {"name": "Bob", "grades": [88, 90, 85, 92], "attendance": 78},
    {"name": "Carol", "grades": [92, 88, 94, 90], "attendance": 96},
    {"name": "David", "grades": [78, 85, 80, 88], "attendance": 67},
    # Messy entries to prove validation works:
    {"name": "Eve", "grades": [105, 90, "bad", 85], "attendance": 101},
    {"name": None, "grades": [], "attendance": 85},
]

# ---------------------------
# Validation helpers
# ---------------------------
def is_number(x):
    return isinstance(x, (int, float))

def validate_student(student):
    """
    Returns a tuple:
      (is_valid, cleaned_student, errors_list)
    cleaned_student keeps only valid grades (0-100) and a valid attendance (0-100) if possible.
    """
    errors = []

    # Validate name
    name = student.get("name")
    if not isinstance(name, str) or not name.strip():
        errors.append("Invalid name (must be non-empty string).")
        name = "UNKNOWN"

    # Validate grades list
    raw_grades = student.get("grades")
    if not isinstance(raw_grades, list):
        errors.append("Grades must be a list.")
        raw_grades = []

    cleaned_grades = []
    for g in raw_grades:
        if not is_number(g):
            errors.append(f"Non-numeric grade removed: {g}")
            continue
        if g < 0 or g > 100:
            errors.append(f"Out-of-range grade removed: {g}")
            continue
        cleaned_grades.append(g)

    if len(cleaned_grades) == 0:
        errors.append("No valid grades available.")

    # Validate attendance
    attendance = student.get("attendance")
    if not is_number(attendance):
        errors.append("Attendance must be numeric (0-100).")
        attendance = None
    elif attendance < 0 or attendance > 100:
        errors.append(f"Attendance out of range (0-100): {attendance}")
        attendance = None

    cleaned = {
        "name": name.strip() if isinstance(name, str) else "UNKNOWN",
        "grades": cleaned_grades,
        "attendance": attendance
    }

    is_valid = (len(errors) == 0)
    return is_valid, cleaned, errors

def average(nums):
    return sum(nums) / len(nums) if nums else 0


# ---------------------------
# Processing + Categorization
# ---------------------------
valid_students = []
invalid_students = []  # keep with reasons
honors = []
probation = []
regular = []

# Criteria (feel free to adjust)
HONORS_AVG = 90
HONORS_ATT = 90
PROBATION_AVG = 70
PROBATION_ATT = 75

for s in students:
    is_valid, cleaned, errors = validate_student(s)

    # Compute student average if possible
    cleaned["avg"] = average(cleaned["grades"])
    cleaned["num_grades"] = len(cleaned["grades"])

    if is_valid:
        valid_students.append(cleaned)
    else:
        invalid_students.append({"student": cleaned, "errors": errors})

    # Categorize (only if we have attendance and at least 1 valid grade)
    if cleaned["attendance"] is not None and cleaned["num_grades"] > 0:
        if cleaned["avg"] >= HONORS_AVG and cleaned["attendance"] >= HONORS_ATT:
            honors.append(cleaned)
        elif cleaned["avg"] < PROBATION_AVG or cleaned["attendance"] < PROBATION_ATT:
            probation.append(cleaned)
        else:
            regular.append(cleaned)

# ---------------------------
# Statistics (valid-only)
# ---------------------------
all_valid_grades = []
attendance_values = []

for s in valid_students:
    for g in s["grades"]:
        all_valid_grades.append(g)
    if s["attendance"] is not None:
        attendance_values.append(s["attendance"])

class_avg = average(all_valid_grades)
avg_attendance = average(attendance_values) if attendance_values else 0

# Highest/lowest student average among students with grades
student_avgs = [s["avg"] for s in valid_students if s["num_grades"] > 0]
highest_student_avg = max(student_avgs) if student_avgs else None
lowest_student_avg = min(student_avgs) if student_avgs else None

# ---------------------------
# Report
# ---------------------------
print("=" * 74)
print("STUDENT MANAGEMENT SYSTEM REPORT")
print("=" * 74)

print("\n--- Summary Counts ---")
print(f"Total records:        {len(students)}")
print(f"Valid records:        {len(valid_students)}")
print(f"Invalid records:      {len(invalid_students)}")
print(f"Honors students:      {len(honors)} (avg >= {HONORS_AVG} AND attendance >= {HONORS_ATT}%)")
print(f"Probation students:   {len(probation)} (avg < {PROBATION_AVG} OR attendance < {PROBATION_ATT}%)")
print(f"Regular students:     {len(regular)}")

print("\n--- Class Statistics (valid-only) ---")
print(f"Class average (all grades):     {class_avg:.2f}" if all_valid_grades else "Class average:                 N/A")
print(f"Average attendance (valid):     {avg_attendance:.2f}%" if attendance_values else "Average attendance:            N/A")
print(f"Highest student average:        {highest_student_avg:.2f}" if highest_student_avg is not None else "Highest student average:       N/A")
print(f"Lowest student average:         {lowest_student_avg:.2f}" if lowest_student_avg is not None else "Lowest student average:        N/A")

def print_group(title, group):
    print(f"\n--- {title} ---")
    if not group:
        print("None")
        return
    print(f"{'Name':<12} {'Avg':>7} {'Att%':>7} {'Grades':>20}")
    print("-" * 74)
    for s in group:
        att_display = f"{s['attendance']:.0f}" if s["attendance"] is not None else "N/A"
        print(f"{s['name']:<12} {s['avg']:>7.2f} {att_display:>7} {str(s['grades']):>20}")

print_group("HONORS", honors)
print_group("PROBATION", probation)
print_group("REGULAR", regular)

print("\n--- Invalid Records (with reasons) ---")
if not invalid_students:
    print("None")
else:
    for item in invalid_students:
        s = item["student"]
        print(f"\nStudent: {s['name']}")
        print(f"Grades kept: {s['grades']}")
        print(f"Attendance: {s['attendance']}")
        print("Issues:")
        for err in item["errors"]:
            print(f" - {err}")

print("\n" + "=" * 74)
print("Tip: Edit the students list and re-run to test more validation cases.")
print("=" * 74)

