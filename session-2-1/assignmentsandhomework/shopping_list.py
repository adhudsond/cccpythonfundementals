# shopping_list.py
# Smart Shopping List (lists + clear output)

print("Welcome to Smart Shopping List 🛒\n")

# 1) Start with:
items = ['apples', 'bread', 'milk']
print(f"Starting list: {items}")

# 2) Add 'eggs' to the list
items.append('eggs')
print(f"Added eggs:    {items}")

# 3) Add 'cheese' to the list
items.append('cheese')
print(f"Added cheese:  {items}")

# 4) Remove 'bread' (already have it)
if 'bread' in items:
    items.remove('bread')
    print(f"Removed bread: {items}")
else:
    print("Bread was not in the list, so nothing to remove.")

# 5) Insert 'butter' at position 0 (need it first)
items.insert(0, 'butter')
print(f"Inserted butter at position 0: {items}")

# 6) Print final list
print("\n----- FINAL SHOPPING LIST -----")
print(items)

# 7) Print how many items total
print(f"Total items: {len(items)}")

# 8) Print first and last items
print(f"First item: {items[0]}")
print(f"Last item:  {items[-1]}")
print("------------------------------")
