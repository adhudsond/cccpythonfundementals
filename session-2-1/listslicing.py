numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# First 3 items
print(numbers[0:3]) # [0, 1, 2]
print(numbers[:3]) # [0, 1, 2] (shortcut)
# Last 3 items
print(numbers[-3:]) # [7, 8, 9]
# Middle items
print(numbers[3:7]) # [3, 4, 5, 6]
# Every other item
print(numbers[::2]) # [0, 2, 4, 6, 8]
# This is how you split data for ML!
# train = data[:800] # First 80%
# test = data[800:] # Last 20%