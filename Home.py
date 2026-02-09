import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Sales Transactions Analysis", layout="wide")

st.title("Global Sales Transactions Analysis")

st.write("""
This application presents a mid-project analysis of global sales transactions
across regions, product categories, and sales channels.
""")

df = pd.read_csv("Sales Clenad_df.csv")

st.header("Dataset Overview")
st.write(f"Rows: {df.shape[0]}")
st.write(f"Columns: {df.shape[1]}")

st.dataframe(df.head())

st.info("Use the sidebar to navigate through the analysis pages.")