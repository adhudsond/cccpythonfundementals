# temp_analyzer.py
# Weekly Temperature Analyzer (lists + stats + f-strings)

temperatures = [72, 68, 75, 70, 73, 69, 71]

# 1) Average temperature
avg_temp = sum(temperatures) / len(temperatures)

# 2) Highest temperature
high_temp = max(temperatures)

# 3) Lowest temperature
low_temp = min(temperatures)

# 4) Temperature range (high - low)
temp_range = high_temp - low_temp

# 5) Days above average
days_above_avg = sum(1 for t in temperatures if t > avg_temp)

# 6) Days below 70 degrees
days_below_70 = sum(1 for t in temperatures if t < 70)

print("----- Weekly Temperature Report -----")
print(f"Temperatures:         {temperatures}")
print(f"Average temperature:  {avg_temp:.2f}°")
print(f"Highest temperature:  {high_temp}°")
print(f"Lowest temperature:   {low_temp}°")
print(f"Temperature range:    {temp_range}°")
print(f"Days above average:   {days_above_avg}")
print(f"Days below 70°:       {days_below_70}")
print("------------------------------------")
