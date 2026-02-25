# data_tools.py
# Project: Data Processing Library (utilities + docstrings + tests)

from typing import Any, Callable, Dict, List


def clean_data(*args: Any, remove_none: bool = True, numeric_only: bool = True) -> List[float]:
    """
    Clean mixed data using flexible *args input.

    This function accepts either:
      - multiple values: clean_data(10, None, "bad", 25)
      - a single list/tuple: clean_data([10, None, "bad", 25])

    Cleaning options:
      - remove_none: remove None values
      - numeric_only: keep only int/float values

    Args:
        *args: Values or a single list/tuple of values.
        remove_none (bool): If True, drop None values.
        numeric_only (bool): If True, keep only numeric values (int/float).

    Returns:
        list[float]: Cleaned numeric list (values kept as floats where possible).
    """
    # Support passing a single list/tuple
    if len(args) == 1 and isinstance(args[0], (list, tuple)):
        values = list(args[0])
    else:
        values = list(args)

    cleaned = []
    for x in values:
        if remove_none and x is None:
            continue
        if numeric_only and not isinstance(x, (int, float)):
            continue
        # Cast numeric to float for consistency
        cleaned.append(float(x))
    return cleaned


def transform_data(data: List[Any], transform_fn: Callable[[Any], Any]) -> List[Any]:
    """
    Transform data using functional programming (map + a function/lambda).

    Args:
        data (list): Input list.
        transform_fn (callable): Function/lambda applied to each element.

    Returns:
        list: Transformed list.
    """
    return list(map(transform_fn, data))


def filter_data(data: List[Any], filter_fn: Callable[[Any], bool]) -> List[Any]:
    """
    Filter data using functional programming (filter + a function/lambda).

    Args:
        data (list): Input list.
        filter_fn (callable): Function/lambda that returns True to keep an item.

    Returns:
        list: Filtered list.
    """
    return list(filter(filter_fn, data))


def calculate_statistics(data: List[float]) -> Dict[str, float]:
    """
    Calculate basic statistics for numeric data.

    Statistics included:
      - count
      - sum
      - mean
      - median
      - min
      - max
      - std (population standard deviation)

    Args:
        data (list[float]): Numeric list.

    Returns:
        dict: Statistics dictionary. If data is empty, values are 0 or None where appropriate.
    """
    if not data:
        return {
            "count": 0,
            "sum": 0,
            "mean": 0,
            "median": 0,
            "min": None,
            "max": None,
            "std": 0
        }

    count = len(data)
    total = sum(data)
    mean_val = total / count

    sorted_data = sorted(data)
    mid = count // 2
    if count % 2 == 1:
        median_val = sorted_data[mid]
    else:
        median_val = (sorted_data[mid - 1] + sorted_data[mid]) / 2

    min_val = min(data)
    max_val = max(data)

    variance_sum = 0
    for x in data:
        variance_sum += (x - mean_val) ** 2
    variance = variance_sum / count
    std_val = variance ** 0.5

    return {
        "count": count,
        "sum": total,
        "mean": mean_val,
        "median": median_val,
        "min": min_val,
        "max": max_val,
        "std": std_val
    }


# -----------------------------
# Tests with real-like data
# -----------------------------
if __name__ == "__main__":
    raw_data = [10, -5, "invalid", 25, None, 30, -2, 100, 15, 0, 42.5]

    print("=" * 72)
    print("DATA TOOLS TEST RUN")
    print("=" * 72)
    print(f"Raw data: {raw_data}")

    # 1) Clean: remove None + non-numeric
    cleaned = clean_data(raw_data)
    print(f"\nCleaned (numeric only, no None): {cleaned}")

    # 2) Filter: keep only values in range 0..50
    filtered = filter_data(cleaned, lambda x: 0 <= x <= 50)
    print(f"Filtered (0 to 50): {filtered}")

    # 3) Transform: square values
    squared = transform_data(filtered, lambda x: x ** 2)
    print(f"Transformed (squared): {squared}")

    # 4) Transform: normalize 0..1
    if filtered:
        mn = min(filtered)
        mx = max(filtered)
        rng = mx - mn
        normalized = transform_data(filtered, lambda x: 0 if rng == 0 else (x - mn) / rng)
    else:
        normalized = []
    normalized_rounded = transform_data(normalized, lambda x: round(x, 2))
    print(f"Normalized (0-1, rounded): {normalized_rounded}")

    # 5) Stats
    stats = calculate_statistics(filtered)
    print("\n--- Statistics (Filtered Data) ---")
    print(f"Count:  {stats['count']}")
    print(f"Sum:    {stats['sum']:.2f}")
    print(f"Mean:   {stats['mean']:.2f}")
    print(f"Median: {stats['median']:.2f}")
    print(f"Min:    {stats['min']}")
    print(f"Max:    {stats['max']}")
    print(f"Std:    {stats['std']:.2f}")

    print("=" * 72)