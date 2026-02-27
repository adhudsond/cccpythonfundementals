# safe_input.py
# Robust integer input with try/except

def get_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Invalid! Enter a number.")


# Test
age = get_integer("Age: ")
print(f"You entered age: {age}")