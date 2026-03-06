# statistics_utils.py
# Your first reusable statistics module!

def calculate_mean(numbers):
    """
    Calculate the mean (average) of a list of numbers.

    Args:
        numbers (list): Non-empty list of numeric values.

    Returns:
        float: Mean value.

    Raises:
        ValueError: If numbers is empty.
    """
    if not numbers:
        raise ValueError("calculate_mean() requires a non-empty list.")
    return sum(numbers) / len(numbers)


def calculate_median(numbers):
    """
    Calculate the median of a list of numbers.

    Args:
        numbers (list): Non-empty list of numeric values.

    Returns:
        float: Median value.

    Raises:
        ValueError: If numbers is empty.
    """
    if not numbers:
        raise ValueError("calculate_median() requires a non-empty list.")

    s = sorted(numbers)
    n = len(s)
    mid = n // 2

    if n % 2 == 1:
        return s[mid]
    return (s[mid - 1] + s[mid]) / 2


def calculate_mode(numbers):
    """
    Calculate the mode(s) of a list of numbers.

    Returns a list because there can be multiple modes.

    Args:
        numbers (list): Non-empty list of numeric values.

    Returns:
        list: Sorted list of most frequent value(s).

    Raises:
        ValueError: If numbers is empty.
    """
    if not numbers:
        raise ValueError("calculate_mode() requires a non-empty list.")

    counts = {}
    for x in numbers:
        counts[x] = counts.get(x, 0) + 1

    max_count = max(counts.values())
    modes = [x for x, c in counts.items() if c == max_count]
    return sorted(modes)


def calculate_std_dev(numbers):
    """
    Calculate the population standard deviation of a list of numbers.

    Formula:
        sqrt(sum((x - mean)^2) / N)

    Args:
        numbers (list): Non-empty list of numeric values.

    Returns:
        float: Population standard deviation.

    Raises:
        ValueError: If numbers is empty.
    """
    if not numbers:
        raise ValueError("calculate_std_dev() requires a non-empty list.")

    mean_val = calculate_mean(numbers)
    variance = sum((x - mean_val) ** 2 for x in numbers) / len(numbers)
    return variance ** 0.5


if __name__ == "__main__":
    # Test each function
    test_data = [85, 92, 78, 95, 88, 76, 92]

    print("=" * 60)
    print("STATISTICS_UTILS TESTS")
    print("=" * 60)
    print(f"Data: {test_data}")
    print(f"Mean:   {calculate_mean(test_data):.2f}")
    print(f"Median: {calculate_median(test_data):.2f}")
    print(f"Mode:   {calculate_mode(test_data)}")
    print(f"StdDev: {calculate_std_dev(test_data):.4f}")
    print("=" * 60)