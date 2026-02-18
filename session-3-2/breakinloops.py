# Find first number divisible by 7 and 11
for num in range(1, 1000):
    if num % 7 == 0 and num % 11 == 0:
        print(f'Found it: {num}')
    break # Stop searching!
# Output: Found it: 77
# Doesn't check 78-999 (break stopped loop)
# Without break, would check all 999 numbers
# With break: stops when found
# More efficient!
# Use break to exit early when done!