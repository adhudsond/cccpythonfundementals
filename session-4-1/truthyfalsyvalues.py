# Check if list has items
data = [1, 2, 3]
# Long way
if len(data) > 0:
    print('Has data')
# Short way (Pythonic!)
if data:
    print('Has data')
# Empty list is falsy
empty = []
if not empty:
    print('List is empty') # Runs!
# Check if string exists
name = 'Alice'
if name:
    print(f'Hello, {name}')
# Professional Python style!