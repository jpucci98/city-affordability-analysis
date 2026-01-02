import pandas as pd
import matplotlib.pyplot as plt
import os

# Load data
df = pd.read_csv("city_data.csv")

# Create output folder for figures
os.makedirs("figures", exist_ok=True)

# Calculate rent-to-income ratio
df["Rent_to_Income_Ratio"] = df["Median_Annual_Rent"] / df["Median_Annual_Wage"]

# Rank cities by affordability
df_sorted = df.sort_values("Rent_to_Income_Ratio")
print("\nCity Affordability Ranking (Lower = More Affordable):\n")
print(df_sorted[["City", "Rent_to_Income_Ratio"]])

# -----------------------
# Scatter plot: Wage vs Rent
plt.figure()
plt.scatter(df["Median_Annual_Wage"], df["Median_Annual_Rent"])
for i, city in enumerate(df["City"]):
    plt.annotate(city, (df["Median_Annual_Wage"][i], df["Median_Annual_Rent"][i]))
plt.xlabel("Median Annual Wage ($)")
plt.ylabel("Median Annual Rent ($)")
plt.title("Median Rent vs Median Wage by City")
plt.tight_layout()
plt.savefig("figures/rent_vs_income.png")
plt.show()

# -----------------------
# Bar chart: Affordability ranking
plt.figure()
plt.barh(df_sorted["City"], df_sorted["Rent_to_Income_Ratio"])
plt.xlabel("Rent-to-Income Ratio")
plt.title("City Affordability Ranking")
plt.tight_layout()
plt.savefig("figures/affordability_rank.png")
plt.show()

