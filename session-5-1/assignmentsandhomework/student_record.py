# student_record.py

# Create a student dictionary (database-like record)
student = {
    "name": "Alice Johnson",
    "student_id": "S123456",
    "age": 20,
    "major": "Computer Science",
    "gpa": 3.5,
    "courses": ["Python 101", "Intro to ML", "Data Structures"]
}

# 1) Print each field with label
print("----- STUDENT RECORD (ORIGINAL) -----")
print(f"Name:        {student['name']}")
print(f"Student ID:  {student['student_id']}")
print(f"Age:         {student['age']}")
print(f"Major:       {student['major']}")
print(f"GPA:         {student['gpa']}")
print(f"Courses:     {student['courses']}")

# 2) Update GPA to 3.8
student["gpa"] = 3.8

# 3) Add new field: graduation_year
student["graduation_year"] = 2027

# 4) Add a new course to courses list
student["courses"].append("Databases")

# 5) Print the complete updated record
print("\n----- STUDENT RECORD (UPDATED) -----")
for key, value in student.items():
    print(f"{key}: {value}")
