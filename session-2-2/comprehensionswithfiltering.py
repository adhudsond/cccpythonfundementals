# Get only even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = [n for n in numbers if n % 2 == 0]
print(evens) # [2, 4, 6, 8, 10]
# Get only positive numbers
values = [-5, 3, -1, 8, -2, 10, 0]
positive = [v for v in values if v > 0]
print(positive) # [3, 8, 10]
# Get names longer than 4 letters
names = ['Jo', 'Alice', 'Bob', 'Carol', 'Dave']
long_names = [name for name in names if len(name) > 4]
print(long_names) # ['Alice', 'Carol']
# Filter unwanted data!