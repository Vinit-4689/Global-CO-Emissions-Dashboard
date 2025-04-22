import pandas as pd

# Load the uploaded CO₂ dataset
file_path = "/mnt/data/owid-co2-data.csv"
df = pd.read_csv(file_path)

# Display basic info and preview of the dataset
df_info = df.info()
df_preview = df.head(5)
df_columns = df.columns.tolist()

df_info, df_columns, df_preview

# Reload the main OWID dataset for CO₂ emissions
df = pd.read_csv("/mnt/data/owid-co2-data.csv")

# Filter to relevant columns
columns_to_keep = [
    'iso_code', 'country', 'year', 'population', 'gdp', 'co2', 'co2_per_capita',
    'co2_per_gdp', 'cumulative_co2', 'coal_co2', 'oil_co2', 'gas_co2',
    'cement_co2', 'flaring_co2', 'other_industry_co2', 'share_global_co2',
    'temperature_change_from_co2'
]
df_clean = df[columns_to_keep]

# Remove aggregates like 'World', 'Asia', 'Europe' etc.
aggregates = ['World', 'Asia', 'Africa', 'Europe', 'European Union', 'North America',
              'South America', 'Oceania', 'International transport']
df_clean = df_clean[~df_clean['country'].isin(aggregates)]

# Keep data only from 1990 onward
df_clean = df_clean[df_clean['year'] >= 1990]

# Drop rows with no CO2 values
df_clean = df_clean[df_clean['co2'].notna()]

# Preview cleaned dataset shape and first few rows
df_clean.shape, df_clean.head(3)

