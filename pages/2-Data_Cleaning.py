import streamlit as st
import pandas as pd

st.title("Data Cleaning")

st.markdown("""
Cleaning steps applied:
- Removed duplicates
- Handled missing values
- Converted dates
- Standardized column names
""")

df = pd.read_csv("Dataset/Sales Clenad_df.csv")

st.dataframe(df.head())

