# data_processor.py
# CSV-like processing (manual parsing) using with-statement

# Create CSV-like file
with open("students.csv", "w") as f:
    f.write("Alice,25,85\nBob,30,92\nCarol,28,78")

# 1) Read line by line + 2) Split by comma + 3) Extract fields
students = []
with open("students.csv", "r") as f:
    for line in f:
        line = line.strip()
        if line == "":
            continue

        parts = line.split(",")
        name = parts[0]
        age = int(parts[1])
        score = float(parts[2])

        students.append({"name": name, "age": age, "score": score})

# 4) Calculate average score
total_score = 0
for s in students:
    total_score += s["score"]
avg_score = total_score / len(students) if students else 0

# 5) Find highest scorer
highest = students[0] if students else None
for s in students:
    if highest is None or s["score"] > highest["score"]:
        highest = s

# 6) Print results
print("=" * 60)
print("STUDENT CSV-LIKE DATA PROCESSOR REPORT")
print("=" * 60)

for s in students:
    print(f"Name: {s['name']:<5} | Age: {s['age']:<2} | Score: {s['score']:.0f}")

print("-" * 60)
print(f"Average score: {avg_score:.2f}")

if highest:
    print(f"Highest scorer: {highest['name']} ({highest['score']:.0f})")

print("=" * 60)