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
#ambda x: x.strip(): This is a small, anonymous function that runs on every column name.
#   x: Represents the current column name.
#   .strip(): Removes any leading or trailing whitespace (spaces, tabs, newlines).

expected_cols = ['Country', 'Year', 'GDP_per_capita']

# Action: Selects and reorders the columns based on the list above.
# Logic: Pandas takes the list expected_cols and filters the DataFrame to match it.
# It tells Pandas: "I want these specific columns, in this specific order."It matches the strings in expected_cols against the actual column headers in the DataFrame.
# If a column name in expected_cols does not exist in the DataFrame, Pandas will raise a KeyError.
df = df[expected_cols]

# --- Ensure correct types ---
df['Year'] = df['Year'].astype(int)
df['GDP_per_capita'] = pd.to_numeric(df['GDP_per_capita'], errors='coerce')
# 'raise' (Default) -- Crash. Stops the program and raises a ValueError.
# 'ignore' -- Skip. Returns the original data unchanged (still a string).
# 'coerce' -- Force. Converts invalid data to NaN (Not a Number).

# --- Sort data ---
df = df.sort_values(by=['Country', 'Year'])

# --- Save cleaned CSV ---
df.to_csv(output_file, index=False)
print(f"Cleaned data saved to {os.path.abspath(output_file)}")

