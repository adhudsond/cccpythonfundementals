# school_database.py
# Session 5.2 Exercise 1: School Database (Nested Dictionaries)

school = {
    "math_dept": {
        "teachers": ["Dr. Smith", "Prof. Jones"],
        "students": 150,
        "budget": 50000
    },
    "english_dept": {
        "teachers": ["Dr. Brown", "Prof. Taylor"],
        "students": 120,
        "budget": 42000
    }
}

# 1) Add science_dept
school["science_dept"] = {
    "teachers": ["Dr. Lee", "Prof. Patel"],
    "students": 180,
    "budget": 60000
}

# 2) Calculate total students
total_students = 0
for dept_info in school.values():
    total_students += dept_info["students"]

# 3) List all teachers (from all depts)
all_teachers = []
for dept_info in school.values():
    for teacher in dept_info["teachers"]:
        all_teachers.append(teacher)

# 4) Find dept with most students
most_students_dept = None
most_students_count = None

for dept_name, dept_info in school.items():
    if most_students_count is None or dept_info["students"] > most_students_count:
        most_students_count = dept_info["students"]
        most_students_dept = dept_name

# 5) Calculate total budget
total_budget = 0
for dept_info in school.values():
    total_budget += dept_info["budget"]

# Report
print("=" * 70)
print("SCHOOL DATABASE REPORT")
print("=" * 70)

print("\n--- Departments ---")
for dept_name, dept_info in school.items():
    print(f"{dept_name}: students={dept_info['students']}, budget=${dept_info['budget']}, teachers={dept_info['teachers']}")

print("\n--- Totals ---")
print(f"Total students: {total_students}")
print(f"Total budget:   ${total_budget}")

print("\n--- Teachers (All Departments) ---")
for t in all_teachers:
    print(f"- {t}")

print("\n--- Department With Most Students ---")
print(f"{most_students_dept} ({most_students_count} students)")

print("=" * 70)
