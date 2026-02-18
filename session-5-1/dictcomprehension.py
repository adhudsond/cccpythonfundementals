# Create dict of squares
squares = {x: x**2 for x in range(1, 6)}
print(squares)
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
# Double all values
prices = {'apple': 1.50, 'banana': 0.75}
doubled = {k: v*2 for k, v in prices.items()}
print(doubled)
# {'apple': 3.0, 'banana': 1.5}
# Filter high grades only
grades = {'math': 85, 'english': 92, 'science': 78}
high = {k: v for k, v in grades.items() if v >= 80}
print(high)
# {'math': 85, 'english': 92}
# Compact and powerful!