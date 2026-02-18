# Square each number (perfect!)
nums = [1, 2, 3, 4, 5]
squares = [n**2 for n in nums]
print(squares) # [1, 4, 9, 16, 25]
# Make all uppercase (spot on!)
names = ['alice', 'bob', 'carol']
upper = [name.upper() for name in names]
print(upper) # ['ALICE', 'BOB', 'CAROL']
# Capitalize first letter (great use of .capitalize()!)
names = ['alice', 'bob', 'carol', 'carlos']
capitalized_names = [name.capitalize() for name in names]
print(capitalized_names) # ['Alice', 'Bob', 'Carol’, ‘Carlos’]
# Get string lengths (correct now!)
lengths = [len(name) for name in names]
print(lengths) # [5, 3, 5, 6]
words = ['hi', 'hello', 'hey', 'goodbye']
lengths = [len(word) for word in words]
print(lengths) # [2, 5, 3, 7]