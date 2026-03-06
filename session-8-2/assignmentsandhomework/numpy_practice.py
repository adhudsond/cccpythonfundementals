import numpy as np

# 1. Create array
arr = np.array([1, 2, 3, 4, 5])
print("Original array:", arr)

# 2. Multiply by 10
print("Array * 10:", arr * 10)

# 3. Calculate mean, sum, max, min
print("Mean:", np.mean(arr))
print("Sum:", np.sum(arr))
print("Max:", np.max(arr))
print("Min:", np.min(arr))

# 4. Create 2D array (3x3 matrix)
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
print("\n3x3 Matrix:")
print(matrix)

# 5. Access specific elements
print("Element at row 1, col 1:", matrix[1, 1])
print("Element at row 0, col 2:", matrix[0, 2])

# 6. Calculate row and column sums
print("Row sums:", np.sum(matrix, axis=1))
print("Column sums:", np.sum(matrix, axis=0))

# Compare to Python lists
py_list = [1, 2, 3, 4, 5]
list_times_10 = [x * 10 for x in py_list]
print("\nPython list * 10 using loop/comprehension:", list_times_10)

list_mean = sum(py_list) / len(py_list)
print("Python list mean:", list_mean)
print("Python list sum:", sum(py_list))
print("Python list max:", max(py_list))
print("Python list min:", min(py_list))

print("\nComparison:")
print("NumPy is cleaner for array math and matrix operations.")
print("NumPy is usually faster for large data because it is optimized in C.")