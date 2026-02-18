# data_analyzer_pro.py
# Complete Data Analyzer (Week 2 Session 2.2 Homework)
# - Mean, Median, Std Dev
# - Outliers: > 2 std dev from mean
# - Clean data (remove outliers)
# - Before/After stats
# - Use comprehensions throughout

# Dataset: 50 numbers (includes a few extreme values as outliers)
data = [
    52, 55, 49, 60, 58, 61, 57, 54, 59, 56,
    53, 62, 50, 51, 63, 64, 48, 47, 65, 66,
    52, 55, 57, 58, 59, 60, 61, 62, 63, 64,
    54, 56, 58, 60, 62, 50, 52, 53, 55, 57,
    58, 59, 60, 61, 62, 63, 64, 10, 120, 200
]

# ---------- Helper functions ----------
def mean(nums):
    return sum(nums) / len(nums) if nums else 0

def median(nums):
    s = sorted(nums)
    n = len(s)
    if n == 0:
        return 0
    mid = n // 2
    return s[mid] if n % 2 == 1 else (s[mid - 1] + s[mid]) / 2

def std_dev(nums):
    # Population standard deviation
    m = mean(nums)
    variance = sum([(x - m) ** 2 for x in nums]) / len(nums) if nums else 0
    return variance ** 0.5

def summarize(label, nums):
    m = mean(nums)
    med = median(nums)
    sd = std_dev(nums)
    return {
        "label": label,
        "count": len(nums),
        "mean": m,
        "median": med,
        "std": sd,
        "min": min(nums) if nums else None,
        "max": max(nums) if nums else None,
    }

# ---------- Before stats ----------
before = summarize("BEFORE (raw data)", data)
m = before["mean"]
sd = before["std"]

# ---------- Outliers (> 2 std dev from mean) ----------
outliers = [x for x in data if abs(x - m) > 2 * sd]

# ---------- Clean data (remove outliers) ----------
clean_data = [x for x in data if abs(x - m) <= 2 * sd]

# ---------- After stats ----------
after = summarize("AFTER (cleaned data)", clean_data)

# ---------- Output ----------
print("=" * 60)
print("DATA ANALYZER PRO REPORT")
print("=" * 60)

print(f"Dataset size (raw): {before['count']}")
print(f"Raw data (50 nums): {data}")

print("\n--- BEFORE STATS ---")
print(f"Count:  {before['count']}")
print(f"Mean:   {before['mean']:.2f}")
print(f"Median: {before['median']:.2f}")
print(f"StdDev: {before['std']:.2f}")
print(f"Min:    {before['min']}")
print(f"Max:    {before['max']}")

print("\n--- OUTLIERS (> 2 std dev from mean) ---")
print(f"Outliers found: {len(outliers)}")
print(f"Outlier values: {sorted(outliers)}")

print("\n--- CLEANED DATA ---")
print(f"Dataset size (clean): {after['count']}")
print(f"Clean data: {clean_data}")

print("\n--- AFTER STATS ---")
print(f"Count:  {after['count']}")
print(f"Mean:   {after['mean']:.2f}")
print(f"Median: {after['median']:.2f}")
print(f"StdDev: {after['std']:.2f}")
print(f"Min:    {after['min']}")
print(f"Max:    {after['max']}")

print("\nNice work — this is the exact workflow: analyze → detect outliers → clean → re-check stats.")
print("=" * 60)
