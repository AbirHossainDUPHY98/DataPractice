#!/usr/bin/env python3
import requests
import pandas as pd

# --- Parameters ---
countries = ["BGD", "IND", "PAK"]  # Bangladesh, India, Pakistan
indicator = "NY.GDP.PCAP.CD"       # GDP per capita (current US$)
start_year = 2005
end_year = 2025
output_file = "GDP_per_capita_BD_IND_PAK_2005_2025.csv"

# --- Build API URL ---
# Example API format:
# http://api.worldbank.org/v2/country/BGD;IND;PAK/indicator/NY.GDP.PCAP.CD?date=2005:2025&format=json&per_page=1000
url = f"http://api.worldbank.org/v2/country/{';'.join(countries)}/indicator/{indicator}?date={start_year}:{end_year}&format=json&per_page=1000"

print("Fetching data from World Bank API...")
response = requests.get(url)
data = response.json()

# --- Parse JSON ---
# The first element is metadata, second element is the data
records = []
for entry in data[1]:
    country = entry["country"]["value"]
    year = entry["date"]
    value = entry["value"]
    records.append({"Country": country, "Year": int(year), "GDP_per_capita": value})

# --- Convert to DataFrame ---
df = pd.DataFrame(records)

# --- Sort by country and year ---
df = df.sort_values(by=["Country", "Year"])

# --- Save to CSV ---
df.to_csv(output_file, index=False)
print(f"Data saved to {output_file}")

