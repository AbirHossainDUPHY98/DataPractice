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
# This url is the standart for REST APIs . Like the format, per_page part.
url = f"http://api.worldbank.org/v2/country/{';'.join(countries)}/indicator/{indicator}?date={start_year}:{end_year}&format=json&per_page=1000"

print("Fetching data from World Bank API...")
response = requests.get(url)
data = response.json()

# The first element is metadata, second element is the data
records = []   # list of dictionaries
for entry in data[1]:
    country = entry["country"]["value"]
    year = entry["date"]
    value = entry["value"]
    records.append({"Country": country, "Year": int(year), "GDP_per_capita": value})
# entry:raw api data: {
#    "country": {"id": "US", "value": "United States"},
#    "date": "2020",       # Note: This is a string
#    "value": 63543.58     # This is a float}
# {"Country": "United States",
#    "Year": 2020,         # Note: Now an integer
#    "GDP_per_capita": 63543.58}

# --- Convert to DataFrame ---
# DataFrame is a programmable Excel sheet or a SQL table
# It allows you to perform complex operations (sorting, filtering, math)                                                                                much faster than using standard Python lists.
df = pd.DataFrame(records)

# --- Sort by country and year ---
df = df.sort_values(by=["Country", "Year"])

# --- Save to CSV --- Saves the DataFrame to a CSV (Comma Separated Values) file.
df.to_csv(output_file, index=False)  # Pandas DataFrames have a hidden row number index (0, 1, 2, 3...).
print(f"Data saved to {output_file}")

