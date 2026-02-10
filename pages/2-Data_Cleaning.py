import streamlit as st
import pandas as pd

st.title("Data Cleaning")

# Cleaning Summary
st.subheader("Cleaning Steps Applied")
st.markdown("""
The following data cleaning steps were applied to prepare the dataset for analysis:
- Removed duplicate records  
- Checked and handled missing values  
- Converted date columns to datetime format  
- Standardized column names for consistency  
""")

# Load Dataset
df = pd.read_csv("Dataset/Sales Clenad_df.csv")

# Missing Values Check
st.subheader("Missing Values Check")

missing_values = df.isna().sum()

missing_df = (
    missing_values[missing_values > 0]
    .reset_index()
    .rename(columns={"index": "Column", 0: "Missing Values"})
)

if missing_df.empty:
    st.success("No missing values were found in the dataset.")
else:
    st.warning("Some columns contain missing values:")
    st.dataframe(missing_df)

# Dataset Size After Cleaning
st.subheader("Dataset Size After Cleaning")

col1, col2 = st.columns(2)

with col1:
    st.metric("Number of Rows", df.shape[0])

with col2:
    st.metric("Number of Columns", df.shape[1])

# Cleaned Data Preview
st.subheader("Cleaned Dataset Preview")
st.write("Sample rows from the cleaned dataset used for analysis.")
st.dataframe(df.head())
