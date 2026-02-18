# temp_analyzer.py
# Session 4.2 Exercise 1: Temperature Analyzer (loops + conditionals + validation)

temps = [22, -5, 18, 30, 15, -2, 25, 28, 12, 35, -10, 20]

freezing_days = 0          # < 0
cold_days = 0              # 0 - 15
comfortable_days = 0       # 16 - 25
hot_days = 0               # > 25

valid_temps = []           # >= -50 and <= 50

# Loop through temps once and do everything
for t in temps:
    # 5) Validate temp range
    if t >= -50 and t <= 50:
        valid_temps.append(t)

    # 1-4) Categorize days
    if t < 0:
        freezing_days += 1
    elif t <= 15:
        cold_days += 1
    elif t <= 25:
        comfortable_days += 1
    else:
        hot_days += 1

# 6) Average of valid temps only (avoid division by zero)
valid_total = 0
for t in valid_temps:
    valid_total += t

valid_avg = valid_total / len(valid_temps) if len(valid_temps) > 0 else 0

# Print statistics with clear labels
print("=" * 52)
print("TEMPERATURE ANALYZER REPORT (Celsius)")
print("=" * 52)
print(f"Raw temps:            {temps}")
print(f"Valid temps (-50..50): {valid_temps}")
print("-" * 52)
print(f"Freezing days (< 0):        {freezing_days}")
print(f"Cold days (0 to 15):        {cold_days}")
print(f"Comfortable days (16 to 25): {comfortable_days}")
print(f"Hot days (> 25):            {hot_days}")
print("-" * 52)
print(f"Average of valid temps:     {valid_avg:.2f}°C")
print("=" * 52)
