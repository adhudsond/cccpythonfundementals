# File processing with complete error handling
try:
    file = open('data.txt', 'r')
    content = file.read()
    print('File read successfully')
except FileNotFoundError:
    print('Error: File not found')
    content = None
else:
    # Runs only if no exception
    print(f'Loaded {len(content)} characters')
finally:
    # ALWAYS runs
    try:
        file.close()
        print('File closed')
    except:
        print('No file to close')
    # Proper cleanup guaranteed!