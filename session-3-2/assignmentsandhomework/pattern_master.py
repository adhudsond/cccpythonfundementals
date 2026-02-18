# pattern_master.py
# Generate multiple patterns using nested loops

print("=" * 40)
print("PATTERN MASTER")
print("=" * 40)

# -------------------------
# Pattern 1: Square (5x5)
# -------------------------
print("\nPattern 1: Square")
size = 5
for _ in range(size):
    for _ in range(size):
        print("*", end="")
    print()

# -------------------------
# Pattern 2: Countdown
# -------------------------
print("\nPattern 2: Countdown")
start = 5
for row in range(start, 0, -1):          # row controls how many numbers to print
    for num in range(start, start - row, -1):
        print(num, end=" ")
    print()

# -------------------------
# Pattern 3: Number grid (1–25 in 5×5)
# -------------------------
print("\nPattern 3: Number Grid (1–25)")
current = 1
rows = 5
cols = 5

for r in range(rows):
    for c in range(cols):
        print(f"{current:>2}", end=" ")
        current += 1
    print()

print("\n" + "=" * 40)
