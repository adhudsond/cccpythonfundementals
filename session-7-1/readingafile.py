# Create sample file first (you'd normally have this)
# with open('sample.txt', 'w') as f:
# f.write('Hello from a file!\nLine 2\nLine 3')
# Read the file
file = open('sample.txt', 'r')
content = file.read()
file.close()
print(content)
# Hello from a file!
# Line 2
# Line 3
# Problem: Must remember to close!
# If error occurs, file stays open!
# Better way: use 'with' statement