# math_library.py
# Project: Math & Stats Library
# - Factorial
# - Fibonacci sequence
# - Prime number checker
# - Mean, median, mode
# - Standard deviation
# - Includes docstrings and tests

def factorial(n):
    """
    Calculate n! (factorial of n).

    Args:
        n (int): Non-negative integer.

    Returns:
        int: Factorial of n.

    Raises:
        ValueError: If n is negative or not an integer.
    """
    if not isinstance(n, int):
        raise ValueError("factorial() requires an integer.")
    if n < 0:
        raise ValueError("factorial() is not defined for negative numbers.")

    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def fibonacci_sequence(n):
    """
    Generate the first n Fibonacci numbers.

    Fibonacci starts: 0, 1, 1, 2, 3, 5, ...

    Args:
        n (int): Number of terms to generate (n >= 0).

    Returns:
        list: List of the first n Fibonacci numbers.

    Raises:
        ValueError: If n is negative or not an integer.
    """
    if not isinstance(n, int):
        raise ValueError("fibonacci_sequence() requires an integer.")
    if n < 0:
        raise ValueError("fibonacci_sequence() requires n >= 0.")

    if n == 0:
        return []
    if n == 1:
        return [0]

    fib = [0, 1]
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])
    return fib


def is_prime(n):
    """
    Check whether a number is prime.

    Args:
        n (int): Integer to test.

    Returns:
        bool: True if prime, False otherwise.
    """
    if not isinstance(n, int):
        return False
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


def mean(numbers):
    """
    Calculate the mean (average) of a list of numbers.

    Args:
        numbers (list): List of numeric values.

    Returns:
        float: Mean of the numbers.

    Raises:
        ValueError: If list is empty.
    """
    if len(numbers) == 0:
        raise ValueError("mean() requires a non-empty list.")
    return sum(numbers) / len(numbers)


def median(numbers):
    """
    Calculate the median of a list of numbers.

    Args:
        numbers (list): List of numeric values.

    Returns:
        float: Median value.

    Raises:
        ValueError: If list is empty.
    """
    if len(numbers) == 0:
        raise ValueError("median() requires a non-empty list.")

    sorted_nums = sorted(numbers)
    n = len(sorted_nums)
    mid = n // 2

    if n % 2 == 1:
        return sorted_nums[mid]
    return (sorted_nums[mid - 1] + sorted_nums[mid]) / 2


def mode(numbers):
    """
    Calculate the mode(s) of a list of numbers.

    Args:
        numbers (list): List of numeric values.

    Returns:
        list: List of most frequent value(s). Can return multiple modes.

    Raises:
        ValueError: If list is empty.
    """
    if len(numbers) == 0:
        raise ValueError("mode() requires a non-empty list.")

    counts = {}
    for num in numbers:
        counts[num] = counts.get(num, 0) + 1

    max_count = max(counts.values())
    modes = []

    for num, count in counts.items():
        if count == max_count:
            modes.append(num)

    return sorted(modes)


def standard_deviation(numbers):
    """
    Calculate the population standard deviation of a list of numbers.

    Formula:
        sqrt(sum((x - mean)^2) / N)

    Args:
        numbers (list): List of numeric values.

    Returns:
        float: Population standard deviation.

    Raises:
        ValueError: If list is empty.
    """
    if len(numbers) == 0:
        raise ValueError("standard_deviation() requires a non-empty list.")

    avg = mean(numbers)
    variance_sum = 0

    for x in numbers:
        variance_sum += (x - avg) ** 2

    variance = variance_sum / len(numbers)
    return variance ** 0.5


# -----------------------------
# Test each function
# -----------------------------
if __name__ == "__main__":
    print("=" * 60)
    print("MATH & STATS LIBRARY TESTS")
    print("=" * 60)

    # Factorial tests
    print("\nFactorial Tests")
    print(f"factorial(0) = {factorial(0)}")
    print(f"factorial(5) = {factorial(5)}")
    print(f"factorial(7) = {factorial(7)}")

    # Fibonacci tests
    print("\nFibonacci Tests")
    print(f"fibonacci_sequence(0) = {fibonacci_sequence(0)}")
    print(f"fibonacci_sequence(1) = {fibonacci_sequence(1)}")
    print(f"fibonacci_sequence(10) = {fibonacci_sequence(10)}")

    # Prime checker tests
    print("\nPrime Checker Tests")
    test_primes = [1, 2, 3, 4, 17, 18, 19, 20]
    for n in test_primes:
        print(f"is_prime({n}) = {is_prime(n)}")

    # Stats tests
    print("\nStatistics Tests")
    data = [4, 7, 7, 9, 10, 12, 12]
    print(f"Data = {data}")
    print(f"Mean = {mean(data):.2f}")
    print(f"Median = {median(data)}")
    print(f"Mode = {mode(data)}")
    print(f"Standard Deviation = {standard_deviation(data):.4f}")

    # Multi-mode test
    print("\nMode (Multi-mode) Test")
    data2 = [1, 1, 2, 2, 3, 4]
    print(f"Data = {data2}")
    print(f"Mode = {mode(data2)}")

    print("\n" + "=" * 60)
    print("All tests complete ✅")
    print("=" * 60)