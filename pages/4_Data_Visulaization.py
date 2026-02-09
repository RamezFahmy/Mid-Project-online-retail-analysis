import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Data Visualization")

df = pd.read_csv("Sales Clenad_df.csv")
df["order date"] = pd.to_datetime(df["order date"])

monthly = df.set_index("order date").resample("M")["total revenue"].sum()

fig, ax = plt.subplots()
ax.plot(monthly.index, monthly.values, marker="o")
st.pyplot(fig)