# Calculate statistics from dictionary
prices = {
'laptop': 999.99,
'mouse': 25.50,
'keyboard': 79.99,
'monitor': 299.99
}
# Total value
total = sum(prices.values())
print(f'Total: ${total:.2f}') # $1405.47
# Average price
avg = total / len(prices)
print(f'Average: ${avg:.2f}') # $351.37
# Most expensive
max_item = max(prices, key=prices.get)
print(f'Most expensive: {max_item}') # laptop
# Real data analysis!