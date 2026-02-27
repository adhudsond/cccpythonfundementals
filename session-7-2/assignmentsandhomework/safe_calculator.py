# safe_calculator.py
# Calculator with error handling

def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Error: Division by zero")
        return None
    except TypeError:
        print("Error: Invalid types for division")
        return None


# Test cases
print(safe_divide(10, 2))    # 5.0
print(safe_divide(10, 0))    # Error message, None
print(safe_divide(10, "a"))  # Error message, None