# comprehension_practice.py

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 1. List of all numbers squared
squares = [n ** 2 for n in numbers]

# 2. List of only odd numbers
odds = [n for n in numbers if n % 2 != 0]

# 3. List of numbers divisible by 3
div_by_3 = [n for n in numbers if n % 3 == 0]

# 4. List of numbers squared, but only if even
even_squares = [n ** 2 for n in numbers if n % 2 == 0]

# 5. List containing 'even' or 'odd' for each number
even_or_odd = ["even" if n % 2 == 0 else "odd" for n in numbers]

print(f"Squares: {squares}")
print(f"Odds: {odds}")
print(f"Divisible by 3: {div_by_3}")
print(f"Even squares: {even_squares}")
print(f"Even/Odd labels: {even_or_odd}")
