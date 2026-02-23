# Function that returns value
def add(a, b):
    result = a + b
    return result
# Call and store result
sum1 = add(5, 3)
print(sum1) # 8
sum2 = add(10, 20)
print(sum2) # 30
# Use returned value in calculation
total = add(5, 3) + add(10, 2)
print(total) # 8 + 12 = 20
# Return lets you use the result!
# Without return: just prints, can't reuse
