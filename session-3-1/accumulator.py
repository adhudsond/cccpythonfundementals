# Build list of squares (accumulator pattern)
squares = [] # 1. Initialize empty list to store results
for i in range(10): # 2. Loop through data (from 0 to 9)
    squares.append(i ** 2) # 3. Square i and add to list
print(squares)
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# Same as comprehension:
# squares = [i**2 for i in range(10)]
# But accumulator pattern works for
# more complex logic!
# You'll use this CONSTANTLY!