# Analyze test scores
scores = [95, 87, 78, 92, 88, 76, 94, 85, 90, 82]
# Count different grade levels
a_count = 0
b_count = 0
c_count = 0
for score in scores:
    if score >= 90:
        a_count += 1
    elif score >= 80:
        b_count += 1
    elif score >= 70:
        c_count += 1
print(f'A grades: {a_count}') # 4
print(f'B grades: {b_count}') # 5
print(f'C grades: {c_count}') # 1
# Real grade distribution analysis!