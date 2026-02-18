# budget.py

# 1) Monthly expenses (edit these numbers to match your real budget)
rent = 1200
food = 400
transport = 120
entertainment = 150

# Optional: monthly income (set to 0 if you don't want to include income)
income = 2500

# 2) Calculate total expenses
total_expenses = rent + food + transport + entertainment

# 3) If you have income, calculate savings
savings = income - total_expenses

# 4) Print results nicely
print("----- Monthly Budget Summary -----")
print(f"Rent:           ${rent}")
print(f"Food:           ${food}")
print(f"Transport:      ${transport}")
print(f"Entertainment:  ${entertainment}")
print("----------------------------------")
print(f"Total expenses: ${total_expenses}")

if income > 0:
    print(f"Income:         ${income}")
    print(f"Savings:        ${savings}")

    if savings > 0:
        print("Status: You are saving money ✅")
    elif savings == 0:
        print("Status: You break even ⚖️")
    else:
        print("Status: You are overspending ❌")
