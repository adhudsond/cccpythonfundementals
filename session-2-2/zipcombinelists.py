# Two parallel lists
names = ['Alice', 'Bob', 'Carol', 'David']
scores = [95, 87, 92, 78]
# Combine with zip()
for name, score in zip(names, scores):
    print(f'{name}: {score}')
# Output:
# Alice: 95
# Bob: 87
# Carol: 92
# David: 78
# Create dictionary from two lists
grade_dict = dict(zip(names, scores))
print(grade_dict)
# {'Alice': 95, 'Bob': 87, 'Carol': 92, 'David': 78