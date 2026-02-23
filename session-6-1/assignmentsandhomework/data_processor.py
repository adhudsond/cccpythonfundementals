# data_processor.py
# Professional data science functions (cleaning, normalization, stats, outlier filtering)

def clean_data(data):
    """
    Remove None values from a list and return a cleaned list.

    Args:
        data (list): List that may contain None values.

    Returns:
        list: New list with None values removed.
    """
    clean_list = []
    for x in data:
        if x is not None:
            clean_list.append(x)
    return clean_list


def normalize_data(data):
    """
    Normalize numeric data to a 0-1 range using:
    (x - min) / (max - min)

    Args:
        data (list): List of numeric values.

    Returns:
        list: Normalized values between 0 and 1.
              If all values are the same, returns a list of 0s.
    """
    if not data:
        return []

    min_val = min(data)
    max_val = max(data)
    range_val = max_val - min_val

    if range_val == 0:
        return [0 for _ in data]

    normalized = []
    for x in data:
        normalized.append((x - min_val) / range_val)
    return normalized


def calculate_statistics(data):
    """
    Calculate summary statistics for numeric data.

    Returns a dictionary with:
    - mean
    - median
    - min
    - max
    - std (population standard deviation)

    Args:
        data (list): List of numeric values.

    Returns:
        dict: Statistics dictionary. If data is empty, values are None.
    """
    if not data:
        return {
            "mean": None,
            "median": None,
            "min": None,
            "max": None,
            "std": None
        }

    # Mean
    mean_val = sum(data) / len(data)

    # Median
    sorted_data = sorted(data)
    n = len(sorted_data)
    mid = n // 2
    if n % 2 == 1:
        median_val = sorted_data[mid]
    else:
        median_val = (sorted_data[mid - 1] + sorted_data[mid]) / 2

    # Min/Max
    min_val = min(data)
    max_val = max(data)

    # Population standard deviation
    variance = 0
    for x in data:
        variance += (x - mean_val) ** 2
    variance = variance / len(data)
    std_val = variance ** 0.5

    return {
        "mean": mean_val,
        "median": median_val,
        "min": min_val,
        "max": max_val,
        "std": std_val
    }


def filter_outliers(data, threshold=2.0):
    """
    Remove outliers that are more than `threshold` standard deviations
    away from the mean.

    Rule:
        Keep x if abs(x - mean) <= threshold * std

    Args:
        data (list): List of numeric values.
        threshold (float): Number of standard deviations to use as cutoff.

    Returns:
        list: Data with outliers removed.
    """
    if not data:
        return []

    stats = calculate_statistics(data)
    mean_val = stats["mean"]
    std_val = stats["std"]

    # If std is 0, all values are identical, so nothing is an outlier
    if std_val == 0:
        return data[:]

    filtered = []
    for x in data:
        if abs(x - mean_val) <= threshold * std_val:
            filtered.append(x)
    return filtered


# -----------------------------
# Test with sample data
# -----------------------------
sample_data = [10, 20, None, 30, 100, 25]

print("=" * 60)
print("DATA PROCESSOR FUNCTION TEST")
print("=" * 60)
print(f"Raw data: {sample_data}")

cleaned = clean_data(sample_data)
print(f"Cleaned data (no None): {cleaned}")

normalized = normalize_data(cleaned)
print(f"Normalized (0-1): {[round(x, 3) for x in normalized]}")

stats_before = calculate_statistics(cleaned)
print("\nStatistics (before outlier filtering):")
print(f"Mean:   {stats_before['mean']:.2f}")
print(f"Median: {stats_before['median']:.2f}")
print(f"Min:    {stats_before['min']}")
print(f"Max:    {stats_before['max']}")
print(f"Std:    {stats_before['std']:.2f}")

filtered = filter_outliers(cleaned, threshold=2.0)
print(f"\nFiltered data (outliers removed): {filtered}")

stats_after = calculate_statistics(filtered)
print("\nStatistics (after outlier filtering):")
print(f"Mean:   {stats_after['mean']:.2f}")
print(f"Median: {stats_after['median']:.2f}")
print(f"Min:    {stats_after['min']}")
print(f"Max:    {stats_after['max']}")
print(f"Std:    {stats_after['std']:.2f}")
print("=" * 60)