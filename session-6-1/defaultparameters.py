# Function with default parameter
def greet(name, greeting='Hello'):
    print(f'{greeting}, {name}!')
# Call different ways
greet('Alice')
# Hello, Alice! (uses default)
greet('Bob', 'Hi')
# Hi, Bob! (overrides default)
greet('Carol', 'Good morning')
# Good morning, Carol!
# Default makes parameter optional!
# Flexible function calls