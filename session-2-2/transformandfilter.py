# Square only the even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
even_squares = [n**2 for n in numbers if n % 2 == 0]
print(even_squares) # [4, 16, 36, 64]
# Uppercase only long names
names = ['Jo', 'Alice', 'Bob', 'Carol']
upper_long = [n.upper() for n in names if len(n) > 3]
print(upper_long) # ['ALICE', 'CAROL']
# Double only numbers above 50
scores = [45, 67, 52, 38, 91, 73]
doubled_high = [s*2 for s in scores if s > 50]
print(doubled_high) # [134, 104, 182, 146]
# This is data science magic!