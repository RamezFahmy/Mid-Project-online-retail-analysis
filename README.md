📊 #Mid-Project: Global Sales Transactions Analysis

📌 ##Project Overview

This project presents an end-to-end data analysis of a global sales transactions dataset. The objective is to explore, clean, analyze, and visualize sales data, then deploy the results using an interactive Streamlit web application.

---
###The project demonstrates practical skills in:
- Data cleaning and preparation
- Exploratory data analysis (EDA)
- Business-driven analytical questions
- Data visualization
- Web app deployment using Streamlit Cloud

--- 
##📂 Dataset Description
###Dataset Information

- **Source File**: https://www.kaggle.com/datasets/okhiriadaveoseghale/100000-sales-records?utm_source=chatgpt.com
- **Scope**:Global sales transactions
- **Records**:10K Sales transactions across multiple regions
- **Columns**:15 featues including product details, channels and order informations.
- **Key Dimensions**: Region, Product Category, Sales Channel, Order Date
- **Metrics**: Units Sold, Total Revenue, Total Profit

----
##Key Columns

###Geographic Information
- Region
- Country
  
###Product Information                       
- item type
- sales channel
  
###Transaction Details
- Order id
- Order date
- Ship date
- Units sold
  
###Financial Metrics
- Unit price
- Unit cost
- Total revenue
- Total profit

----
##🧹 Data Cleaning Process
The dataset was prepared for analysis using the following steps:

###Cleaning Steps Applied

- Removed duplicate records
- Checked and verified missing values
- Converted date columns to datetime format
- Standardized column names for consistency
- Ensured numeric fields were properly formatted

----
**Output**
Cleaned dataset used for all analysis and visualizations
Verified dataset size and structure after cleaning

----
**🔎 Exploratory Data Analysis (EDA)**

The exploration phase included:

- Reviewing dataset structure and data types
- Generating summary statistics for numerical variables
- Analyzing categorical distributions:
- Sales channel distribution
- Regional distribution
- Product category distribution
This step ensured a clear understanding of data composition before performing business analysis.

**📈 Data Analysis**

The analysis focused on answering key business questions.

1️⃣ Sales by Product Category

- Aggregated total revenue by item type
- Identified top-performing product categories
- Highlighted revenue concentration patterns

2️⃣ Average Order Value (AOV) by Region

Calculated as:
**AOV = Total Revenue ÷ Number of Unique Orders**
- Compared purchasing behavior across regions
- Identified variation in average transaction size

3️⃣ Total Revenue Over Time

- Resampled data monthly
- Analyzed revenue trends and seasonality patterns

4️⃣ Total Profit by Region

- Aggregated total profit by region
- Identified most profitable markets
- Distinguished revenue performance from profitability

**🌐 Streamlit Web Application**

The project includes a multi-page interactive Streamlit application.

**Application Structure** 
Mid-Project - Global Sales Data Analysis/
│
├── app.py                       # Home page
├── Dataset/
│   └── Sales Clenad_df.csv      # Dataset used in analysis
├── pages/
│   ├── Data Exploration.py
│   ├── Data Cleaning.py
│   ├── Data Analysis.py
│   └── Data Visualization.py
├── notebooks/
│   └── Jupyter analysis notebook
└── README.md

**Application Pages**
🏠 Home
Project overview
Dataset metrics
Sample data preview

🔍 Data Exploration
Dataset structure
Summary statistics
Categorical distributions

🧹 Data Cleaning
Cleaning steps documentation
Missing value verification
Dataset size confirmation
Cleaned data preview

📊 Data Analysis
Revenue by product category
Average Order Value by region

📈 Data Visualization
Monthly revenue trend
Profit by region chart

🚀 Deployment
**The application is deployed using:**
GitHub (repository hosting)
Streamlit Cloud (web deployment)

Run Locally
pip install streamlit pandas matplotlib
streamlit run app.py

🛠 Technologies Used
Python 3.x
Pandas
Matplotlib
Streamlit
GitHub
Streamlit Cloud

📌 Project Workflow
Data loading
Data cleaning
Exploratory data analysis
Business-focused analysis
Visualization
Streamlit development
Cloud deployment

📽 Project Demonstration

Streamlit Public Link: (https://mid-project-global-sales-transactions-analysis-qphburpqcbkbjob.streamlit.app/Home)
Video Walkthrough: (Add Google Drive or YouTube link here)
Powepoint Presentation: (https://docs.google.com/presentation/d/1XXPwXGRZhUOWr1dT9hxQ5ed3HWPGU2AD/edit?usp=drive_link&ouid=113635610336734727227&rtpof=true&sd=true)
