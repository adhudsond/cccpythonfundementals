# mult_table_generator.py
# Full 1–10 multiplication table using nested loops (with headers + aligned columns)

print("=" * 78)
print("FULL MULTIPLICATION TABLE (1 to 10)")
print("=" * 78)

# Bonus: Column headers
print(f"{'':>4}", end="")  # top-left blank corner
for col in range(1, 11):
    print(f"{col:>7}", end="")
print()
print("-" * 78)

# 1) Nested loops for rows and columns
for row in range(1, 11):
    # Bonus: Row header
    print(f"{row:>3} |", end="")

    for col in range(1, 11):
        product = row * col

        # 2-4) Print formatted cell, aligned nicely
        # Example: " 1×10=10" fits in 7 chars wide with right alignment
        print(f"{row}×{col}={product:>2}".rjust(7), end="")

    print()  # new line after each row

print("=" * 78)
