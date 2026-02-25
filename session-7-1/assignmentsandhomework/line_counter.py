# line_counter.py
# Log file analysis with safe file handling (with statement)

# Create a test file first
with open("test.txt", "w") as f:
    f.write("Line 1\nLine 2\nLine 3\nLine 4\nLine 5")

# 1) Read the file
with open("test.txt", "r") as f:
    lines = f.readlines()

# 2) Count total lines
total_lines = len(lines)

# 3) Count non-empty lines
non_empty_lines = 0
for line in lines:
    if line.strip() != "":
        non_empty_lines += 1

# 4) Count lines containing 'Line'
contains_line = 0
for line in lines:
    if "Line" in line:
        contains_line += 1

# 5) Print statistics
print("=" * 50)
print("LINE COUNTER REPORT (test.txt)")
print("=" * 50)
print(f"Total lines:        {total_lines}")
print(f"Non-empty lines:    {non_empty_lines}")
print(f"Lines containing 'Line': {contains_line}")
print("-" * 50)
print("File contents:")
for line in lines:
    print(line.rstrip())
print("=" * 50)