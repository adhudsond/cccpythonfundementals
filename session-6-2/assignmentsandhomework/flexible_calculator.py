# flexible_calculator.py
# Flexible argument handling with *args

def multiply_all(*args):
    """
    Multiply all numbers provided in *args.

    Returns:
        int/float: Product of all numbers.
        If no args are provided, returns 1.
    """
    if len(args) == 0:
        return 1

    product = 1
    for n in args:
        product *= n
    return product


def calculate_stats(*args):
    """
    Calculate basic statistics from any number of numeric inputs.

    Returns a dict:
        {
          'count': len(args),
          'sum': sum(args),
          'avg': average (0 if count is 0)
        }
    """
    count = len(args)
    total = sum(args) if count > 0 else 0
    avg = (total / count) if count > 0 else 0

    return {"count": count, "sum": total, "avg": avg}


# Tests
print(multiply_all(2, 3, 4))  # 24
print(calculate_stats(10, 20, 30, 40))