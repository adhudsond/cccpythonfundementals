import os
# Check current directory
print(os.getcwd())
# /home/claude
# List files in directory
print(os.listdir('.'))
# ['file1.txt', 'file2.txt', ...]
# Check if file exists
if os.path.exists('data.txt'):
    print('File found!')
else:
    print('File not found!')
# Join paths (works on any OS!)
filepath = os.path.join('data', 'input', 'file.txt')
# data/input/file.txt (Linux)
# data\input\file.txt (Windows)
# Portable across operating systems!