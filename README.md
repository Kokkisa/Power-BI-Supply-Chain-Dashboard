# Power-BI-Supply-Chain-Dashboard
[README_project15.md](https://github.com/user-attachments/files/25794847/README_project15.md)
# Power BI Supply Chain Dashboard

## Overview
Three-page interactive Power BI dashboard for supply chain analytics covering demand trends, forecast accuracy, supplier performance, and inventory management. Built on petroleum supply chain data with 8 products across 4 regions over 2 years.

**Built by:** Nithin Kumar Kokkisa — Senior Demand Planner with 12+ years at HPCL managing 180,000 MTPA facility.

---

## Business Problem
Supply chain leaders need a single view of operations health: Are forecasts accurate? Are suppliers delivering on time? Is inventory optimally positioned? This dashboard answers these questions with interactive visuals and drill-down capability.

## Dashboard Pages

### Page 1: Executive Overview
- **5 KPI Cards**: Total Revenue, Total Demand, Forecast Accuracy %, OTD Rate, Quality Rate
- **Demand Trend**: Actual vs Forecast line chart (24 months)
- **Revenue by Product**: Horizontal bar chart (sorted by revenue)
- **Demand by Region**: Donut chart showing regional distribution
- **Quarterly Summary**: Table with Revenue, Demand, FA% per quarter

### Page 2: Supplier Scorecard
- **OTD Rate by Supplier**: Bar chart with 90% target line
- **Quality Rate by Supplier**: Bar chart with 95% target line
- **Supplier Detail Table**: Lead time, OTD count, quality count with conditional formatting
- **OTD Trend**: Line chart tracking each supplier's performance over time

### Page 3: Inventory Analysis
- **Inventory by Product**: Average ending inventory per product
- **Inventory vs Demand**: Scatter plot identifying over/understocked items
- **Safety Stock Coverage**: Product x Region detail table

### Interactive Slicers (All Pages)
- Year, Quarter, Region, Product filters
- Synced across all pages for consistent analysis

## Key Insights
1. **Supplier D** consistently below 90% OTD target — needs escalation
2. **Supplier E** has quality issues — 87% pass rate vs 95% target
3. **Diesel HSD** and **Petrol MS** show strong seasonal demand peaks in Apr-May and Oct-Nov
4. **East region** carries higher inventory relative to demand — potential optimization

## Dataset
- 768 records (8 products x 4 regions x 24 months)
- 20 features including demand, forecast, inventory, revenue, supplier metrics

## Files
- `Supply_Chain_Dashboard.pbix` — Power BI dashboard file
- `supply_chain_data.csv` — Source data
- `screenshots/` — Dashboard page screenshots

## Tools
- **Power BI Desktop** (free)
- **DAX** (Data Analysis Expressions for calculated measures)

---

## About
Part of a **30-project data analytics portfolio**. See [GitHub profile](https://github.com/Kokkisa) for the full portfolio.
