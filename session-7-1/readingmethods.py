# Method 1: read() - whole file
with open('sample.txt', 'r') as file:
    content = file.read()
    print(type(content)) # str
# Method 2: readlines() - list of lines
with open('sample.txt', 'r') as file:
    lines = file.readlines()
    print(type(lines)) # list
    print(lines[0]) # First line
# Method 3: Loop (BEST for large files)
with open('sample.txt', 'r') as file:
    for line in file:
        print(line.strip()) # Remove \n
# Loop doesn't load entire file into memory!
# Efficient for huge files