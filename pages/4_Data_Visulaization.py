import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Data Visualization")

# Load data
df = pd.read_csv("Dataset/Sales Clenad_df.csv")

# Convert date column
df["order date"] = pd.to_datetime(df["order date"])

# ===============================
# Chart 1: Total Revenue Over Time
# ===============================
monthly = (
    df.set_index("order date")
      .resample("M")["total revenue"]
      .sum()
)

fig1, ax1 = plt.subplots()
ax1.plot(monthly.index, monthly.values, marker="o")
ax1.set_title("Total Revenue Over Time")
ax1.set_xlabel("Date")
ax1.set_ylabel("Total Revenue")

st.pyplot(fig1)

# ===============================
# Chart 2: Total Profit by Region
# ===============================
profit_by_region = (
    df.groupby("region")["total profit"]
      .sum()
      .sort_values(ascending=False)
)

fig2, ax2 = plt.subplots()
profit_by_region.plot(kind="bar", ax=ax2)
ax2.set_title("Total Profit by Region")
ax2.set_xlabel("Region")
ax2.set_ylabel("Total Profit")
plt.xticks(rotation=45, ha="right")

st.pyplot(fig2)
