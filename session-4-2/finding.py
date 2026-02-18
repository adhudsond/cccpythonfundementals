# Find first negative number
data = [10, 25, 30, -5, 15, 40, -2, 35]
found_invalid = None
for i, value in enumerate(data):
    if value < 0:
        found_invalid = (i, value) # Store position & value
    break # Stop searching!
if found_invalid:
    pos, val = found_invalid
    print(f'Invalid value {val} at position {pos}')
# Invalid value -5 at position 3
else:
    print('All data valid')
# Early detection of problems!
# Doesn't waste time checking rest