# Title: Impact of Cost of Living on Social Metrics Across the World

# Link to archival record: Link to the archived copy of your project, including persistent identifier.

# Contributors: Bulleted list of contributors (with optional ORCIDs).
- Angela Jing: 0009-0001-0231-7402
- Shawna Ye: 0009-0001-4840-3883

# Summary: [500-1000 words] Description of your project, motivation, research question(s), and any findings.
Our project looks at two datasets: a 2022 cost of living across global cities dataset and economic, social, demographic, and environmental indicators from the World Bank. By analyzing
these datasets, we hope to discover where there's a relationship between cost of living metrics (food prices, housing costs, average salary, etc.) and social indicators in the US (school enrollment rates, infant mortality rates, 
poverty headcount, etc.). For example, if a country has a higher cost of living, are social indicators higher due to increased access to better services and infrastructure? We were motivated to research this topic due to personal
curiosity and practicality. As young adults about to enter the workforce and manage our own living expenses, we have become more aware of how cost of living not only affects individual liestyles but also broader social outcomes
within society. However, some major cities such as New York City or San Francisco offer better public services and amenities but are also known for their social inequalities. Our research
question is: For countries across the world, what is the relationship between cost of living metrics in major cities and overall social indicators? By examining this question, we hope to look at whether cost of living metrics (an
inexpensive meal at a restaurant, monthly cost of preschool/kindergarten for one child, price per square meter to buy an apartment in the city center, average monthly net salary) have some sort of impact or relationship
with social wellness metrics (fertility rate, life expectancy, school enrollment, poverty headcount). 

FINDINGS


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
