# table_processor.py
# Project: Data Table Processor (5x5 matrix + random + nested loops)

import random

ROWS = 5
COLS = 5

# 1) Create 5×5 matrix (nested lists) and fill with random numbers 1-100
matrix = []
for r in range(ROWS):
    row = []
    for c in range(COLS):
        row.append(random.randint(1, 100))
    matrix.append(row)

print("=" * 55)
print("DATA TABLE PROCESSOR REPORT (5×5)")
print("=" * 55)

# Display the matrix nicely
print("\nMatrix:")
for r in range(ROWS):
    for c in range(COLS):
        print(f"{matrix[r][c]:>4}", end="")
    print()

# 2) Calculate row averages
print("\nRow Averages:")
row_averages = []
for r in range(ROWS):
    row_total = 0
    for c in range(COLS):
        row_total += matrix[r][c]
    row_avg = row_total / COLS
    row_averages.append(row_avg)
    print(f"Row {r + 1}: {row_avg:.2f}")

# 3) Calculate column averages
print("\nColumn Averages:")
col_averages = []
for c in range(COLS):
    col_total = 0
    for r in range(ROWS):
        col_total += matrix[r][c]
    col_avg = col_total / ROWS
    col_averages.append(col_avg)
    print(f"Col {c + 1}: {col_avg:.2f}")

# 4) Find max value and its position
max_val = matrix[0][0]
max_row = 0
max_col = 0

for r in range(ROWS):
    for c in range(COLS):
        if matrix[r][c] > max_val:
            max_val = matrix[r][c]
            max_row = r
            max_col = c

print("\nMaximum Value:")
print(f"Max = {max_val} at position (row={max_row + 1}, col={max_col + 1})")

print("=" * 55)
