# product_catalog.py
# Real inventory management using dictionaries + loops

product1 = {
    "name": "Laptop",
    "price": 999.99,
    "category": "Electronics",
    "in_stock": True
}

product2 = {
    "name": "Desk Chair",
    "price": 149.50,
    "category": "Furniture",
    "in_stock": False
}

product3 = {
    "name": "Water Bottle",
    "price": 18.99,
    "category": "Accessories",
    "in_stock": True
}

products = [product1, product2, product3]

# 1) Calculate total value of all products (sum of prices)
total_value = 0
for p in products:
    total_value += p["price"]

# 2) Count how many are in stock
in_stock_count = 0
for p in products:
    if p["in_stock"]:
        in_stock_count += 1

# 3) Find most expensive product
most_expensive = products[0]
for p in products:
    if p["price"] > most_expensive["price"]:
        most_expensive = p

# Print original catalog
print("=" * 60)
print("PRODUCT CATALOG (ORIGINAL)")
print("=" * 60)
for p in products:
    print(f"{p['name']:<15}  ${p['price']:>8.2f}  {p['category']:<12}  In stock: {p['in_stock']}")
print("-" * 60)
print(f"Total value:     ${total_value:.2f}")
print(f"In stock count:  {in_stock_count}")
print(f"Most expensive:  {most_expensive['name']} (${most_expensive['price']:.2f})")

# 4) Give 10% discount to all (update prices)
for p in products:
    p["price"] = round(p["price"] * 0.90, 2)

# Recalculate total after discount
discounted_total = 0
for p in products:
    discounted_total += p["price"]

# Print updated catalog
print("\n" + "=" * 60)
print("PRODUCT CATALOG (AFTER 10% DISCOUNT)")
print("=" * 60)
for p in products:
    print(f"{p['name']:<15}  ${p['price']:>8.2f}  {p['category']:<12}  In stock: {p['in_stock']}")
print("-" * 60)
print(f"Total value (discounted): ${discounted_total:.2f}")
print("=" * 60)
