def calculate_average(numbers):
    """
    Calculate the average of a list of numbers. 
    Args:
    numbers: List of numeric values
    Returns:
    Float representing the average 
    Example:
    >>> calculate_average([10, 20, 30])
    20.0
    """
    return sum(numbers) / len(numbers)
# Access docstring
print(calculate_average.__doc__)
# Professional documentation!
# Explains what, how, and examples
