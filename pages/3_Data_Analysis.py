import streamlit as st
import pandas as pd

st.title("Data Analysis")

df = pd.read_csv("Sales Clenad_df.csv")

st.subheader("Sales by Product Category")
category_sales = df.groupby("item type")["total revenue"].sum()
st.bar_chart(category_sales)

st.subheader("Average Order Value by Region")
aov = (
    df.groupby("region")
    .agg(revenue=("total revenue", "sum"),
         orders=("order id", "nunique"))
)
aov["AOV"] = aov["revenue"] / aov["orders"]
st.bar_chart(aov["AOV"])