import pandas as pd
import matplotlib.pyplot as plt
import os
df = pd.read_csv("unemployed_rate.csv")
# print(df.head())

plt.figure(figsize=(10,8))   # width x height in inches
plt.plot(df['year'], df['value'], marker='o', linestyle='-', color='blue')
plt.title("Unemployment Rate Over Years")  # title of the plot
plt.xlabel("Year")            # x-axis label
plt.ylabel("Unemployment Rate")           # y-axis label
plt.grid(True)                # optional grid for easier reading
plt.savefig("unemployment_rate.png")
plt.show()  # displays the plot

plt.figure(figsize=(10,8))   # width x height in inches
plt.plot(df['year'], df['change_per_year'], marker='o', linestyle='-', color='red')
plt.title("Change Of Unemployement Rate Over Years")  # title of the plot
plt.xlabel("Year")            # x-axis label
plt.ylabel("Change of unemployment rate")           # y-axis label
plt.grid(True)                # optional grid for easier reading
plt.savefig("Change_of_unemployment_rate.png")
plt.show()  # displays the plot


