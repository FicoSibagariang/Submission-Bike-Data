import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
all_data_df = pd.read_csv("dashboard1/all_data.csv")

# Pastikan kolom dteday ada dan diubah ke tipe datetime
all_data_df["dteday"] = pd.to_datetime(all_data_df["dteday"])

# Ambil rentang tanggal minimum dan maksimum
min_date = all_data_df["dteday"].min()
max_date = all_data_df["dteday"].max()

# Sidebar untuk memilih rentang waktu
with st.sidebar:
    start_date, end_date = st.date_input(
        label='Rentang Waktu',
        min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )

# Filter data berdasarkan rentang waktu yang dipilih
main_df = all_data_df[(all_data_df["dteday"] >= str(start_date)) & 
                      (all_data_df["dteday"] <= str(end_date))]

# Streamlit Dashboard
st.header("Dashboard Penyewaan Sepeda")

# 1. Total Penyewaan Harian
st.subheader("Daily Rent")
total_rent = main_df["total_rentals"].sum()
st.metric("Total Rent", value=total_rent)

# 2. Musim dengan Penyewaan Tertinggi
st.subheader("Musim dengan Penyewaan Tertinggi")
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x="total_per_season", y="season", data=all_data_df, palette="Blues", ax=ax)
st.pyplot(fig)

# 3. Cuaca dengan Penyewaan Tertinggi
st.subheader("Cuaca dengan Penyewaan Tertinggi")
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x="total_by_weather", y="weathersit", data=all_data_df, palette="Blues", ax=ax)
st.pyplot(fig)

# 4. Total Penyewaan Sepeda pada Hari Kerja vs Hari Libur
st.subheader("Total Penyewaan Sepeda pada Hari Kerja vs Hari Libur")
fig, ax = plt.subplots(figsize=(3, 4))
sns.barplot(x="workingday", y="total_by_working_day", data=all_data_df, palette="Blues", ax=ax)
st.pyplot(fig)

# 5. Visualisasi Clustering
st.subheader("Visualisasi Clustering Penyewaan Sepeda")
fig, ax = plt.subplots(figsize=(12, 6))
sns.scatterplot(data=all_data_df, x="dteday", y="total_rentals", hue="cluster", palette="Set2", ax=ax)
plt.xticks(rotation=45)
st.pyplot(fig)
