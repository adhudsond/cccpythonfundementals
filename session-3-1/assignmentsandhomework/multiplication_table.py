# multiplication_table.py
# Multiplication Table Generator (Loops + range + f-strings)

# 1) Ask user for a number (fallback to 7 if they press Enter)
user_input = input("Enter a number for the multiplication table (press Enter for 7): ").strip()

number = int(user_input) if user_input else 7

print("\n" + "=" * 34)
print(f"MULTIPLICATION TABLE: {number}")
print("=" * 34)

# 2) Use a for loop with range(1, 11)
for i in range(1, 11):
    # 3-4) Print formatted line
    print(f"{number} × {i:>2} = {number * i}")

print("=" * 34)
