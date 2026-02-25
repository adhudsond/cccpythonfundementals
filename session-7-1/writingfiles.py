# Write mode - creates new file or overwrites
with open('output.txt', 'w') as file:
    file.write('Hello, World!\n')
    file.write('This is line 2\n')
    file.write('This is line 3\n')
# File now contains 3 lines
# Append mode - adds to end
with open('output.txt', 'a') as file:
    file.write('This is line 4\n')
# File now has 4 lines
# Write doesn't add newlines automatically!
# Must include \n yourself
# Read it back to verify
with open('output.txt', 'r') as file:
    print(file.read())