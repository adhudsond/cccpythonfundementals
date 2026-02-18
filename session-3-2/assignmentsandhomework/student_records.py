# student_records.py
# Project: Student Record System (Full CRUD + JSON persistence + statistics)

import json

DB_FILE = "student_records.json"


# -----------------------------
# Helpers: load/save
# -----------------------------
def load_db(filename):
    try:
        with open(filename, "r") as f:
            db = json.load(f)
            # Ensure basic structure
            if not isinstance(db, dict) or "students" not in db or not isinstance(db["students"], dict):
                return {"students": {}}
            return db
    except FileNotFoundError:
        return {"students": {}}
    except json.JSONDecodeError:
        print("⚠️  Warning: JSON file is corrupted. Starting with an empty database.")
        return {"students": {}}


def save_db(filename, db):
    with open(filename, "w") as f:
        json.dump(db, f, indent=2)


def is_number(x):
    return isinstance(x, (int, float))


def average(nums):
    return sum(nums) / len(nums) if nums else 0


def safe_int_input(prompt):
    while True:
        s = input(prompt).strip()
        if s.lstrip("-").isdigit():
            return int(s)
        print("Please enter a whole number.")


def safe_float_input(prompt):
    while True:
        s = input(prompt).strip()
        try:
            return float(s)
        except ValueError:
            print("Please enter a number (like 87 or 87.5).")


# -----------------------------
# CRUD operations
# -----------------------------
def create_student(db):
    student_id = input("Enter new student ID (example S006): ").strip()
    if not student_id:
        print("Student ID cannot be empty.")
        return

    if student_id in db["students"]:
        print(f"Student ID '{student_id}' already exists.")
        return

    name = input("Enter student name: ").strip()
    attendance = safe_float_input("Enter attendance % (0-100): ")
    if attendance < 0 or attendance > 100:
        print("Invalid attendance. Must be 0-100.")
        return

    grades = []
    print("Enter grades one by one (0-100). Type 'done' to finish.")
    while True:
        g = input("Grade (or 'done'): ").strip().lower()
        if g == "done":
            break
        try:
            val = float(g)
        except ValueError:
            print("Invalid grade. Enter a number or 'done'.")
            continue
        if val < 0 or val > 100:
            print("Grade must be between 0 and 100.")
            continue
        grades.append(val)

    db["students"][student_id] = {
        "name": name if name else "UNKNOWN",
        "attendance": attendance,
        "grades": grades
    }

    print(f"✅ Added student {student_id} ({db['students'][student_id]['name']}).")


def read_student(db):
    student_id = input("Enter student ID to view: ").strip()
    record = db["students"].get(student_id)

    if not record:
        print("Student not found.")
        return

    avg = average(record.get("grades", []))
    print("\n" + "=" * 60)
    print("STUDENT RECORD")
    print("=" * 60)
    print(f"ID:         {student_id}")
    print(f"Name:       {record.get('name', 'UNKNOWN')}")
    print(f"Attendance: {record.get('attendance', 'N/A')}%")
    print(f"Grades:     {record.get('grades', [])}")
    print(f"Average:    {avg:.2f}")
    print("=" * 60)


def update_student(db):
    student_id = input("Enter student ID to update: ").strip()
    record = db["students"].get(student_id)

    if not record:
        print("Student not found.")
        return

    print("\nUpdate Options:")
    print("1) Update name")
    print("2) Update attendance")
    print("3) Add a new grade")
    print("4) Replace ALL grades")
    choice = input("Choose (1-4): ").strip()

    if choice == "1":
        new_name = input("Enter new name: ").strip()
        if new_name:
            record["name"] = new_name
            print("✅ Name updated.")
        else:
            print("Name not changed (empty input).")

    elif choice == "2":
        new_att = safe_float_input("Enter new attendance % (0-100): ")
        if 0 <= new_att <= 100:
            record["attendance"] = new_att
            print("✅ Attendance updated.")
        else:
            print("Invalid attendance. Must be 0-100.")

    elif choice == "3":
        new_grade = safe_float_input("Enter new grade (0-100): ")
        if 0 <= new_grade <= 100:
            record.setdefault("grades", []).append(new_grade)
            print("✅ Grade added.")
        else:
            print("Invalid grade. Must be 0-100.")

    elif choice == "4":
        new_grades = []
        print("Enter grades one by one (0-100). Type 'done' to finish.")
        while True:
            g = input("Grade (or 'done'): ").strip().lower()
            if g == "done":
                break
            try:
                val = float(g)
            except ValueError:
                print("Invalid grade. Enter a number or 'done'.")
                continue
            if val < 0 or val > 100:
                print("Grade must be between 0 and 100.")
                continue
            new_grades.append(val)

        record["grades"] = new_grades
        print("✅ Grades replaced.")

    else:
        print("Invalid choice.")


def delete_student(db):
    student_id = input("Enter student ID to delete: ").strip()
    removed = db["students"].pop(student_id, None)

    if removed:
        print(f"✅ Deleted student {student_id} ({removed.get('name', 'UNKNOWN')}).")
    else:
        print("Student not found.")


# -----------------------------
# Filtering + statistics
# -----------------------------
def list_students(db):
    students = db["students"]
    if not students:
        print("No students in the database.")
        return

    print("\n" + "=" * 72)
    print("STUDENT LIST")
    print("=" * 72)
    print(f"{'ID':<8} {'Name':<14} {'Avg':>7} {'Att%':>7} {'Grades':>30}")
    print("-" * 72)

    for sid, rec in students.items():
        grades = rec.get("grades", [])
        avg = average(grades)
        att = rec.get("attendance", "N/A")
        name = rec.get("name", "UNKNOWN")
        att_display = f"{att:.0f}" if is_number(att) else "N/A"
        print(f"{sid:<8} {name:<14} {avg:>7.2f} {att_display:>7} {str(grades):>30}")

    print("=" * 72)


def report_stats(db):
    students = db["students"]
    if not students:
        print("No data to analyze.")
        return

    # Compute per-student averages
    student_avgs = []
    passing_count = 0
    top_id = None
    top_avg = None

    all_grades = []
    total_a_grades = 0

    for sid, rec in students.items():
        grades = rec.get("grades", [])
        avg = average(grades)
        student_avgs.append(avg)

        # Passing based on average >= 60
        if avg >= 60:
            passing_count += 1

        # Top performer
        if top_avg is None or avg > top_avg:
            top_avg = avg
            top_id = sid

        # Class grade pool + A count
        for g in grades:
            all_grades.append(g)
            if g >= 90:
                total_a_grades += 1

    class_avg = average(all_grades)
    overall_pass_rate = (passing_count / len(students)) * 100

    top_name = students.get(top_id, {}).get("name", "UNKNOWN")

    print("\n" + "=" * 72)
    print("DATABASE STATISTICS REPORT")
    print("=" * 72)
    print(f"Total students:           {len(students)}")
    print(f"Students passing (>=60):  {passing_count} ({overall_pass_rate:.2f}%)")
    print(f"Class average (all grades): {class_avg:.2f}" if all_grades else "Class average:            N/A")
    print(f"Total A grades (>=90):    {total_a_grades}")
    print("-" * 72)
    if top_avg is not None:
        print(f"Top performer:            {top_name} ({top_id}) with avg {top_avg:.2f}")
    else:
        print("Top performer:            N/A")
    print("=" * 72)


def filter_categories(db):
    """
    Example categories:
    - Honors: avg >= 90 AND attendance >= 90
    - Probation: avg < 70 OR attendance < 75
    """
    students = db["students"]
    if not students:
        print("No students to filter.")
        return

    honors = []
    probation = []
    regular = []

    for sid, rec in students.items():
        grades = rec.get("grades", [])
        att = rec.get("attendance")
        avg = average(grades)

        # Only categorize if attendance exists and numeric
        if not is_number(att):
            regular.append((sid, rec, avg))
            continue

        if avg >= 90 and att >= 90:
            honors.append((sid, rec, avg))
        elif avg < 70 or att < 75:
            probation.append((sid, rec, avg))
        else:
            regular.append((sid, rec, avg))

    def print_group(title, group):
        print(f"\n--- {title} ---")
        if not group:
            print("None")
            return
        print(f"{'ID':<8} {'Name':<14} {'Avg':>7} {'Att%':>7}")
        print("-" * 44)
        for sid, rec, avg in group:
            name = rec.get("name", "UNKNOWN")
            att = rec.get("attendance", "N/A")
            att_display = f"{att:.0f}" if is_number(att) else "N/A"
            print(f"{sid:<8} {name:<14} {avg:>7.2f} {att_display:>7}")

    print_group("HONORS (avg >= 90 AND attendance >= 90%)", honors)
    print_group("PROBATION (avg < 70 OR attendance < 75%)", probation)
    print_group("REGULAR", regular)


# -----------------------------
# Main program (menu)
# -----------------------------
def main():
    db = load_db(DB_FILE)

    # If empty, seed with a few records so it runs immediately
    if not db["students"]:
        db["students"] = {
            "S001": {"name": "Alice", "grades": [95, 87, 92, 88], "attendance": 92},
            "S002": {"name": "Bob",   "grades": [45, 62, 55, 68], "attendance": 78},
            "S003": {"name": "Carol", "grades": [92, 88, 94, 90], "attendance": 96}
        }
        save_db(DB_FILE, db)

    while True:
        print("\n" + "=" * 60)
        print("STUDENT RECORD SYSTEM (CRUD + JSON)")
        print("=" * 60)
        print("1) List all students")
        print("2) View a student record")
        print("3) Add a new student (CREATE)")
        print("4) Update a student (UPDATE)")
        print("5) Delete a student (DELETE)")
        print("6) Statistics report")
        print("7) Filter categories (honors/probation)")
        print("8) Save changes")
        print("9) Exit")
        choice = input("Choose (1-9): ").strip()

        if choice == "1":
            list_students(db)
        elif choice == "2":
            read_student(db)
        elif choice == "3":
            create_student(db)
        elif choice == "4":
            update_student(db)
        elif choice == "5":
            delete_student(db)
        elif choice == "6":
            report_stats(db)
        elif choice == "7":
            filter_categories(db)
        elif choice == "8":
            save_db(DB_FILE, db)
            print(f"✅ Saved to {DB_FILE}")
        elif choice == "9":
            save_db(DB_FILE, db)
            print(f"✅ Saved to {DB_FILE}")
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1-9.")


if __name__ == "__main__":
    main()
