# Power BI Desktop guide

## Step 1 — Import
Extract the ZIP first. Open Power BI Desktop and choose **Get Data → Text/CSV**. Import `data/fact_sales.csv`, `data/dim_customers.csv`, `data/dim_products.csv`, `data/dim_dates.csv`. Rename the imported queries **FactSales**, **DimCustomer**, **DimProduct**, **DimDate** respectively. In **Transform data**, check types: identifiers/text, dates/date, quantities/whole number, monetary values/decimal or fixed decimal, discount/decimal. Trim identifiers if needed; choose **Close & Apply**.

A reusable example Power Query script is in `powerbi/transformations.m`. It is optional; entering each table through Get Data is easier for beginners. You must replace its placeholder Windows file path before running it.

## Step 2 — Data model
In **Model view**, create the following *single-direction, one-to-many* relationships:

- `DimCustomer[customer_id]` (1) → `FactSales[customer_id]` (*)
- `DimProduct[product_id]` (1) → `FactSales[product_id]` (*)
- `DimDate[date]` (1) → `FactSales[order_date]` (*)

Select `DimDate` and **Mark as date table**, choosing its `date` column. The generated dim_dates table has one row per day, with no missing dates. Use DimCustomer region/segment and DimProduct category/product in visuals and slicers.

## Step 3 — Measures
Create measures shown in `powerbi/measures.dax` using **Modeling → New measure**. Enter **one measure per action** (the `.dax` file is a reference, not a single executable batch). Format `Profit Margin` and `Revenue YoY %` as percentages; other monetary measures as INR (₹).

## Step 4 — Canvas (16:9, navy accents)

Top: title `Retail Sales & Profit Performance | 2024–2025` and slicers for Year, Region, Category, Segment.

Row 1: Cards for **Total Revenue**, **Total Profit**, **Profit Margin**, **Total Orders**, **Average Order Value**.

Row 2: Line chart: `DimDate[year_month]` vs `Total Revenue`; bar chart: `DimCustomer[region]` vs `Total Revenue`.

Row 3: horizontal bar chart: `DimProduct[category]` vs `Total Revenue`, sorted descending; table with product, Revenue, Profit, Margin.

Filter labels should show that examples are simulated. Cross-filter interactions can be adjusted via **Format → Edit interactions**. Set page to 16:9 and use a consistent navy/white theme.

## Step 5 — Validate
With all filters cleared, **Total Orders** should equal 12,400 and **Units Sold** should equal the sum of `quantity` in `data/retail_transactions.csv`. Compare Total Revenue / Profit with `docs/business_insights.md`. Save the finished native file yourself as `.pbix`; the ZIP contains instructions but **does not contain a PBIX file**.
