# gradebook_advanced.py
# Professional Grade Management System (Nested Lists + Comprehensions)

grades = [
    [95, 87, 92, 88],
    [88, 90, 85, 92],
    [92, 88, 94, 90],
    [78, 85, 80, 88]
]

students = ['Alice', 'Bob', 'Carol', 'David']

# --- Per-student calculations (use comprehensions where possible) ---
student_avgs = [sum(g) / len(g) for g in grades]
student_highs = [max(g) for g in grades]
student_lows = [min(g) for g in grades]
student_a_counts = [sum(1 for score in g if score >= 90) for g in grades]

# --- Class statistics ---
all_scores = [score for row in grades for score in row]  # flatten nested list
class_avg = sum(all_scores) / len(all_scores)
highest_student_avg = max(student_avgs)
lowest_student_avg = min(student_avgs)
total_as = sum(student_a_counts)

# --- Output formatting ---
print("=" * 56)
print("GRADEBOOK REPORT (STUDENTS + CLASS STATISTICS)")
print("=" * 56)

print(f"{'Student':<10} {'Avg':>7} {'High':>7} {'Low':>7} {'A (90+)':>9}")
print("-" * 56)

for name, avg, hi, lo, a_cnt in zip(students, student_avgs, student_highs, student_lows, student_a_counts):
    print(f"{name:<10} {avg:>7.2f} {hi:>7} {lo:>7} {a_cnt:>9}")

print("-" * 56)
print("CLASS SUMMARY")
print(f"Overall class average:   {class_avg:.2f}")
print(f"Highest student average: {highest_student_avg:.2f}")
print(f"Lowest student average:  {lowest_student_avg:.2f}")
print(f"Total A's in class:      {total_as}")
print("=" * 56)
