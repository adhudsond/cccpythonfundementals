# gradebook_analyzer.py
# Advanced Gradebook Analysis (nested dictionaries + loops)

gradebook = {
    "Alice": {"math": 95, "eng": 92, "sci": 88},
    "Bob":   {"math": 87, "eng": 90, "sci": 85},
    "Carol": {"math": 92, "eng": 88, "sci": 94}
}

# 1) Average per student + 3) Top student overall + 4) Best subject for each student
student_averages = {}
best_subject_by_student = {}

top_student = None
top_avg = None

for student, subjects in gradebook.items():
    total = 0
    count = 0

    best_subject = None
    best_score = None

    for subject, score in subjects.items():
        total += score
        count += 1

        if best_score is None or score > best_score:
            best_score = score
            best_subject = subject

    avg = total / count if count > 0 else 0
    student_averages[student] = avg
    best_subject_by_student[student] = (best_subject, best_score)

    if top_avg is None or avg > top_avg:
        top_avg = avg
        top_student = student

# 2) Average per subject (across all students)
subject_totals = {}
subject_counts = {}

for student, subjects in gradebook.items():
    for subject, score in subjects.items():
        subject_totals[subject] = subject_totals.get(subject, 0) + score
        subject_counts[subject] = subject_counts.get(subject, 0) + 1

subject_averages = {}
for subject in subject_totals:
    subject_averages[subject] = subject_totals[subject] / subject_counts[subject]

# Report
print("=" * 72)
print("GRADEBOOK ANALYZER REPORT")
print("=" * 72)

print("\n--- Average Per Student ---")
for student, avg in student_averages.items():
    print(f"{student:<10} Average: {avg:.2f}")

print("\n--- Average Per Subject ---")
for subject, avg in subject_averages.items():
    print(f"{subject.upper():<5} Average: {avg:.2f}")

print("\n--- Top Student Overall ---")
print(f"{top_student} with average {top_avg:.2f}")

print("\n--- Best Subject For Each Student ---")
for student, (subj, score) in best_subject_by_student.items():
    print(f"{student:<10} Best: {subj.upper()} ({score})")

print("=" * 72)
