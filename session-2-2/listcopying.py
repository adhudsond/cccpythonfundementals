# WRONG! (This is a trap!)
original = [1, 2, 3]
reference = original # Not a copy!
reference.append(4)
print(original) # [1, 2, 3, 4] - CHANGED!
print(reference) # [1, 2, 3, 4]
# RIGHT! Make actual copy
original = [1, 2, 3]
copy = original.copy() # Real copy
copy.append(4)
print(original) # [1, 2, 3] - Unchanged!
print(copy) # [1, 2, 3, 4]
# Other ways to copy:
# copy = list(original)
# copy = original[:]
# All three create real copies!