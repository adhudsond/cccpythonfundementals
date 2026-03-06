import numpy as np

# Create array from list
arr = np.array([1, 2, 3, 4, 5])
print(arr)    # [1 2 3 4 5]

# Mathematical operations (vectorized!)
print(arr * 2)      # [2 4 6 8 10]
print(arr + 10)     # [11 12 13 14 15]
print(arr ** 2)     # [1 4 9 16 25]

# Works on ALL elements at once!
# Much faster than loops
# 2D array (matrix)

matrix = np.array([[1, 2, 3], [4, 5, 6]])
print(matrix)
# [[1 2 3]
#  [4 5 6]]