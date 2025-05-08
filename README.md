# Title: Impact of Cost of Living on Social Metrics Across the World

# Link to archival record: Link to the archived copy of your project, including persistent identifier.

# Contributors: Bulleted list of contributors (with optional ORCIDs).
- Angela Jing: 0009-0001-0231-7402
- Shawna Ye: 0009-0001-4840-3883

# Summary: [500-1000 words] Description of your project, motivation, research question(s), and any findings.
Our project looks at two datasets: a 2022 cost of living across global cities dataset and economic, social, demographic, and environmental indicators from the World Bank. By analyzing
these datasets, we hope to discover where there's a relationship between the total cost of living metrics (which consist of food prices, housing costs, average salary, etc.) and social indicators in the US (school enrollment rates, infant mortality rates, poverty headcount, etc.). For example, if a country has a higher cost of living, are social indicators higher due to increased access to better services and infrastructure? We were motivated to research this topic due to personal curiosity and practicality. As young adults about to enter the workforce and manage our own living expenses, we have become more aware of how cost of living not only affects individual liestyles but also broader social outcomes within society. However, some major cities such as New York City or San Francisco offer better public services and amenities but are also known for their social inequalities. Our research
question is: For countries across the world, what is the relationship between cost of living in their major cities and overall social indicators? By examining this question, we hope to look at whether total cost of living metrics (an
inexpensive meal at a restaurant, monthly cost of preschool/kindergarten for one child, price per square meter to buy an apartment in the city center, average monthly net salary) have some sort of impact or relationship
with social wellness metrics (fertility rate, life expectancy, school enrollment, poverty headcount). 

Based on our findings, we found that there is a positive correlation between higher cost of living and life expectancy. However, there is a slight negative correlation between total fertility rate and higher cost of living. We also made an overall index to summarize the indicators by scaling each indicator similarly, as well as comparing individual indicators such as the food production index. However, we found the relation between the overall index and food production index with the cost of living to be inconclusive. Overall, these results seem to suggest that a higher cost of living is often associated with longer life expectancy. This could be due to better healthcare systems, infrastructure, and services in more expensive cities. On the other hand, the negative correlation with fertility rate may showcase broader socioeconomic trends, such as delayed family planning and higher child-rearing costs in more developed urban areas. Based on our background knowledge, we have also heard that fertility rates tend to be lower in more developed nations. Additionally, the inconclusive findings regarding the food production index and the overall index suggest that not all social indicators are directly linked to cost of living. For example, while some aspects of well-being (like health and education) may be better in wealthier cities and countries, other factors influencing social metrics could be attributed to
non-cost-of-living related factors such as national policies, cultural factors, or resource distributions. The results are in line with our initial expectations prior to starting the analysis, and we weren't too surprised by the results.

# Data profile:
We are using 2 datasets from Kaggle: Global Cost of Living (https://www.kaggle.com/datasets/mvieira101/global-cost-of-living?select=cost-of-living_v2.csv) and World Bank Indicators Dataset (https://www.kaggle.com/datasets/georgejdinicola/world-bank-indicators).

For the Global Cost of Living dataset, this dataset features information scraped from Numbeo's website (per Numbeo's website: "Numbeo is the world's largest cost of living database and a crowdsourced global resource for quality of life data") on the
cost of living from approximately 5000 cities across the world. The dataset features 58 columns that encompass a variety of metrics, everything from restaruant costs; food prices (different drinks such as milk or soda, grains, poultry, produce, and more); transportation-related
costs such as fuel costs and public transport ticket prices; amenities such as schools, internet costs, fitness club fees, movie price tickets; educational costs; apartment housing prices; and salaries. Thus, we chose this dataset because it offers a comprehensive
look into the affordability and economic accessibility of urban life around the globe. This dataset was last updated on 12/3/2022, and we are using the latest version. The dataset features 4956 rows and 117 columns, with 22% of the cities represented being American cities, 
roughly 4% from Italy, and the remaining ~75% from other places around the world. We also chose this dataset because it has a 9.71 usability score on Kaggle, with 100% ratings for completeness, credibility, and compatibility. The licensing on this dataset is CC0: Public Domain, which allows unrestricted use, distribution, and modification for research, analysis, and public dissemination. According to the Numbeo website, its terms of use states that its data is free for personal and academic use, as long as appropriate credit is given. However, automated data collection via scraping is prohibited unless authorized. For more information, please visit https://www.numbeo.com/common/terms_of_use.jsp.

The second dataset is from the World Bank and covers a range of global indicators spanning from 1960 to 2023. These indicators include economic metrics (GDP growth, merchandise trade, gross capital formation, etc.), environmental metrics (forest area, renewable energy consumption), 
demographic metrics (urban population, life expectancy, net migration), and the one type of metric we're focusing on: social metrics, which encompasses topics such as school enrollment, mortality rates, and more. This dataset was selected because it's not only comprehensive but also from an extremely reliable source; The World Bank is an international development organization owned by 187 countries that provides assistance to developing countries to reduce poverty and promote sustainable development goals (SDGs). The dataset has roughly 16960 rows and and 215 columns, and it has a 9.41 usability score with 100% ratings for completeness and credibility, and a 75% rating for compatibility. The licensing on this dataset is Creative Commons Attribution 4.0 International (CC BY 4.0), which means that users are free to share, adapt and build upon data fora variety of purposes as long as they give appropriate credit to the World Bank and note any changes made. Additionally, according to the World Bank website, the terms of use also state that some of its "datasets may include third-party content with separate terms, which must be followed ... Users may not imply World Bank endorsement or use its name, logo, or branding without written permission." For more information on the World Bank's terms of use, please visit https://www.worldbank.org/en/about/legal/terms-of-use-for-datasets. 

# Findings: [~500 words] Description of any findings including numeric results and/or visualizations.
<<<<<<< HEAD
In this analysis, we explored the relationship between the cost of living across different global locations and various socioeconomic indicators. Specifically, we compiled cost of living data from 4,816 cities across 249 countries and examined how these costs might be influenced by three key indicators sourced from the World Bank: total fertility rate, life expectancy at birth, and food production index. These indicators represent demographic, health, and agricultural productivity dimensions of a country, respectively.


To compare these diverse indicators on a similar scale, we created a composite index by standardizing the values of each indicator and weighing them approximately equally. This total index allowed us to perform more direct comparisons between the combined socioeconomic conditions of a country and its cost of living. The goal was to identify whether there were any consistent, interpretable correlations between the socioeconomic profile of a country and how expensive it is to live there.


The findings revealed some interesting patterns. First, the composite total index (which includes all three indicators) did not show a strong or consistent correlation with the cost of living. This suggests that when considered together, these indicators do not clearly explain variations in how much it costs to live in different cities or countries.


However, when we looked at individual indicators, clearer relationships began to emerge. One of the most noticeable findings was that life expectancy tends to be positively correlated with the cost of living. This means that countries where people live longer also tend to be more expensive. This relationship could imply that higher living standards and better healthcare systems, which contribute to longer life spans, also drive up the cost of living.


On the other hand, the total fertility rate appeared to have a slightly negative correlation with cost of living. This suggests that in countries where people have more children on average, the cost of living is somewhat lower. While the trend isn’t dramatically strong, it might reflect that higher fertility rates are more common in developing countries, which typically have lower living costs compared to developed nations.


Lastly, the food production index did not show a clear or consistent correlation with the cost of living. This indicates that the amount of food a country produces relative to a base year doesn’t seem to strongly impact how expensive it is to live there. There could be many reasons for this, such as the influence of global food trade, distribution inefficiencies, or subsidies that decouple domestic food production from consumer prices.


Overall, the analysis shows that while some socioeconomic indicators—particularly life expectancy—are related to the cost of living, others are either weakly correlated or not at all. It highlights how complex and multi-dimensional the drivers of living costs are, and that while demographic and economic data offer valuable insights, they do not paint a full picture on their own. Future research could incorporate more variables such as income levels, education, urbanization rates, or government policy to better understand what influences cost of living globally.
=======
>>>>>>> d4ac99301fc9e29e9bc9ec83cd956a4c5561b546

# Future work: [~500-1000 words] Brief discussion of any lessons learned and potential future work.
Through this project, we've gained valuable insights into the relationship between cost of living and social indicators for different countries across the world. However, we also encountered several challenges and questions that open up potential for future research.

One lesson we've learned is the importance of scaling data across multiple datasets. In our project, the cost of living data was collected at the city level, while the indicators from the World Bank were reported at the country level. This initially posed challenges when trying to determine the relationships between the cost of living metrics and the social indicators. For example, New York City's cost of living metrics may not accurately reflect the cost of living metrics across the entire United States. Due to this limitation, we had to aggregate cities by country so that the average of the metrics could hopefully provide a more clear image of the country. To translate this into future work, we might seek out a cost-of-living dataset that features data at a country-level, or instead use a social metrics dataset that operates at a city-level. Doing so could prevent potential mismatches, allowing us to draw more clear conclusions about causality or correlation. 

Another lesson we learned is that a simple correlation analysis might not be enough to understand the complexity of the relationship between cost of living and social metrics. As some of our results are inconclusive, in future work we could use regression models or machine learning techniques (such as clustering) to uncover more hidden patterns. Such models could help control confounding variables that affect social indicators such as population density, GDP per capita, etc. 

We also recognize that our cost of living dataset may be limited as it only features one year, which hampers our ability to detect trends. In the future, we could use datasets that span across multiple years, which would allow us to better analyze the relationship between cost of living and social indicators over time. This could help determine whether observed relationships are stable, increasing, or diminishing. For instance, cost of living metrics have been especially subject to fluctuations after the pandemic because of supply chain disruptions, inflation, shifting labor markets, and changing patterns in housing and food costs. With multi-year data, we could explore lagged effects, such as seeing whether a sharp increase in cost of living in one year leads to measurable changes in social indicators in the following years.

Lastly, we see immense potential in expanding the scope of our analysis beyond social indicators. For this project, we decided to look only at social indicators because that's what interested us the most, but the World Bank dataset also includes economic, environmental, and demographic metrics that we could use in future studies. This would help create a more holistic image of the relationship between wellbeing metrics and cost of living metrics. For instance, economic indicators such as GDP per capita, unemployment rates, inflation, or income inequality could provide deeper insight into whether high costs of living is associated with economic prosperity, and environmental metrics (such as CO2 emissions, access to clean water, urban air quality) could reveal how environmental sustainability relates to affordability and quality of life. Demographic variables like population growth rate, urbanization levels, or median age could also shed light factors that may influence both cost of living and societal wellbeing. Thus, while our current project offers a focused look at the intersection of cost of living and social wellness, future work that expands into economic, environmental, and demographic data could paint a more interconnected picture of global living conditions.

In conclusion, this project served as a starting point for understanding how cost of living may relate to social indicators. While our results provide some insight, they also highlight the complexity of these relationships and the need for future analysis to more precisely capture how cost-of-living conditions intersect with well-being in cities across the world.

# Reproducing: Sequence of steps required for someone else to reproduce your results.
1.Import the Global Indicators dataset, Countries Cost of Living dataset, and Country Dictionary CSVs from Kaggle.

2.Clean all datasets by removing null values, trimming trailing whitespaces, and standardizing capitalization.

3.From the Global Indicators dataset, extract relevant columns (e.g., fertility rate, life expectancy, food production index).

4.In the Countries Cost of Living dataset, calculate and create a new column labeled "totaled costs" to represent total living expenses.

5.Construct a composite "indicators indexed" column by weighting each global indicator approximately equally.

6.In analysis.py, merge datasets using country names as the primary key.

7.Visualize and analyze the relationship between each global indicator, the composite index, and "totaled costs".

# References: Formatted citations for any papers, datasets, or software used in your project. We used ACM formatting
- Human Rights Watch. 2022. What COVID teaches us about the cost-of-living crisis. https://www.hrw.org/news/2022/12/20/what-covid-teaches-us-about-cost-living-crisis. Accessed May 7, 2025.
- Numbeo. 2025. Cost of Living. Numbeo. https://www.numbeo.com/cost-of-living/. Accessed May 7, 2025.
- The World Bank. 2025. *World Development Indicators*. World Bank Open Data. https://databank.worldbank.org/source/world-development-indicators. Accessed May 7, 2025.
- Vieira, M. 2022. Global Cost of Living. Kaggle. https://www.kaggle.com/datasets/mvieira101/global-cost-of-living/data. Accessed May 7, 2025.
