# File: main.py (in same directory as math_utils.py)
# Method 1: Import module
import math_utils
result = math_utils.add(10, 5)
print(result) # 15
avg = math_utils.calculate_average([10, 20, 30])
print(avg) # 20.0
# Method 2: Import specific functions
from math_utils import multiply, PI
result = multiply(4, 5)
print(result) # 20
print(PI) # 3.14159
# Reusing code across files!