# calculators.py
# Calculation functions (from earlier weeks: averages, stats, grade logic)

def average(numbers):
    """Return average of a non-empty list of numbers. Returns 0 if empty."""
    return sum(numbers) / len(numbers) if numbers else 0


def minimum(numbers):
    """Return min of list or None if empty."""
    return min(numbers) if numbers else None


def maximum(numbers):
    """Return max of list or None if empty."""
    return max(numbers) if numbers else None


def median(numbers):
    """Return median or 0 if empty."""
    if not numbers:
        return 0
    s = sorted(numbers)
    n = len(s)
    mid = n // 2
    return s[mid] if n % 2 == 1 else (s[mid - 1] + s[mid]) / 2


def std_dev(numbers):
    """Population standard deviation. Returns 0 if empty."""
    if not numbers:
        return 0
    m = average(numbers)
    var = sum((x - m) ** 2 for x in numbers) / len(numbers)
    return var ** 0.5


def score_to_letter(score):
    """Convert numeric score to letter grade A/B/C/D/F."""
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


def count_as(scores):
    """Count how many scores are A's (>= 90)."""
    count = 0
    for s in scores:
        if s >= 90:
            count += 1
    return count