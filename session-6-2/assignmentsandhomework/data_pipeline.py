# data_pipeline.py
# Data processing pipeline: map/filter/lambda + comparison loop version

data = [10, -5, 'invalid', 25, None, 30, -2, 100, 15]

# -----------------------------
# Functional pipeline version
# -----------------------------
# 1) Filter out non-numeric
numeric = list(filter(lambda x: isinstance(x, (int, float)), data))

# 2) Filter out negative numbers
non_negative = list(filter(lambda x: x >= 0, numeric))

# 3) Filter out outliers (> 50)
filtered = list(filter(lambda x: x <= 50, non_negative))

# 4) Normalize to 0-1 range
if len(filtered) == 0:
    normalized = []
else:
    min_val = min(filtered)
    max_val = max(filtered)
    range_val = max_val - min_val

    if range_val == 0:
        normalized = [0 for _ in filtered]
    else:
        normalized = list(map(lambda x: (x - min_val) / range_val, filtered))

# 5) Round to 2 decimals
final_fp = list(map(lambda x: round(x, 2), normalized))


# -----------------------------
# Loop version (same result)
# -----------------------------
clean = []
for x in data:
    if isinstance(x, (int, float)) and x >= 0 and x <= 50:
        clean.append(x)

if len(clean) == 0:
    final_loop = []
else:
    min_val2 = clean[0]
    max_val2 = clean[0]
    for x in clean:
        if x < min_val2:
            min_val2 = x
        if x > max_val2:
            max_val2 = x

    range_val2 = max_val2 - min_val2
    final_loop = []

    for x in clean:
        if range_val2 == 0:
            norm = 0
        else:
            norm = (x - min_val2) / range_val2
        final_loop.append(round(norm, 2))


# -----------------------------
# Report
# -----------------------------
print("=" * 70)
print("DATA PIPELINE REPORT")
print("=" * 70)
print(f"Raw data:              {data}")
print(f"Numeric only:          {numeric}")
print(f"Non-negative:          {non_negative}")
print(f"Outliers removed (<=50): {filtered}")
print("-" * 70)
print(f"Final (functional):    {final_fp}")
print(f"Final (loop):          {final_loop}")
print("=" * 70)