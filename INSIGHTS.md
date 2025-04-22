# 🌍 Global CO₂ Emissions Dashboard – Data Insights & Notes

This document serves as a read-only explanatory file accompanying the Power BI project titled **"Global CO₂ Emissions Dashboard"**. It summarizes the key **insights**, **data context**, **challenges**, and **design decisions** made during the development of the project.

---

## 📦 Data Sources
- **Our World in Data (OWID)**: Main dataset used for country-level and sector-wise CO₂ emissions.
- **cleaned_co2_data**: Maib dataset used (after clean and filtering)
- **Annual CO₂ Emissions by Region**
- **Per Capita CO₂ Emissions**
- **Annual % Change in CO₂ Emissions**
- **CO₂ Emissions from Fossil Fuels and Land Use**
- **Share of Global CO₂ Emissions**

All files were cleaned, merged, and transformed using **Python (Google Colab)** and **Power BI Power Query Editor**.

---

## 🔍 Key Metrics & KPIs
- **Total CO₂ Emissions (Latest Year)**
- **% Change from Previous Year**
- **Global Per Capita Emissions**
- **Top Emitter (Latest Year)**

These KPIs were highlighted using **custom cards** to immediately give viewers the most crucial info.

---

## 📈 Visualizations
- **Time Series Line Chart**: Shows emission trends over time globally and for selected countries.
- **Donot Chart**: Distribution of emissions by economic sector (e.g., Energy, Transport, Agriculture).
- **Geo Map**: Country-wise emissions with interactive tooltips and a custom color theme.
- **Bar Charts**: Top emitters, % change by region, and sector-wise contribution.

---

## 🌐 Map Customization
- **Map View Tweaks**:
  - Custom legend placement
  - Dark navy theme matching dashboard palette

---

## 🛠 Key Features
- **Slicers**:
  - By Country / Region
  - By Sector (for pie charts)
  - By Year (timeline navigation)
- **DAX Measures**:
  - Created for dynamic filtering and visual-specific aggregations
- **Dynamic Tooltips**:
  - Additional insights revealed on hover across charts

---

## 💡 Insights
- CO₂ emissions have consistently risen over the decades with notable spikes post-industrial revolution.
- The top five countries contribute more than 50% of total global emissions.
- Transport and energy remain the dominant sectors contributing to annual CO₂ emissions.
- Per capita emissions highlight inequality — smaller populations can have disproportionately large footprints.

---

## ⚠️ Challenges & Considerations
- Handling missing values for earlier years in regional data
- Matching inconsistent country names across different datasets
- Balancing aesthetics with data density in the visual layout

---

## 📌 Goal
To **educate**, **inform**, and **inspire** action through transparent, accessible data storytelling — and showcase proficiency in data visualization using real-world environmental data.

---

✅ _Project by Vinit Singh Pathir_  
🔗 View the dashboard & full source code on GitHub.

