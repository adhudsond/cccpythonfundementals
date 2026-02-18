# Calculate total (accumulator pattern)
numbers = [10, 25, 30, 15, 40]
total = 0 # 1. Initialize accumulator at zero
for num in numbers: # 2. Loop through each number in list
    total += num # 3. Add current number to running total
print(f'Total: {total}') # 120
# Average = total / count
average = total / len(numbers) # Divide total by number of items
print(f'Average: {average}') # 24.0