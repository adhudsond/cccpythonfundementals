# data_cleaner.py
# Data Cleaning Challenge (-999 = sensor error)

data = [10, -999, 25, 30, -999, 15, 40, -999, 35, 20]

# 1) Remove all -999 values (filter) using a comprehension
clean_data = [x for x in data if x != -999]

# 2) Calculate average of clean data
avg = sum(clean_data) / len(clean_data)

# 3) Find all values above average
above_avg = [x for x in clean_data if x > avg]

# 4) Normalize to 0-1 range: (value - min) / (max - min)
min_val = min(clean_data)
max_val = max(clean_data)
range_val = max_val - min_val

# Protect against division by zero (just in case all values are the same)
normalized = [(x - min_val) / range_val for x in clean_data] if range_val != 0 else [0 for _ in clean_data]

# 5) Print before/after comparison
print("====================================")
print("SENSOR DATA CLEANER REPORT")
print("====================================")
print(f"Raw data:        {data}")
print(f"Clean data:      {clean_data}")
print("------------------------------------")
print(f"Count (raw):     {len(data)}")
print(f"Count (clean):   {len(clean_data)}")
print(f"Average (clean): {avg:.2f}")
print(f"Min (clean):     {min_val}")
print(f"Max (clean):     {max_val}")
print(f"Above average:   {above_avg}")
print("------------------------------------")
print("Normalized (0 to 1):")
print([round(n, 3) for n in normalized])
print("====================================")
