# Retail Sales & Profit Performance — Data Analyst Portfolio

**Owner:** Mohammed Tabish · **GitHub:** https://github.com/MOHDTABISH78

A **reproducible synthetic retail** project supporting a Power BI report with customer, product, region and time-series analysis. **This is a newly generated demonstration project, not real business data**. No external API or licensed dataset is used.

## What's included
- `data/retail_transactions.csv`: 19,380 transaction line rows across **12,400 orders** (2024–2025).
- `data/fact_sales.csv` plus three dimension tables (`dim_customers`, `dim_products`, `dim_dates`) and a separate order reference CSV.
- `dashboard/dashboard_preview.html`: responsive, self-contained **interactive browser dashboard** (not a native `.pbix`).
- `powerbi/measures.dax`: business measures and year-on-year analysis.
- `powerbi/transformations.m`: optional example Power Query import/cleaning.
- `docs/powerbi_setup.md`: guided Power BI Desktop modeling and design.
- `docs/business_insights.md`: computed insights, verified from synthetic data.
- `scripts/verify_project.py`: basic integrity tests.

## Start
1. **Download and extract** the project ZIP with Windows File Explorer.
2. Open `dashboard/dashboard_preview.html` in Chrome or Edge. Use filters to explore the simulated data.
3. Follow `docs/powerbi_setup.md` to create a real Power BI Desktop report.
4. Optionally run `python scripts/verify_project.py` from the extracted project folder to check the data.

## Data definition
`sales = quantity × unit_price × (1 − discount)`; `cost = quantity × unit_price × simulated_cost_ratio`; `profit = sales − cost`. Discounts range from 0–20%. Cost ratios are illustrative. The `retail_transactions.csv` file also contains denormalized human-readable category, product, region and segment fields.

## Portfolio notes
Dashboards and quantified metrics must be labelled **synthetic / simulated**. No unverified efficiency improvements or real-world impacts are claimed. The demo supports skills in data cleaning, star-schema modeling, DAX, SQL-style metrics and dashboard design. To publish on GitHub, see `docs/github_publish.md`.

## Resume bullets (use only after you personally review/test the implementation)
- Built a retail sales portfolio dataset of 19,380 synthetic transaction lines across 12,400 orders and modeled customer, product and date dimensions for Power BI.
- Defined DAX measures for revenue, gross profit, margins, average order value and period comparisons; designed KPI, regional and product reporting views.
- Developed a self-contained interactive HTML dashboard and documented reproducible data-quality checks.
