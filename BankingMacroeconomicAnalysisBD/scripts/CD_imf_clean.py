import pandas as pd
import os

raw_file = "../data_raw/IMF-FSI-A.BD.FSCD_PT.csv"
clean_dir = "../data_clean"
os.makedirs(clean_dir, exist_ok=True)
clean_file = os.path.join(clean_dir, "fsi_deposits_to_loans.csv")

df = pd.read_csv(raw_file)

# Rename columns
df = df.rename(columns={
    "period": "year",
    df.columns[1]: "value"
})

# Add indicator
df["indicator"] = "Deposits_to_loans_pct"

# Ensure types
df["year"] = df["year"].astype(int)
df["value"] = pd.to_numeric(df["value"], errors='coerce')

# Reorder
df = df[["indicator", "year", "value"]]

df.to_csv(clean_file, index=False)
print(f"Cleaned CSV saved to {clean_file}")

