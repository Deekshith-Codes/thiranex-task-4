# Thiranex Task 4 — Real-world Retail Data Project

## Retail Sales Analysis and Customer Insights

### Objective
Analyze a real-world retail transaction dataset to discover sales trends,
top-performing products, geographic performance, customer value, and
relationships between sales metrics.

### Dataset
This project uses the **Online Retail** dataset from the
**UCI Machine Learning Repository**.

The dataset contains transactions from **1 December 2010 to 9 December 2011**
for a UK-based non-store online retailer. UCI reports 541,909 instances and
8 variables in its full dataset description.

Source:
https://archive.ics.uci.edu/dataset/352/online+retail

DOI:
https://doi.org/10.24432/C5BW33

### Tools
- Python
- Pandas
- Matplotlib
- UCI `ucimlrepo`

### Analysis performed

1. Data loading from UCI
2. Data cleaning
3. Cancellation identification
4. Revenue calculation
5. Monthly revenue trend
6. Top products by revenue
7. Top countries by revenue
8. Top customers by revenue
9. Orders by day of week
10. Quantity vs revenue analysis
11. Customer RFM analysis
12. Correlation analysis
13. Business conclusions and recommendations

### Generated figures

- `01_monthly_revenue.png`
- `02_top_products.png`
- `03_top_countries.png`
- `04_top_customers.png`
- `05_orders_by_day.png`
- `06_quantity_vs_revenue.png`
- `07_customer_frequency_vs_monetary.png`
- `08_sales_correlation_matrix.png`

### How to run

Install dependencies:

```bash
pip install -r requirements.txt
```

Then run:

```bash
python Task4.py
```

The script automatically retrieves the UCI dataset using `ucimlrepo` and
generates the analysis figures.

### Important data-cleaning choices

- Cancellation invoices are identified using invoice numbers beginning with
  `C` and excluded from completed-sales analysis.
- Rows with non-positive quantities or prices are excluded from revenue
  calculations.
- Revenue is calculated as:

`Revenue = Quantity × UnitPrice`

- Customer RFM analysis uses customers with available `CustomerID`.

### Business value

The analysis can support:
- Inventory planning
- Product prioritization
- Customer retention
- Marketing decisions
- Sales forecasting preparation
- Identification of high-value customers

### Conclusion

This project demonstrates an end-to-end real-world retail analytics workflow:
obtaining a public dataset, cleaning transaction data, engineering business
metrics, analyzing trends and customer behavior, visualizing findings, and
turning the results into actionable business insights.
