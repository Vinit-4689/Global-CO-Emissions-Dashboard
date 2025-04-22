# 🌍 Global CO₂ Emissions Dashboard - Power BI

This project is a fully interactive Power BI dashboard that visualizes and analyzes **global CO₂ emissions** trends, sources, and impacts. It combines rich datasets from Our World in Data to deliver actionable insights through cards, maps, slicers, pie charts, and dynamic KPIs.

---

## 📊 Features

- **Total Global Emissions (Latest Year)**
- **Year-over-Year % Change**
- **Global Per Capita Emissions**
- **Top Emitter (Latest Year)**
- **Interactive Map by Country**
- **CO₂ Emissions by Sector (Coal, Oil, Gas, etc.)**
- **Dynamic Pie Chart (with Sector Slicer)**
- **Trends Over Time: Line Graph**

---

## 🗂️ Datasets Used

1. `owid-co2-data.csv` — Core dataset containing historical and sectoral CO₂ data
2. `co2-fossil-plus-land-use.csv` — To evaluate net fossil + land-use emissions
3. `annual-co2-emissions-per-country.csv` — For mapping and country-wise analysis
4. `annual-share-of-co2-emissions.csv` — To calculate % share by country
5. `annual-co-emissions-by-region.csv` — Regional trend analysis
6. `change-co2-annual-pct.csv` — For year-over-year change visualization
7. `cleaned_co2_data.csv` — Final data used 
---

## 🛠️ Key Power BI Elements

### Cards / KPIs:
- **Global CO₂ Emissions (Mt)**
- **% Change from Previous Year**
- **Emissions Per Capita (t/person)**
- **Top Emitter Country**

### Map:
- Used **Filled Map** visual
- Color-coded by total emissions
- Country column set to **"Geography" data category**

### Donot Chart:
- Displays emissions breakdown by sector (coal, gas, oil, cement, flaring)
- Driven by a separate dynamic sector table using DAX or Power Query

### Sector Slicer:
```DAX
Sector Table =
DATATABLE(
    "Sector", STRING,
    {
        {"Coal"},
        {"Gas"},
        {"Oil"},
        {"Cement"},
        {"Flaring"}
    }
)
```

---

## 📐 Visual Design

- **Canvas Size:** 1280x720 (16:9 Ratio)
- **Background Color:** `#0A122A` (Dark Navy Blue)
- **Legend Inside Map:** Set via visual formatting


---

## 🖼️ Screenshot
(![image](https://github.com/user-attachments/assets/01df6533-5d54-4c1e-92bf-db1c7a1064d3)


---

## 📁 Folder Structure
```
├── cleaned_data/                  # Cleaned datasets for upload
├── visuals/                       # Screenshots or sample backgrounds
├── PowerBI_Project.pbix          # Final Power BI dashboard file
├── README.md                     # Project documentation
├── INSIGHTS.md                     # insights found from the datasets
```

---

## ✅ Status
- [x] Data Cleaning
- [x] Background Design & Canvas Setup
- [x] Card Visuals & KPIs
- [x] Pie Chart by Sector
- [x] Map with Country Emissions
- [x] Trend Lines
- [x] Sector Slicer Working

---

## 🧠 Inspired By
- [Our World in Data](https://ourworldindata.org/co2-and-other-greenhouse-gas-emissions)
- [Power BI Design Best Practices](https://learn.microsoft.com/en-us/power-bi/)

---

## 📌 Notes
- Ensure country column is categorized as **Geography**
- Relationship must be built between Sector Table and CO₂ table for slicer to work

---

## 🧪 Bonus Projects
Also check out the repository for our other project: [🎰 Multi-Armed Bandit Algorithms](https://github.com/Vinit-4689/Multi-Armed-Bandit)

---

## 🙌 Author
**Vinit Singh Pathir** — [Blackout | Data Science Portfolio](https://your-portfolio-link)

> Built with 💡 in Power BI to visualize our planet's emissions story.

