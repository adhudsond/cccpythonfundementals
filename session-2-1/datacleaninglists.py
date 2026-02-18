# Raw data with errors
ages = [25, 32, -5, 28, 150, 45, 19]
# Remove negative age
ages.remove(-5)
# Remove outlier
ages.remove(150)
print(ages) # [25, 32, 28, 45, 19]
# Now calculate statistics
average_age = sum(ages) / len(ages)
print(f'Average age: {average_age:.1f}') # 29.8
# Clean data = accurate results!
# This is data science!