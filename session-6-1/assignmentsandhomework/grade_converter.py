# grade_converter.py
# Reusable grade logic with functions

def score_to_letter(score):
    """Convert numeric score to letter grade."""
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


def is_passing(score):
    """Return True if score is passing (>= 60), else False."""
    return score >= 60


# Test with different scores
print(score_to_letter(95))  # A
print(score_to_letter(85))  # B
print(score_to_letter(75))  # C

# Test passing function
print(is_passing(95))  # True
print(is_passing(59))  # False
print(is_passing(60))  # True