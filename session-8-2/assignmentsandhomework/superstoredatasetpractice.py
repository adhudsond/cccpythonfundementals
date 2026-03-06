import pandas as pd
import matplotlib.pyplot as plt

# 1. Import libraries
# pandas and matplotlib imported above

# 2. Load dataset
# Change the file name if needed
df = pd.read_csv("Superstore.csv", encoding="latin1")

# 3. Data exploration
print("First 5 rows:")
print(df.head())

print("\nColumns:")
print(df.columns)

print("\nDataset info:")
print(df.info())

print("\nSummary statistics:")
print(df.describe())

print("\nMissing values:")
print(df.isnull().sum())

# Convert Order Date to datetime for monthly analysis
df["Order Date"] = pd.to_datetime(df["Order Date"])

# 4. Total revenue
total_revenue = df["Sales"].sum()
print("\nTotal Revenue:", total_revenue)

# 5. Revenue by region
revenue_by_region = df.groupby("Region")["Sales"].sum().sort_values(ascending=False)
print("\nRevenue by Region:")
print(revenue_by_region)

# 6. Visualization – region sales
plt.figure(figsize=(8, 5))
revenue_by_region.plot(kind="bar")
plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 7. Sales by category
sales_by_category = df.groupby("Category")["Sales"].sum().sort_values(ascending=False)
print("\nSales by Category:")
print(sales_by_category)

# 8. Visualization – category sales
plt.figure(figsize=(8, 5))
sales_by_category.plot(kind="bar")
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 9. Region with most orders
region_most_orders = df["Region"].value_counts()
print("\nNumber of Orders by Region:")
print(region_most_orders)
print("\nRegion with Most Orders:", region_most_orders.idxmax())

# 10. Top 5 highest sales
top_5_sales = df.nlargest(5, "Sales")
print("\nTop 5 Highest Sales:")
print(top_5_sales[["Order ID", "Customer Name", "Region", "Category", "Sales", "Profit"]])

# 11. Filter West region
west_region = df[df["Region"] == "West"]
print("\nWest Region Data:")
print(west_region.head())

# 12. Filter sales > $1000
sales_above_1000 = df[df["Sales"] > 1000]
print("\nSales Greater Than $1000:")
print(sales_above_1000[["Order ID", "Customer Name", "Region", "Category", "Sales"]].head())

# 13. Average sales per category
avg_sales_per_category = df.groupby("Category")["Sales"].mean().sort_values(ascending=False)
print("\nAverage Sales per Category:")
print(avg_sales_per_category)

# 14. Monthly sales calculation
df["Month"] = df["Order Date"].dt.to_period("M")
monthly_sales = df.groupby("Month")["Sales"].sum()
print("\nMonthly Sales:")
print(monthly_sales)

# Optional: convert PeriodIndex to string for plotting
monthly_sales.index = monthly_sales.index.astype(str)

# 15. Monthly sales visualization
plt.figure(figsize=(12, 5))
monthly_sales.plot(kind="line", marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 16. Most Profitable Category
profit_by_category = df.groupby("Category")["Profit"].sum().sort_values(ascending=False)
print("\nProfit by Category:")
print(profit_by_category)
print("\nMost Profitable Category:", profit_by_category.idxmax())

# 17. Most Profitable Region
profit_by_region = df.groupby("Region")["Profit"].sum().sort_values(ascending=False)
print("\nProfit by Region:")
print(profit_by_region)
print("\nMost Profitable Region:", profit_by_region.idxmax())