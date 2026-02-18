# Task: Double each number
numbers = [1, 2, 3, 4, 5]
# OLD WAY: 5 lines with loop
doubled = []
for num in numbers:
    doubled.append(num * 2)
print(doubled) # [2, 4, 6, 8, 10]
# NEW WAY: 1 line with comprehension
doubled = [num * 2 for num in numbers]
print(doubled) # [2, 4, 6, 8, 10]
# SAME RESULT!
# Which would you rather write?