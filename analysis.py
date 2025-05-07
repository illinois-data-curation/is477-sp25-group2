import matplotlib.pyplot as plt
import pandas as pd

countries_costs_df = pd.read_csv("countries_costs_cleaned.csv")
wb_indicators_df = pd.read_csv("wb_indicators_cleaned.csv")

wb_indicators_df["indicators indexed"] = wb_indicators_df["total fertility rate"]*10+wb_indicators_df["total life expectancy"]+wb_indicators_df["food production index"]
all_data = pd.merge(countries_costs_df, wb_indicators_df, on='country', how='inner')

plt.figure()
plt.plot(all_data['totaled costs'], all_data['indicators indexed'], marker='o')
plt.title("All totaled cost of living compared against QoL indicators")
plt.ylabel("indicators indexed")
plt.xlabel("totaled costs")
plt.grid(True)
plt.savefig("index_to_costs.png", dpi=300, bbox_inches='tight')

no_outliers_costs_df = all_data.sort_values('totaled costs', ascending=False).iloc[3:]

plt.figure()
plt.plot(no_outliers_costs_df['totaled costs'], no_outliers_costs_df['indicators indexed'], marker='o')
plt.title("Totaled cost of living compared against QoL indicators (outliers removed)")
plt.ylabel("indicators indexed")
plt.xlabel("totaled costs")
plt.grid(True)
plt.savefig("no_outliers_index_to_costs.png", dpi=300, bbox_inches='tight')

#individual variables
plt.figure()
plt.plot(no_outliers_costs_df['totaled costs'], no_outliers_costs_df['total fertility rate'], marker='o')
plt.title("Totaled cost of living compared against total fertility rate (outliers removed)")
plt.ylabel("indicators indexed")
plt.xlabel("totaled costs")
plt.grid(True)
plt.savefig("fertility_rate_to_costs.png", dpi=300, bbox_inches='tight')

plt.figure()
plt.plot(no_outliers_costs_df['totaled costs'], no_outliers_costs_df['total life expectancy'], marker='o')
plt.title("Totaled cost of living compared against total life expectancy (outliers removed)")
plt.ylabel("indicators indexed")
plt.xlabel("totaled costs")
plt.grid(True)
plt.savefig("life_expectancy_to_costs.png", dpi=300, bbox_inches='tight')

plt.figure()
plt.plot(no_outliers_costs_df['totaled costs'], no_outliers_costs_df['food production index'], marker='o')
plt.title("Totaled cost of living compared against the food production index (outliers removed)")
plt.ylabel("indicators indexed")
plt.xlabel("totaled costs")
plt.grid(True)
plt.savefig("food_production_index_to_costs.png", dpi=300, bbox_inches='tight')
