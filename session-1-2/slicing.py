text = 'Hello World'
# Get first 5 characters (positions 0-4)
print(text[0:5]) # 'Hello'
# Get from position 6 to end
print(text[6:]) # 'World'
# Get first 5 (shortcut - skip the 0)
print(text[:5]) # 'Hello'
# Get last 5 characters
print(text[-5:]) # 'World'
# This is CRITICAL for data processing!
# You'll use slicing constantly