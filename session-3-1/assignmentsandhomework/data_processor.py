# data_processor.py
# Project: Data Processor (Loops for EVERYTHING)

# 1) Create list of 20 numbers (use range)
numbers = list(range(1, 21))  # 1 to 20

# 2) Calculate: sum, average, min, max (using loops)
total = 0
min_val = numbers[0]
max_val = numbers[0]

for n in numbers:
    total += n
    if n < min_val:
        min_val = n
    if n > max_val:
        max_val = n

average = total / len(numbers)

# 3) Count: evens, odds, divisible by 5 (using loops)
evens = 0
odds = 0
div_by_5 = 0

for n in numbers:
    if n % 2 == 0:
        evens += 1
    else:
        odds += 1
    if n % 5 == 0:
        div_by_5 += 1

# 4) Build new list: only numbers > average (using loops)
above_avg = []
for n in numbers:
    if n > average:
        above_avg.append(n)

# Output
print("=" * 46)
print("DATA PROCESSOR REPORT")
print("=" * 46)
print(f"Numbers:              {numbers}")
print(f"Count:                {len(numbers)}")
print(f"Sum:                  {total}")
print(f"Average:              {average:.2f}")
print(f"Minimum:              {min_val}")
print(f"Maximum:              {max_val}")
print("-" * 46)
print(f"Evens:                {evens}")
print(f"Odds:                 {odds}")
print(f"Divisible by 5:       {div_by_5}")
print("-" * 46)
print(f"Numbers > average:    {above_avg}")
print("=" * 46)
