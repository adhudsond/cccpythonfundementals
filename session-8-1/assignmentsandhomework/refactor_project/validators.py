# validators.py
# Validation functions (from earlier weeks: safe input, email validation, data validation)

def is_number(x):
    """Return True if x is int or float (not bool), else False."""
    return isinstance(x, (int, float)) and not isinstance(x, bool)


def in_range(x, low, high):
    """Return True if x is numeric and low <= x <= high."""
    return is_number(x) and low <= x <= high


def validate_age(age):
    """
    Validate age for 0-120.

    Returns:
        (bool, str): (is_valid, message)
    """
    if not is_number(age) or age != int(age):
        return False, "Age must be a whole number."
    age = int(age)
    if age < 0 or age > 120:
        return False, "Invalid age (must be 0-120)."
    return True, "Valid age."


def validate_score(score):
    """
    Validate score for 0-100.

    Returns:
        (bool, str): (is_valid, message)
    """
    if not is_number(score):
        return False, "Score must be a number."
    if score < 0 or score > 100:
        return False, "Invalid score (must be 0-100)."
    return True, "Valid score."


def clean_numeric_list(data, low=None, high=None):
    """
    Clean mixed data:
    - removes None
    - keeps only numeric (int/float)
    - optionally filters by range [low, high]

    Returns:
        (clean_list, removed_count)
    """
    clean = []
    removed = 0

    for x in data:
        if x is None:
            removed += 1
            continue
        if not is_number(x):
            removed += 1
            continue
        if low is not None and x < low:
            removed += 1
            continue
        if high is not None and x > high:
            removed += 1
            continue
        clean.append(float(x))

    return clean, removed


def validate_email(email):
    """
    Simple email validation:
    - strip spaces
    - lowercase
    - must contain '@' and '.'

    Returns:
        (cleaned_email, is_valid)
    """
    cleaned = str(email).strip().lower()
    is_valid = ("@" in cleaned) and ("." in cleaned)
    return cleaned, is_valid