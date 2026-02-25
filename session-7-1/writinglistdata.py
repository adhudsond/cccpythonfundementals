# Student scores to save
scores = [95, 87, 92, 78, 88, 94]
# Method 1: Loop
with open('scores.txt', 'w') as file:
    for score in scores:
        file.write(f'{score}\n')
# Method 2: writelines with comprehension
with open('scores.txt', 'w') as file:
    lines = [f'{score}\n' for score in scores]
file.writelines(lines)
# Read back and verify
with open('scores.txt', 'r') as file:
    loaded = [int(line.strip()) for line in file]
print(loaded) # [95, 87, 92, 78, 88, 94]
# Saved and loaded successfully!