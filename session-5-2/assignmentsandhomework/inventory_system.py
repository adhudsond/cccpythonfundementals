# inventory_system.py
# Nested Inventory System (categories -> products -> {price, stock})

inventory = {
    "laptops": {
        "Dell": {"price": 999, "stock": 5},
        "HP": {"price": 899, "stock": 3}
    },
    "phones": {
        "iPhone": {"price": 1099, "stock": 10},
        "Samsung": {"price": 899, "stock": 7}
    }
}

# 1) Total value per category
category_values = {}  # category -> total value
category_avg_prices = {}  # category -> average price

total_inventory_value = 0
low_stock_products = []  # (category, product, stock)

for category, products in inventory.items():
    cat_value = 0
    price_total = 0
    product_count = 0

    for product_name, info in products.items():
        price = info.get("price", 0)
        stock = info.get("stock", 0)

        # category value accumulates price * stock
        cat_value += price * stock

        # for average price
        price_total += price
        product_count += 1

        # 3) low stock (< 5)
        if stock < 5:
            low_stock_products.append((category, product_name, stock))

    category_values[category] = cat_value
    category_avg_prices[category] = (price_total / product_count) if product_count > 0 else 0

    # 2) total inventory value
    total_inventory_value += cat_value

# Report
print("=" * 70)
print("INVENTORY SYSTEM REPORT")
print("=" * 70)

print("\n--- Category Values ---")
for category, value in category_values.items():
    print(f"{category.title():<10} Total value: ${value:,.2f}")

print("\n--- Average Price Per Category ---")
for category, avg_price in category_avg_prices.items():
    print(f"{category.title():<10} Average price: ${avg_price:,.2f}")

print("\n--- Total Inventory Value ---")
print(f"Total inventory value: ${total_inventory_value:,.2f}")

print("\n--- Low Stock Products (stock < 5) ---")
if low_stock_products:
    for cat, name, stock in low_stock_products:
        print(f"{cat.title():<10} {name:<10} Stock: {stock}")
else:
    print("None")

print("=" * 70)
