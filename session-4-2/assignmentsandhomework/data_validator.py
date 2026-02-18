# data_validator.py
# Professional Data Quality Control: validate types + ranges + summary stats

data = [25, 'John', -5, 150, 30, None, 45, 'invalid', 67, 0, 95]

valid_data = []
out_of_range = []
non_numeric = []
null_values = []

# 1-3) Categorize using loops + isinstance + range checks
for x in data:
    # 3) Null values
    if x is None:
        null_values.append(x)
        continue

    # 1) Numeric check
    if not isinstance(x, (int, float)):
        non_numeric.append(x)
        continue

    # 2) Range check (0-100)
    if 0 <= x <= 100:
        valid_data.append(x)
    else:
        out_of_range.append(x)

# 4) Counts
count_total = len(data)
count_valid = len(valid_data)
count_out_of_range = len(out_of_range)
count_non_numeric = len(non_numeric)
count_null = len(null_values)

# 5) Calculations
percent_valid = (count_valid / count_total) * 100 if count_total > 0 else 0
total_errors = count_out_of_range + count_non_numeric + count_null

# Average of valid data (avoid division by zero)
if count_valid > 0:
    valid_sum = 0
    for v in valid_data:
        valid_sum += v
    valid_avg = valid_sum / count_valid
else:
    valid_sum = 0
    valid_avg = 0

# Print report
print("=" * 70)
print("DATA VALIDATION REPORT")
print("=" * 70)

print(f"Raw data: {data}")

print("\n--- Categorized Results ---")
print(f"Valid data (0-100):         {valid_data}")
print(f"Out of range (numeric):     {out_of_range}")
print(f"Non-numeric values:         {non_numeric}")
print(f"Null values:                {null_values}")

print("\n--- Counts ---")
print(f"Total items:                {count_total}")
print(f"Valid:                      {count_valid}")
print(f"Out of range:               {count_out_of_range}")
print(f"Non-numeric:                {count_non_numeric}")
print(f"Nulls:                      {count_null}")

print("\n--- Quality Metrics ---")
print(f"Percent valid:              {percent_valid:.2f}%")
print(f"Average of valid data:      {valid_avg:.2f}" if count_valid > 0 else "Average of valid data:      N/A")
print(f"Total errors:               {total_errors}")

print("=" * 70)
