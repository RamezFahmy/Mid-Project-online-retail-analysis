import streamlit as st
import pandas as pd

st.title("Data Exploration")

df = pd.read_csv("Sales Clenad_df.csv")

st.subheader("Dataset Structure")
st.write(df.info())

st.subheader("Summary Statistics")
st.dataframe(df.describe())

st.subheader("Sales Channel Distribution")
st.bar_chart(df["sales channel"].value_counts())

st.subheader("Regional Distribution")
st.bar_chart(df["region"].value_counts())