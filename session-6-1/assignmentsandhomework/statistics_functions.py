# statistics_functions.py
# Real data analysis functions

def calculate_average(numbers):
    """Return the average of a list of numbers."""
    return sum(numbers) / len(numbers)


def find_maximum(numbers):
    """Return the maximum value in a list of numbers."""
    return max(numbers)


def count_above_threshold(numbers, threshold):
    """Count how many numbers are greater than a threshold."""
    count = 0
    for num in numbers:
        if num > threshold:
            count += 1
    return count


# Test data
scores = [85, 92, 78, 95, 88, 76]

# Test functions
print("Scores:", scores)
print("Average:", calculate_average(scores))
print("Maximum:", find_maximum(scores))
print("Above 85:", count_above_threshold(scores, 85))
print("Above 90:", count_above_threshold(scores, 90))