# =============================================================================
# PROJECT 15: POWER BI SUPPLY CHAIN DASHBOARD
# (Plan #15 — Block D: Dashboards & Visualization)
# =============================================================================
#
# This project is built in POWER BI DESKTOP (free), not Python.
# Below is your step-by-step guide to build it.
#
# PREREQUISITE: Download Power BI Desktop (free) from:
# https://powerbi.microsoft.com/en-us/desktop/
#
# DATASET: supply_chain_data.csv (downloaded from Claude)
#
# ESTIMATED TIME: 2 hours
# =============================================================================


# =============================================================================
# STEP 1: INSTALL POWER BI DESKTOP (5 minutes)
# =============================================================================
#
# 1. Go to: https://powerbi.microsoft.com/en-us/desktop/
# 2. Click "Download free"
# 3. Choose "Download from Microsoft Store" (easiest) or .exe installer
# 4. Install and open Power BI Desktop
# 5. Sign in with a Microsoft account (free, use any email)
#    OR click "Already have an account? Sign in" then "X" to skip


# =============================================================================
# STEP 2: LOAD THE DATA (5 minutes)
# =============================================================================
#
# 1. Open Power BI Desktop
# 2. Click "Get Data" (top ribbon) → "Text/CSV"
# 3. Navigate to where you saved supply_chain_data.csv
# 4. Click "Open" → Preview appears → Click "Load"
# 5. The data appears in the Fields pane on the right
#
# VERIFY: You should see all 20 columns listed in the Fields pane:
#   Date, Year, Month, Month_Num, Quarter, Product, Region, Supplier,
#   Actual_Demand, Forecast_Demand, Inventory_Start, Inventory_End,
#   Revenue, COGS, Cost_Per_Unit, Lead_Time_Days, On_Time_Delivery,
#   Quality_Pass, Order_Qty, Safety_Stock


# =============================================================================
# STEP 3: CREATE CALCULATED MEASURES (10 minutes)
# =============================================================================
#
# In Power BI, "Measures" are calculations that update with filters.
# Click on the table in the Fields pane, then:
# Home ribbon → "New Measure" → type the formula → press Enter
#
# CREATE THESE 6 MEASURES:
#
# Measure 1: Total Revenue
#   Total Revenue = SUM(supply_chain_data[Revenue])
#
# Measure 2: Total Demand
#   Total Demand = SUM(supply_chain_data[Actual_Demand])
#
# Measure 3: Forecast Accuracy
#   FA% = 1 - DIVIDE(
#       SUM(ABS(supply_chain_data[Forecast_Demand] - supply_chain_data[Actual_Demand])),
#       SUM(supply_chain_data[Actual_Demand]),
#       0
#   )
#
#   NOTE: If the ABS formula doesn't work, create a helper column first:
#   Go to: Modeling → New Column → type:
#   Abs_Error = ABS(supply_chain_data[Forecast_Demand] - supply_chain_data[Actual_Demand])
#   Then: FA% = 1 - DIVIDE(SUM(supply_chain_data[Abs_Error]), SUM(supply_chain_data[Actual_Demand]), 0)
#
# Measure 4: Inventory Turns
#   Inventory Turns = DIVIDE(
#       SUM(supply_chain_data[COGS]),
#       AVERAGE(supply_chain_data[Inventory_End]) * AVERAGE(supply_chain_data[Cost_Per_Unit]),
#       0
#   )
#
# Measure 5: On-Time Delivery Rate
#   OTD Rate = DIVIDE(
#       SUM(supply_chain_data[On_Time_Delivery]),
#       COUNT(supply_chain_data[On_Time_Delivery]),
#       0
#   )
#
# Measure 6: Supplier Quality Rate
#   Quality Rate = DIVIDE(
#       SUM(supply_chain_data[Quality_Pass]),
#       COUNT(supply_chain_data[Quality_Pass]),
#       0
#   )


# =============================================================================
# STEP 4: BUILD THE DASHBOARD — PAGE 1: EXECUTIVE OVERVIEW (20 minutes)
# =============================================================================
#
# 4.1 ADD KPI CARDS (Top row — 5 cards)
# ─────────────────────────────────────
# From Visualizations pane, click "Card" icon (rectangle with big number)
# Drag each measure to the card:
#
#   Card 1: Total Revenue → format as Currency
#   Card 2: Total Demand → format as Number with commas
#   Card 3: FA% → format as Percentage
#   Card 4: OTD Rate → format as Percentage
#   Card 5: Quality Rate → format as Percentage
#
# Arrange 5 cards across the top of the page.
# Resize each to be small and compact.
#
# 4.2 DEMAND TREND LINE CHART (Left middle)
# ──────────────────────────────────────────
# Click "Line Chart" from Visualizations
#   X-axis: Date
#   Y-axis: Actual_Demand (Sum)
#   Also add: Forecast_Demand (Sum) as second line
# Title: "Demand Trend: Actual vs Forecast"
#
# 4.3 REVENUE BY PRODUCT (Right middle — Horizontal Bar Chart)
# ─────────────────────────────────────────────────────────────
# Click "Stacked Bar Chart"
#   Y-axis: Product
#   X-axis: Revenue (Sum)
# Title: "Revenue by Product"
# Sort descending by Revenue
#
# 4.4 DEMAND BY REGION (Bottom left — Donut Chart)
# ─────────────────────────────────────────────────
# Click "Donut Chart"
#   Legend: Region
#   Values: Actual_Demand (Sum)
# Title: "Demand by Region"
#
# 4.5 QUARTERLY PERFORMANCE TABLE (Bottom right)
# ───────────────────────────────────────────────
# Click "Table" or "Matrix" visual
#   Rows: Quarter
#   Values: Total Revenue, Total Demand, FA%
# Title: "Quarterly Summary"


# =============================================================================
# STEP 5: BUILD PAGE 2 — SUPPLIER SCORECARD (20 minutes)
# =============================================================================
#
# Right-click the page tab at bottom → "New Page" → rename to "Supplier Scorecard"
#
# 5.1 SUPPLIER OTD BAR CHART (Top left)
# ──────────────────────────────────────
# Clustered Bar Chart
#   Y-axis: Supplier
#   X-axis: OTD Rate
# Add a "Constant Line" reference at 0.90 (90% target)
# Title: "On-Time Delivery Rate by Supplier"
#
# 5.2 SUPPLIER QUALITY BAR CHART (Top right)
# ───────────────────────────────────────────
# Clustered Bar Chart
#   Y-axis: Supplier
#   X-axis: Quality Rate
# Add constant line at 0.95 (95% target)
# Title: "Quality Pass Rate by Supplier"
#
# 5.3 LEAD TIME BOX (Middle)
# ──────────────────────────
# Table visual:
#   Rows: Supplier
#   Values: Lead_Time_Days (Average), On_Time_Delivery (Sum), Quality_Pass (Sum)
# Title: "Supplier Performance Detail"
#
# 5.4 SUPPLIER TREND (Bottom)
# ───────────────────────────
# Line Chart
#   X-axis: Date
#   Y-axis: OTD Rate
#   Legend: Supplier
# Title: "OTD Trend by Supplier Over Time"


# =============================================================================
# STEP 6: BUILD PAGE 3 — INVENTORY ANALYSIS (15 minutes)
# =============================================================================
#
# New page → rename to "Inventory"
#
# 6.1 INVENTORY LEVELS BY PRODUCT (Bar chart)
# ────────────────────────────────────────────
# Clustered Bar Chart
#   Y-axis: Product
#   X-axis: Inventory_End (Average)
# Title: "Average Inventory by Product"
#
# 6.2 INVENTORY vs DEMAND SCATTER (Scatter plot)
# ───────────────────────────────────────────────
# Scatter Chart
#   X-axis: Actual_Demand (Sum)
#   Y-axis: Inventory_End (Sum)
#   Details: Product
# Title: "Inventory vs Demand by Product"
#
# 6.3 SAFETY STOCK COVERAGE TABLE
# ────────────────────────────────
# Table visual:
#   Rows: Product, Region
#   Values: Safety_Stock (Sum), Actual_Demand (Sum), Inventory_End (Average)


# =============================================================================
# STEP 7: ADD SLICERS (FILTERS) — ALL PAGES (10 minutes)
# =============================================================================
#
# On EACH page, add slicers for interactive filtering:
#
# 1. Click "Slicer" from Visualizations
# 2. Drag "Year" to the slicer → appears as buttons [2023] [2024]
# 3. Add another slicer for "Region" → [North] [South] [East] [West]
# 4. Add another slicer for "Product" → dropdown list
# 5. Add another slicer for "Quarter" → buttons [Q1] [Q2] [Q3] [Q4]
#
# Place slicers at the top of each page.
# When a user clicks "North" → ALL visuals on the page filter to North only.
#
# To make slicers work ACROSS pages:
#   View ribbon → Sync Slicers → check the boxes for all pages


# =============================================================================
# STEP 8: FORMAT & POLISH (15 minutes)
# =============================================================================
#
# 8.1 THEME
#   View ribbon → Themes → choose a professional theme
#   Recommended: "Executive" or "Innovation" or custom with navy blue
#
# 8.2 TITLES
#   Add a text box at the top: "Supply Chain Dashboard — HPCL Analytics"
#   Font: 20pt, Bold, Navy blue
#
# 8.3 FORMATTING TIPS
#   - Right-click any visual → Format → Turn off unnecessary borders
#   - Use consistent colors across all visuals
#   - Align visuals using Format → Align
#   - Add data labels to bar charts (Format → Data labels → On)
#   - Set cards to show 1 decimal place for percentages
#
# 8.4 CONDITIONAL FORMATTING
#   For the supplier table:
#   Click the table → Format → Cell elements → Background color
#   → Based on field value → choose OTD Rate
#   → Color scale: Red (low) to Green (high)


# =============================================================================
# STEP 9: SAVE & EXPORT (5 minutes)
# =============================================================================
#
# 1. File → Save As → "Supply_Chain_Dashboard.pbix"
# 2. For screenshots: each page → File → Export → Export to PDF
#    OR use Windows Snipping Tool (Win+Shift+S) for each page
# 3. Save screenshots as:
#    - page1_executive_overview.png
#    - page2_supplier_scorecard.png
#    - page3_inventory_analysis.png
#
# FOR GITHUB: Upload the .pbix file + screenshots + README


# =============================================================================
# STEP 10: WHAT TO SAY IN INTERVIEWS
# =============================================================================
#
# "I built a 3-page Power BI dashboard for supply chain analytics:
#
#  Page 1 — Executive Overview: 5 KPI cards (Revenue, Demand, Forecast
#  Accuracy, OTD Rate, Quality), demand trend with actual vs forecast,
#  revenue by product, and regional demand distribution.
#
#  Page 2 — Supplier Scorecard: On-time delivery and quality pass rates
#  per supplier with targets, lead time analysis, and OTD trends over time.
#  Identified Supplier D as consistently below the 90% OTD target.
#
#  Page 3 — Inventory Analysis: Inventory levels by product, inventory
#  vs demand scatter to identify over/understocked items, and safety stock
#  coverage analysis.
#
#  All pages have interactive slicers for Year, Quarter, Region, and Product.
#  Conditional formatting highlights underperforming suppliers in red.
#
#  The data covers 8 petroleum products across 4 regions over 2 years —
#  similar to the analytics I did at HPCL managing a 180,000 MTPA facility."
