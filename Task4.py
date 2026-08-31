"""
THIRANEX TASK 4
Real-world Data Project: Retail Sales Analysis and Customer Insights

Dataset:
UCI Machine Learning Repository - Online Retail
DOI: https://doi.org/10.24432/C5BW33

The script downloads the dataset through ucimlrepo, cleans transactions,
creates revenue metrics, performs sales/customer analysis, and generates
visualizations.
"""

import pandas as pd
import matplotlib.pyplot as plt
from ucimlrepo import fetch_ucirepo


# ------------------------------------------------------------
# 1. LOAD REAL-WORLD DATASET
# ------------------------------------------------------------
print("=" * 70)
print("THIRANEX TASK 4 - RETAIL SALES ANALYSIS")
print("=" * 70)

print("\nLoading UCI Online Retail dataset...")

online_retail = fetch_ucirepo(id=352)

# UCI provides the feature table for this dataset
df = online_retail.data.features.copy()

print("\nOriginal dataset shape:", df.shape)
print("\nOriginal columns:")
print(df.columns.tolist())


# ------------------------------------------------------------
# 2. DATA CLEANING
# ------------------------------------------------------------
print("\n" + "=" * 70)
print("DATA CLEANING")
print("=" * 70)

# Standardize column names
df.columns = [
    str(col).strip().replace(" ", "_").replace("/", "_")
    for col in df.columns
]

# Convert date column
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"], errors="coerce")

# Remove rows without essential transaction information
df = df.dropna(subset=["InvoiceDate", "Description", "Quantity", "UnitPrice"])

# Identify cancellations
df["IsCancellation"] = df["InvoiceNo"].astype(str).str.upper().str.startswith("C")

cancellation_count = int(df["IsCancellation"].sum())

# Keep completed sales only for sales analysis
sales = df[
    (~df["IsCancellation"])
    & (df["Quantity"] > 0)
    & (df["UnitPrice"] > 0)
].copy()

# Calculate revenue
sales["Revenue"] = sales["Quantity"] * sales["UnitPrice"]

# Date features
sales["Year"] = sales["InvoiceDate"].dt.year
sales["Month"] = sales["InvoiceDate"].dt.to_period("M").astype(str)
sales["MonthName"] = sales["InvoiceDate"].dt.strftime("%b")
sales["DayOfWeek"] = sales["InvoiceDate"].dt.day_name()

print("Cancellation records:", cancellation_count)
print("Clean sales rows:", len(sales))
print("Customers with CustomerID:", sales["CustomerID"].notna().sum())


# ------------------------------------------------------------
# 3. BASIC BUSINESS METRICS
# ------------------------------------------------------------
total_revenue = sales["Revenue"].sum()
total_units = sales["Quantity"].sum()
unique_orders = sales["InvoiceNo"].nunique()
unique_products = sales["StockCode"].nunique()
unique_customers = sales["CustomerID"].nunique()

print("\n" + "=" * 70)
print("KEY BUSINESS METRICS")
print("=" * 70)
print(f"Total revenue: £{total_revenue:,.2f}")
print(f"Units sold: {total_units:,.0f}")
print(f"Unique orders: {unique_orders:,}")
print(f"Unique products: {unique_products:,}")
print(f"Unique customers with CustomerID: {unique_customers:,}")


# ------------------------------------------------------------
# 4. MONTHLY SALES TREND
# ------------------------------------------------------------
monthly_sales = (
    sales.groupby("Month", as_index=False)["Revenue"]
    .sum()
    .sort_values("Month")
)

plt.figure(figsize=(10, 5))
plt.plot(monthly_sales["Month"], monthly_sales["Revenue"], marker="o")
plt.title("Figure 1: Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue (£)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("01_monthly_revenue.png", dpi=200)
plt.show()


# ------------------------------------------------------------
# 5. TOP PRODUCTS BY REVENUE
# ------------------------------------------------------------
top_products = (
    sales.groupby("Description", as_index=False)["Revenue"]
    .sum()
    .sort_values("Revenue", ascending=False)
    .head(10)
)

print("\nTop 10 products by revenue:")
print(top_products.to_string(index=False))

plt.figure(figsize=(10, 6))
plt.barh(
    top_products["Description"].iloc[::-1],
    top_products["Revenue"].iloc[::-1]
)
plt.title("Figure 2: Top 10 Products by Revenue")
plt.xlabel("Revenue (£)")
plt.ylabel("Product")
plt.tight_layout()
plt.savefig("02_top_products.png", dpi=200)
plt.show()


# ------------------------------------------------------------
# 6. TOP COUNTRIES BY REVENUE
# ------------------------------------------------------------
top_countries = (
    sales.groupby("Country", as_index=False)["Revenue"]
    .sum()
    .sort_values("Revenue", ascending=False)
    .head(10)
)

print("\nTop 10 countries by revenue:")
print(top_countries.to_string(index=False))

plt.figure(figsize=(10, 6))
plt.barh(
    top_countries["Country"].iloc[::-1],
    top_countries["Revenue"].iloc[::-1]
)
plt.title("Figure 3: Top 10 Countries by Revenue")
plt.xlabel("Revenue (£)")
plt.ylabel("Country")
plt.tight_layout()
plt.savefig("03_top_countries.png", dpi=200)
plt.show()


# ------------------------------------------------------------
# 7. TOP CUSTOMERS BY REVENUE
# ------------------------------------------------------------
customer_sales = (
    sales.dropna(subset=["CustomerID"])
    .groupby("CustomerID", as_index=False)["Revenue"]
    .sum()
    .sort_values("Revenue", ascending=False)
    .head(10)
)

print("\nTop 10 customers by revenue:")
print(customer_sales.to_string(index=False))

plt.figure(figsize=(10, 6))
plt.bar(
    customer_sales["CustomerID"].astype(str),
    customer_sales["Revenue"]
)
plt.title("Figure 4: Top 10 Customers by Revenue")
plt.xlabel("Customer ID")
plt.ylabel("Revenue (£)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("04_top_customers.png", dpi=200)
plt.show()


# ------------------------------------------------------------
# 8. DAY-OF-WEEK ORDER PATTERN
# ------------------------------------------------------------
daily_orders = (
    sales.groupby("DayOfWeek")["InvoiceNo"]
    .nunique()
    .reindex([
        "Monday", "Tuesday", "Wednesday",
        "Thursday", "Friday", "Saturday", "Sunday"
    ])
)

plt.figure(figsize=(9, 5))
plt.bar(daily_orders.index, daily_orders.values)
plt.title("Figure 5: Orders by Day of Week")
plt.xlabel("Day")
plt.ylabel("Number of Unique Orders")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("05_orders_by_day.png", dpi=200)
plt.show()


# ------------------------------------------------------------
# 9. REVENUE VS QUANTITY
# ------------------------------------------------------------
product_metrics = (
    sales.groupby("StockCode", as_index=False)
    .agg(
        Quantity=("Quantity", "sum"),
        Revenue=("Revenue", "sum"),
        UnitPrice=("UnitPrice", "mean")
    )
)

plt.figure(figsize=(8, 6))
plt.scatter(
    product_metrics["Quantity"],
    product_metrics["Revenue"],
    alpha=0.5
)
plt.title("Figure 6: Quantity Sold vs Revenue")
plt.xlabel("Total Quantity Sold")
plt.ylabel("Total Revenue (£)")
plt.tight_layout()
plt.savefig("06_quantity_vs_revenue.png", dpi=200)
plt.show()


# ------------------------------------------------------------
# 10. CUSTOMER RFM ANALYSIS
# ------------------------------------------------------------
customer_data = sales.dropna(subset=["CustomerID"]).copy()

snapshot_date = customer_data["InvoiceDate"].max() + pd.Timedelta(days=1)

rfm = (
    customer_data.groupby("CustomerID")
    .agg(
        Recency=("InvoiceDate", lambda x: (snapshot_date - x.max()).days),
        Frequency=("InvoiceNo", "nunique"),
        Monetary=("Revenue", "sum")
    )
    .reset_index()
)

print("\nRFM summary:")
print(rfm.describe())

plt.figure(figsize=(8, 6))
plt.scatter(
    rfm["Frequency"],
    rfm["Monetary"],
    alpha=0.5
)
plt.title("Figure 7: Customer Frequency vs Monetary Value")
plt.xlabel("Purchase Frequency (Unique Orders)")
plt.ylabel("Monetary Value (£)")
plt.tight_layout()
plt.savefig("07_customer_frequency_vs_monetary.png", dpi=200)
plt.show()


# ------------------------------------------------------------
# 11. CORRELATION ANALYSIS
# ------------------------------------------------------------
correlation_data = sales[["Quantity", "UnitPrice", "Revenue"]].corr()

print("\nCorrelation matrix:")
print(correlation_data)

plt.figure(figsize=(6, 5))
plt.imshow(correlation_data, aspect="auto")
plt.colorbar(label="Correlation")
plt.xticks(
    range(len(correlation_data.columns)),
    correlation_data.columns
)
plt.yticks(
    range(len(correlation_data.columns)),
    correlation_data.columns
)
plt.title("Figure 8: Sales Metrics Correlation Matrix")
plt.tight_layout()
plt.savefig("08_sales_correlation_matrix.png", dpi=200)
plt.show()


# ------------------------------------------------------------
# 12. BUSINESS CONCLUSIONS
# ------------------------------------------------------------
best_month = monthly_sales.loc[
    monthly_sales["Revenue"].idxmax()
]

best_country = top_countries.iloc[0]
best_product = top_products.iloc[0]
best_customer = customer_sales.iloc[0]

print("\n" + "=" * 70)
print("BUSINESS INSIGHTS AND CONCLUSIONS")
print("=" * 70)

print(
    f"1. The highest-revenue month in the analyzed period was "
    f"{best_month['Month']} with £{best_month['Revenue']:,.2f}."
)

print(
    f"2. {best_country['Country']} generated the highest revenue among "
    f"the countries in the dataset, at £{best_country['Revenue']:,.2f}."
)

print(
    f"3. The highest-revenue product was "
    f"'{best_product['Description']}' with "
    f"£{best_product['Revenue']:,.2f}."
)

print(
    f"4. Customer {best_customer['CustomerID']:.0f} was the highest-value "
    f"customer in the top-customer analysis, generating "
    f"£{best_customer['Revenue']:,.2f}."
)

print(
    "5. Customer RFM analysis can help the business identify "
    "high-value and frequently purchasing customers."
)

print(
    "6. Monthly and weekday sales patterns can support inventory, "
    "marketing, and staffing decisions."
)

print(
    "7. Product-level revenue and quantity analysis can help prioritize "
    "high-performing products."
)

print("\nTask 4 completed successfully.")
