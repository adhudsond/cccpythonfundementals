# Process only positive numbers
numbers = [5, -3, 8, -1, 12, -7, 15, 0, 20]
for num in numbers:
    if num <= 0:
        continue # Skip non-positive
# This code only runs for positive numbers
squared = num ** 2
print(f'{num} squared = {squared}')
# Output:
# 5 squared = 25
# 8 squared = 64
# 12 squared = 144
# 15 squared = 225
# 20 squared = 400
# Negative numbers skipped!