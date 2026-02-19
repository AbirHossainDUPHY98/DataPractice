import pandas as pd
import os

# Paths
raw_file = "../data_raw/IMF-FSI-A.BD.FSGDLD_XDC.csv"
clean_dir = "../data_clean"
os.makedirs(clean_dir, exist_ok=True)
clean_file = os.path.join(clean_dir, "fsi_loans_domestic.csv")

# Read CSV
df = pd.read_csv(raw_file)

# Rename columns
df = df.rename(columns={
    "period": "year",
    df.columns[1]: "value"  # the second column has the messy header
})

# Add indicator column
df["indicator"] = "Loans_to_domestic_economy_million_BDT"

# Ensure correct types
df["year"] = df["year"].astype(int)
df["value"] = pd.to_numeric(df["value"], errors='coerce')  # invalid → NaN

# Reorder columns
df = df[["indicator", "year", "value"]]

# Save cleaned CSV
df.to_csv(clean_file, index=False)
print(f"Cleaned CSV saved to {clean_file}")

