import pandas as pd
import numpy as np
import os

# Paths
raw_file = "../data_raw/world_bank1.csv"
clean_dir = "../data_clean"
os.makedirs(clean_dir, exist_ok=True)
clean_file = os.path.join(clean_dir, "world_bank1_clean.csv")

# Read CSV
df = pd.read_csv(raw_file)

# Drop completely empty rows (footer info)
df = df.dropna(how='all')

# Keep only Bangladesh
df = df[df['Country Name'] == 'Bangladesh']

# Select columns: Series Name + year columns
year_cols = [c for c in df.columns if '[YR' in c]
df = df[['Series Name'] + year_cols]

# Melt to long format
df_long = df.melt(id_vars=['Series Name'], value_vars=year_cols,
                  var_name='year', value_name='value')

# Clean year column: remove ' [YRxxxx]' → int
df_long['year'] = df_long['year'].str.extract(r'\[YR(\d+)\]')[0].astype(int)

# Clean value column: replace '..' → NaN and convert to float
df_long['value'] = df_long['value'].replace('..', np.nan).astype(float)

# Optional: simplify Series Name to snake_case
df_long['series_name'] = df_long['Series Name'].str.lower().str.replace(r'[^a-z0-9]+', '_', regex=True)

# Drop original Series Name
df_long = df_long.drop(columns=['Series Name'])

# Save cleaned CSV
df_long.to_csv(clean_file, index=False)
print(f"Cleaned World Bank CSV saved to {clean_file}")

