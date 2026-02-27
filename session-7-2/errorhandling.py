# Code that crashes
number = int('abc') # ValueError!
# Program stops here!
print('This never runs')
# Error message:
# ValueError: invalid literal for int() with base 10: 'abc'
# Traceback (most recent call last):
# File ...
# User sees scary error
# Program terminates
# Bad experience!
# We need to handle this!