# Process scores with validation
def calculate_average(scores):
    # Validate input
    if scores is None:
        return None, 'Error: No scores provided'
    if len(scores) == 0:
        return None, 'Error: Empty score list'
    # Filter out invalid scores
    valid_scores = [s for s in scores if 0 <= s <= 100]
    if len(valid_scores) == 0:
        return None, 'Error: No valid scores'
    # Calculate (we know data is good!)
    avg = sum(valid_scores) / len(valid_scores)
    return avg, 'Success'
# Test
result, msg = calculate_average([95, 87, 92])
print(f'{msg}: {result}') # Success: 91.33