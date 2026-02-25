numbers = [1, 2, 3, 4, 5]
# Square each number
squared = list(map(lambda x: x**2, numbers))
print(squared) # [1, 4, 9, 16, 25]
# Convert to strings
strings = list(map(str, numbers))
print(strings) # ['1', '2', '3', '4', '5']
# Multiple lists (zip them)
a = [1, 2, 3]
b = [10, 20, 30]
sums = list(map(lambda x, y: x + y, a, b))
print(sums) # [11, 22, 33]
# Same as: [x**2 for x in numbers]
# But map is functional programming style