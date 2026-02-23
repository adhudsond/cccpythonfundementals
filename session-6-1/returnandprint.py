# Function that PRINTS
def add_print(a, b):
    result = a + b
    print(result) # Shows but doesn't return
# Function that RETURNS
def add_return(a, b):
    result = a + b
    return result # Sends back value
# Try to use them:
x = add_print(5, 3)
# Prints: 8
print(x) # None (nothing returned!)
y = add_return(5, 3)
# Nothing printed
print(y) # 8 (value returned!)
# RETURN to get usable values!
