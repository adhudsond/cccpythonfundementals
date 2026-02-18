# Multiplication table
for i in range(1, 4): # Outer: 1, 2, 3
    for j in range(1, 4): # Inner: 1, 2, 3
        print(f'{i} × {j} = {i*j}')
# Output:
# 1 × 1 = 1
# 1 × 2 = 2
# 1 × 3 = 3
# 2 × 1 = 2
# 2 × 2 = 4
# 2 × 3 = 6
# 3 × 1 = 3
# 3 × 2 = 6
# 3 × 3 = 9
# Inner loop runs 3 times for EACH outer

# Multiplication table
for row in range(1, 6): # outer loop: rows 1 to 5
 for col in range(1, 6): # inner loop: columns 1 to 5
    product = row * col
 print(f"{product:3d}", end=" ") # print with spacing
 print() # new line after each row
# Output:
# 1 2 3 4 5
# 2 4 6 8 10
# 3 6 9 12 15
# 4 8 12 16 20
# 5 10 15 20 25
# Output (a nice 5×5 table):

# Right triangle pattern
for i in range(1, 6): # Row number
    for j in range(i): # Stars in this row
        print('*', end='') # end='' prevents newline
        print() # New line after each row
# Output:
# * ← row 1: 1 star
# ** ← row 2: 2 stars
# *** ← row 3: 3 stars
# **** ← row 4: 4 stars
# ***** ← row 5: 5 stars
# Visual patterns:
# Row 1: inner runs 1 time
# Row 2: inner runs 2 times
# Row 3: inner runs 3 times