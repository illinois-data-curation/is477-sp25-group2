rule all:
    input:
        "countries_costs_cleaned.csv", 
        "wb_indicators_cleaned.csv",
        "index_to_costs.png", 
        "no_outliers_index_to_costs.png",
        "fertility_rate_to_costs.png",
        "life_expectancy_to_costs.png", 
        "food_production_index_to_costs.png"
  

rule clean_db:
  input: "inputs/countries_col.csv", "inputs/countries_dict.csv", "inputs/world_bank_indicators.csv"
  output: "countries_costs_cleaned.csv", "wb_indicators_cleaned.csv"
  shell: "python inputs/cleanData.py"

rule analyze:
  input: "countries_costs_cleaned.db", "wb_indicators_cleaned.csv"
  output: "index_to_costs.png", "no_outliers_index_to_costs.png", "fertility_rate_to_costs.png", "life_expectancy_to_costs.png", "food_production_index_to_costs.png"
  shell: "python analysis.py"



  