# Best practice: use with
with open('sample.txt', 'r') as file:
    content = file.read()
    print(content)
# File automatically closed here!
# Even if exception occurred
# Can still use content after 'with' block
print('\nLength:', len(content))
# This is the STANDARD way
# Use this pattern always!
# with = try-finally behind the scenes
# Guarantees file.close() gets called