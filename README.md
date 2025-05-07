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

# Future work: [~500-1000 words] Brief discussion of any lessons learned and potential future work.
Through this project, we've gained valuable insights into the relationship between cost of living and social indicators for different countries across the world. However, we also encountered several challenges and questions that open up potential for future research.

One lesson we'ved learned is the importance of scaling data across multiple datasets. In our project, the cost of living data was collected at the city level, while the indicators from the World Bank were reported at the country level. This initially posed challenges when trying to determine the relationships between the cost of living metrics and the social indicators. For example, New York City's cost of living metrics may not accurately reflect the cost of living metrics across the entire United States. Due to this limitation, we had to aggregate cities by country and hope that this provided a #######################This mismatch presented challenges when trying to draw clear conclusions about causality or correlation. For instance, New York City’s cost of living may not accurately reflect the average social conditions across the entire United States. This limitation taught us to be cautious about interpreting results without considering the granularity of our data. In future work, we aim to seek out or construct datasets that align city-level cost of living with city-level social indicators, perhaps using regional health departments, census data, or city-specific surveys.

Another challenge we faced was selecting and scaling diverse indicators. Social wellness metrics like life expectancy, fertility rate, school enrollment, and poverty headcount vary significantly in their nature, scale, and directionality. For example, higher values in life expectancy are positive, while higher fertility rates may be contextually neutral or negative depending on societal norms. To address this, we created an overall index by normalizing the indicators, but this process involved subjective decisions on weighting and transformation methods. A more sophisticated approach in future work would involve the use of dimensionality reduction techniques such as Principal Component Analysis (PCA) to construct indices in a more statistically grounded way.

In addition, while we found some meaningful correlations (such as the positive relationship between cost of living and life expectancy), many results were inconclusive or weak. This suggests that a simple correlation analysis may not be sufficient to understand the complexity of these relationships. In future work, we plan to use regression models or machine learning techniques (such as random forests or clustering algorithms) to uncover more nuanced patterns. These models could help control for confounding variables like GDP per capita, population density, or education spending that may affect both cost of living and social indicators.

We also recognize the need for a temporal dimension in our analysis. Our current study is based on data from a single year (2022), which limits our ability to detect trends or causal pathways. For future work, incorporating historical data across multiple years would allow us to perform longitudinal analyses, observing how changes in cost of living impact social indicators over time. This could help determine whether observed relationships are stable, increasing, or diminishing.

From a broader perspective, one of the more thought-provoking lessons we learned was that cost of living is not inherently positive or negative—it reflects both opportunities and challenges. For example, cities with higher cost of living often provide better services, infrastructure, and salaries, but also pose difficulties related to inequality, housing affordability, and access to care. This duality became especially evident when considering cities like San Francisco or New York, which score highly on some wellness indicators but also have stark inequalities. Future work could explore intra-city disparities using spatial data, such as neighborhood-level indicators, to capture this heterogeneity.

Finally, we see potential in expanding the scope of our analysis beyond traditional social indicators. Future studies could incorporate environmental indicators (e.g., pollution levels, green space availability), digital infrastructure (e.g., internet access), or quality-of-life surveys to create a more holistic picture of well-being. There is also room for more qualitative or mixed-method approaches, such as case studies of specific cities, policy analysis, or interviews, to complement the quantitative data and provide richer context.

In conclusion, this project served as a starting point for understanding how cost of living may relate to social outcomes. While our results provide some insight, they also highlight the complexity of these relationships and the need for more robust, localized, and longitudinal data. We hope that future work will build on this foundation to more precisely capture how economic conditions intersect with human well-being in cities across the world.


# Reproducing: Sequence of steps required for someone else to reproduce your results.
# References: Formatted citations for any papers, datasets, or software used in your project.


Below are examples of artifacts we expect to see as part of your projects:

Data acquisition (cf. Weeks 3-4)
Script(s) used to programmatically acquire data (e.g., via requests) and check integrity (e.g., SHA-256)
Documentation describing steps someone else would use to acquire data, including checksums. This is particularly important if your data cannot be redistributed.
Data integration (cf. Weeks 5-6)
Script(s) used to integrate datasets (e.g., Python or SQL)
Conceptual models, integration schema, or query that spans both sources
Documentation describing steps used to integrate data.
Profiling, quality assessment, cleaning (cf. Week 7)
Script(s) used to profile, assess quality of, and clean data (e.g., Python or SQL)
Documentation describing steps used to profile and clean data
OpenRefine operation history ("recipe")
Data analysis and/or visualization
Script(s) used to analyze data and/or generate associated visualizations
Analysis results and/or visualizations
Documentation describing steps used to analyze or visualize data
Automated Workflow (cf. Week 10)
Snakemake workflow automating your end-to-end analysis workflow from acquisition to result visualization.
Run All script that can be used to re-execute your end-to-end analysis workflow
Documentation describing the steps required to repeat your workflow
Reproducible package (cf. Week 8)
Sufficient information to allow someone else to reproduce your analysis including:
Documentation describing steps someone else needs to take to reproduce your results
Data or documentation describing how to obtain data used
All code, workflow scripts, etc., needed to reproduce your results
Actual results of your analysis including output files, visualizations, etc.
You are required to upload your output data (and optionally, your input data, if not retrieved programmatically) to Box and include, in your report, a shareable link to the folder where the data is stored, as well as information on where the data should be saved in your project folder once it's downloaded from Box.
You are responsible for ensuring the shared folder can be accessed by the TAs. If you are unsure about this, you should reach out to the TAs on Campuswire at least 12 hours before the deadline. You may lose points if the TAs cannot access the data you've shared.
Make sure you add the path to the data that is already in Box to .gitignore before you push any changes to GitHub.
Specification of software dependencies (e.g., requirements.txt) and record of specific packages used (e.g., output of pip freeze). Optionally, a Dockerfile and container image pushed to Dockerhub.
Optionally, a Dockerfile and container image pushed to DockerHub or a CodeOcean capsule
Licenses for data and software created as part of your project
Citation of data and software used (cf. Week 12)
Accurate citations of the data and/or software used in your project in conformance with standards
Metadata describing your dataset and package (cf. Week 13)
Data dictionary or codebook as text file, PDF, or self-describing data formats.
Descriptive metadata describing your project in conformance with a standard such as DataCite, Schema.org.
Archival record (cf. Week 14)
An copy of your project submitted to the Zenodo long-term archive or a CodeOcean capsule
Persistent Identifier (cf. Week 12)
Persistent identifier obtained from the long-term archive
