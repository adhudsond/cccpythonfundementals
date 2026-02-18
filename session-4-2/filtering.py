# Filter scores >= 90
scores = [95, 87, 78, 92, 88, 76, 94, 85, 90, 82]
high_scores = [] # Start empty
for score in scores:
    if score >= 90: # Check condition
        high_scores.append(score) # Add if True
print(high_scores)
# [95, 92, 94, 90]
# Or with list comprehension (same result):
# high_scores = [s for s in scores if s >= 90]
# Both ways are valid!
# Loop version: clearer for complex logic