#!/usr/bin/env python3
import pandas as pd
import os

# --- Input and output files ---
input_file = "GDP_per_capita_BD_IND_PAK_2005_2025.csv"  # raw downloaded file
output_file = "GDP_per_capita_BD_IND_PAK_2005_2025_clean.csv"

# --- Read CSV ---
df = pd.read_csv(input_file)

# --- Rename columns to clean format ---
# Keep only relevant columns
df = df.rename(columns=lambda x: x.strip())  # remove any leading/trailing spaces
expected_cols = ['Country', 'Year', 'GDP_per_capita']
df = df[expected_cols]

# --- Ensure correct types ---
df['Year'] = df['Year'].astype(int)
df['GDP_per_capita'] = pd.to_numeric(df['GDP_per_capita'], errors='coerce')

# --- Sort data ---
df = df.sort_values(by=['Country', 'Year'])

# --- Save cleaned CSV ---
df.to_csv(output_file, index=False)
print(f"Cleaned data saved to {os.path.abspath(output_file)}")

