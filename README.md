# Thiranex Task 4 — Real-world Retail Data Project

## Retail Sales Analysis and Customer Insights

### Objective

Analyze a real-world retail transaction dataset to discover sales trends, top-performing products, geographic performance, customer value, and relationships between sales metrics.

### Dataset

This project uses the **Online Retail** dataset from the **UCI Machine Learning Repository**.

The dataset contains transactions from **1 December 2010 to 9 December 2011** for a UK-based non-store online retailer.

The dataset retrieved through `ucimlrepo` contains the six features used in this project:

- Description
- Quantity
- InvoiceDate
- UnitPrice
- CustomerID
- Country

Source: https://archive.ics.uci.edu/dataset/352/online+retail

DOI: https://doi.org/10.24432/C5BW33

### Tools

- Python
- Pandas
- Matplotlib
- UCI `ucimlrepo`

### Analysis Performed

1. Data loading from UCI
2. Data cleaning
3. Revenue calculation
4. Monthly revenue trend
5. Top products by revenue
6. Top countries by revenue
7. Top customers by revenue
8. Revenue by day of week
9. Quantity vs revenue analysis
10. Customer RFM analysis
11. Correlation analysis
12. Business conclusions and recommendations

### Key Business Metrics

The analysis produced the following results:

- **Total revenue:** £10,666,684.54
- **Units sold:** 5,588,376
- **Cleaned transaction records:** 530,104
- **Unique products:** 4,026
- **Unique customers with CustomerID:** 4,338

### Generated Figures

The project generates the following eight visualizations:

- `01_monthly_revenue.png`
- `02_top_products.png`
- `03_top_countries.png`
- `04_top_customers.png`
- `05_revenue_by_day.png`
- `06_quantity_vs_revenue.png`
- `07_customer_frequency_vs_monetary.png`
- `08_sales_correlation_matrix.png`

### How to Run

Install the required dependencies:

```bash
pip install -r requirements.txt
