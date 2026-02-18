temperatures = [72, 68, 75, 70, 73]
# Change first temperature
temperatures[0] = 74
print(temperatures) # [74, 68, 75, 70, 73]
# Change last temperature
temperatures[-1] = 71
print(temperatures) # [74, 68, 75, 70, 71]
# Change multiple items with slicing
temperatures[1:3] = [69, 76]
print(temperatures) # [74, 69, 76, 70, 71]
# This is data correction!
# Fix errors in your dataset