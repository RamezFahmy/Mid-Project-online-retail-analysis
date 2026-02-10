import streamlit as st
import pandas as pd

st.title("Data Exploration")

# Load dataset
df = pd.read_csv("Dataset/Sales Clenad_df.csv")

# Dataset Structure
st.subheader("Dataset Structure")
st.write("Overview of columns and data types in the dataset.")

structure_df = pd.DataFrame({
    "Column Name": df.columns,
    "Data Type": df.dtypes.astype(str)
})

st.dataframe(structure_df)

# Summary Statistics
st.subheader("Summary Statistics")
st.write("Descriptive statistics for numerical variables.")

st.dataframe(df.describe())

# Categorical Distributions
st.subheader("Categorical Distributions")
st.write("Distribution of key categorical variables in the dataset.")

col1, col2 = st.columns(2)

with col1:
    st.write("Sales Channel Distribution")
    st.bar_chart(df["sales channel"].value_counts())

with col2:
    st.write("Regional Distribution")
    st.bar_chart(df["region"].value_counts())

# Product Category Distribution
st.subheader("Product Category Distribution")
st.write("Number of transactions by product category.")

st.bar_chart(df["item type"].value_counts())
