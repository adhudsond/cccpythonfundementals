# File: math_utils.py
def add(a, b):
    return a + b
def multiply(a, b):
    return a * b
def calculate_average(numbers):
    return sum(numbers) / len(numbers)
PI = 3.14159
# That's it! This is a module
# Save as math_utils.py
# Now any file can import and use these functions!

# File: math_utils.py
def add(a, b):
    return a + b
def multiply(a, b):
    return a * b
# Test code (only runs when executed directly)
if __name__ == '__main__':
    print('Testing math_utils...')
    print(f'5 + 3 = {add(5, 3)}')
    print(f'4 * 5 = {multiply(4, 5)}')
    print('Tests passed!')
# Run directly: python math_utils.py → runs tests
# Import: from math_utils import add → tests don't run
# Perfect for module testing!