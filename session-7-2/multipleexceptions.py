# Risky calculation
try:
    num1 = int(input('First number: '))
    num2 = int(input('Second number: '))
    result = num1 / num2
    print(f'Result: {result}')
except ValueError:
    print('Error: Please enter valid numbers')
except ZeroDivisionError:
    print('Error: Cannot divide by zero')
except Exception as e:
    print(f'Unexpected error: {e}')
# Each error type handled differently!
# Last except catches anything else