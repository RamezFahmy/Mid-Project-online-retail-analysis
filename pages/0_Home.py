import streamlit as st
import pandas as pd

# Page configuration (ONLY ONCE)
st.set_page_config(
    page_title="Home",
    page_icon="🏠",
    layout="wide"
)


# Home Page Title & Description
st.title("Global Sales Transactions Analysis")

st.write("""
This application presents a mid-project analysis of global sales transactions
across regions, product categories, and sales channels.
The objective is to explore the data, perform analysis, and present insights
through an interactive Streamlit application.
""")

# Load Dataset
df = pd.read_csv("Dataset/Sales Clenad_df.csv")

# High-level Dataset Overview
st.header("Dataset Overview")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Records", df.shape[0])

with col2:
    st.metric("Total Columns", df.shape[1])

with col3:
    st.metric("Regions", df["region"].nunique())

# Data Preview
st.subheader("Sample of the Dataset")
st.write("The table below shows a preview of the dataset used in this analysis.")
st.dataframe(df.head())

# Navigation Hint
st.info("Use the sidebar to navigate through the different analysis sections.")
