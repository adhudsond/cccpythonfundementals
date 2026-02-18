# Process only passing grades
grades = [95, 45, 87, 62, 55, 92, 78, 88]
for grade in grades:
    if grade >= 60:
        print(f'{grade} - PASS')
else:
    print(f'{grade} - FAIL')
# Output:
# 95 - PASS
# 45 - FAIL
# 87 - PASS
# 62 - PASS
# 55 - FAIL
# 92 - PASS
# 78 - PASS
# 88 - PASS