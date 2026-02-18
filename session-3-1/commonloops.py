# 1. Read and process each item (transformation / mapping) - Clean and standardize city names
cities = [" new york ", "Los angeles", "chicago ", "houston", "PHOENIX"]
cleaned_cities = []
for city in cities: # process each item: strip whitespace + title case
    cleaned = city.strip().title()
    cleaned_cities.append(cleaned)
print(cleaned_cities)
# Output: ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix’]
# Alternative one-liner style:
cleaned_cities = [city.strip().title() for city in cities]
# 2: Accumulate results (sum, count, min/max, product, concatenation…)
sales = [120.50, 45.00, 890.75, 15.20, 320.00, 675.30]
total_sales = 0
high_value_count = 0
for amount in sales:
    total_sales += amount # accumulate sum
if amount > 500:
    high_value_count += 1 # accumulate count
average_sale = total_sales / len(sales)
print(f"Total sales : ${total_sales:,.2f}")
print(f"Average sale : ${average_sale:,.2f}")
print(f"High-value sales (> $500): {high_value_count}")
# Output: # Total sales : $2,066.75
# Average sale : $344.46
# High-value sales (> $500): 2

# 3. Filter data (create a new list with only items that match a condition)
import datetime # use this if getting syntax error: from datetime import datetime
dates = [
 datetime.date(2025, 10, 13), # Monday
 datetime.date(2025, 10, 14), # Tuesday
 datetime.date(2025, 10, 15), # Wednesday
 datetime.date(2025, 10, 18), # Saturday
 datetime.date(2025, 10, 19), # Sunday
 datetime.date(2025, 10, 20), # Monday
]
weekdays = []
for dt in dates:
 if dt.weekday() < 5: # 0–4 = Mon–Fri
    weekdays.append(dt)
print("Weekdays only:")
for d in weekdays:
 print(d.strftime("%A, %Y-%m-%d"))
# Output:
# Weekdays only:
# Monday, 2025-10-13
# Tuesday, 2025-10-14
# Wednesday, 2025-10-15
# Monday, 2025-10-20