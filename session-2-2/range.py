# First 10 squares
squares = [i**2 for i in range(10)]
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# Even numbers 0 to 20
evens = [i for i in range(21) if i % 2 == 0]
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
# Multiples of 5 up to 50
mult_5 = [i for i in range(0, 51, 5)]
# [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
# Generate test data instantly!
test_data = [i * 0.1 for i in range(100)]
# [0.0, 0.1, 0.2, ..., 9.9]