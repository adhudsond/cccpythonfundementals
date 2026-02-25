# Function accepts any number of arguments
def add_all(*args):
    print(f'Received: {args}') # Tuple
    return sum(args)
# Call with different amounts
print(add_all(1, 2))
# Received: (1, 2)
# 3
print(add_all(1, 2, 3, 4, 5))
# Received: (1, 2, 3, 4, 5)
# 15
print(add_all(10, 20, 30, 40, 50, 60))
# Received: (10, 20, 30, 40, 50, 60)
# 210
# One function, any number of args!