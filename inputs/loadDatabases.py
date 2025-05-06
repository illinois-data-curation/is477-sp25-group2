import pandas as pd

countries_costs = pd.read_csv("inputs/countries_col.csv")
wb_indicators = pd.read_csv("inputs/wb_indicators.csv")


ccosts_cols = ["country", "x1", "x42", "x52", "x54"]
countries_costs = countries_costs[[col for col in ccosts_cols if col in countries_costs.columns]]
countries_costs.columns = countries_costs.columns.str.strip()
countries_costs.dropna()

countries_costs.rename(columns={"x1": "inexpensive meal"}, inplace=True)
countries_costs.rename(columns={"x42": "primary school enrollment"}, inplace=True)
countries_costs.rename(columns={"x52": "apt/sqm in city"}, inplace=True)
countries_costs.rename(columns={"x54": "avg monthly salary"}, inplace=True)


wb_ind_cols = ["year", 
               "country", 
               "Fertility rate, total (births per woman)", 
               "Life expectancy at birth, total (years)", 
               "School enrollment, primary (% net)", 
               "Poverty headcount ratio at national poverty lines (% of population)"]

wb_indicators = wb_indicators[wb_ind_cols]
wb_indicators.columns = wb_indicators.columns.str.strip()

wb_indicators.rename(columns={"Fertility rate, total (births per woman)": "total fertility rate"}, inplace=True)
wb_indicators.rename(columns={"Life expectancy at birth, total (years)": "total life expectancy"}, inplace=True)
wb_indicators.rename(columns={"School enrollment, primary (% net)": "net primary school enrollment"}, inplace=True)
wb_indicators.rename(columns={"Poverty headcount ratio at national poverty lines (% of population)": "poverty ratio"}, inplace=True)

#wb_indicators = wb_indicators[wb_indicators["year"] == "2022"]
#wb_indicators.drop("year", axis=1, inplace=True)

countries_costs.to_csv("countries_costs_cleaned.csv", index=False)
wb_indicators.to_csv("wb_indicators_cleaned.csv", index=False)
## import and clean both
## import and add column names
## countries 2022
##cost of living: x54, x52, x42, x1
## indicators: fertility rate, life expectancy, school enrollment, poverty headcount 2.15 a day
## make an index of each and compare against each other
## snakemake file

