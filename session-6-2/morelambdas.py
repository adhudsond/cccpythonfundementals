# Simple operations
add = lambda a, b: a + b
print(add(10, 5)) # 15
# String operations
uppercase = lambda s: s.upper()
print(uppercase('hello')) # HELLO
# Multiple arguments
full_name = lambda first, last: f'{first} {last}'
print(full_name('Alice', 'Smith')) # Alice Smith
# Conditional
is_adult = lambda age: age >= 18
print(is_adult(25)) # True
print(is_adult(15)) # False
# Quick and clean!