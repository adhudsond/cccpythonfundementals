# data_cleaner.py
# Real Data Cleaning: remove sensor errors (-999), non-numeric values, and None

data = [10, -999, 25, 'invalid', 30, None, -999, 15, 40, 0, -999]

clean_data = []
errors_removed = 0

for x in data:
    # 3) Filter out None values
    if x is None:
        errors_removed += 1
        continue

    # 2) Filter out non-numeric values
    if not isinstance(x, (int, float)):
        errors_removed += 1
        continue

    # 1) Filter out -999 sensor errors
    if x == -999:
        errors_removed += 1
        continue

    # 5) Keep valid values
    clean_data.append(x)

# 6) Before/after statistics
raw_count = len(data)
clean_count = len(clean_data)

raw_numeric_count = 0
for x in data:
    if isinstance(x, (int, float)) and x is not None:
        raw_numeric_count += 1

# Basic stats for clean data (avoid errors if empty)
if clean_count > 0:
    total = 0
    min_val = clean_data[0]
    max_val = clean_data[0]

    for v in clean_data:
        total += v
        if v < min_val:
            min_val = v
        if v > max_val:
            max_val = v

    avg = total / clean_count
else:
    total = 0
    min_val = None
    max_val = None
    avg = 0

print("=" * 62)
print("DATA CLEANER REPORT")
print("=" * 62)
print(f"Raw data:        {data}")
print(f"Clean data:      {clean_data}")
print("-" * 62)
print(f"Items (raw):     {raw_count}")
print(f"Items (clean):   {clean_count}")
print(f"Errors removed:  {errors_removed}")
print("-" * 62)
print("Clean Data Statistics:")
print(f"Sum:             {total}")
print(f"Average:         {avg:.2f}" if clean_count > 0 else "Average:         N/A")
print(f"Min:             {min_val}" if clean_count > 0 else "Min:             N/A")
print(f"Max:             {max_val}" if clean_count > 0 else "Max:             N/A")
print("=" * 62)
