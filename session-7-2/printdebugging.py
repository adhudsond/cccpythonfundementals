# Function with bug
def calculate_average(numbers):
    print(f'DEBUG: Input = {numbers}') # Debug
    total = sum(numbers)
    print(f'DEBUG: Total = {total}') # Debug
    count = len(numbers)
    print(f'DEBUG: Count = {count}') # Debug
    average = total / count
    print(f'DEBUG: Average = {average}') # Debug
    return average
# Run and see all intermediate values
result = calculate_average([10, 20, 30])
# See where things go wrong!
# Remove debug prints when fixed