
import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from collections import Counter

st.set_page_config(page_title="Statistik Deskriptif", layout="wide")

st.title("📊 Aplikasi Statistik: Mean, Median, Modus")

st.markdown(
    "Upload data numerik (CSV) atau masukkan angka manual (pisahkan dengan koma) "
    "untuk menghitung **mean**, **median**, dan **modus** serta menampilkan grafik batangnya."
)

# Input manual
input_manual = st.text_area("Masukkan data (pisahkan dengan koma):", "")

# Upload file
uploaded_file = st.file_uploader("Atau unggah file CSV", type=["csv"])

data = []

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    col_options = df.select_dtypes(include=np.number).columns.tolist()
    if col_options:
        selected_col = st.selectbox("Pilih kolom numerik:", col_options)
        data = df[selected_col].dropna().tolist()
    else:
        st.warning("File tidak memiliki kolom numerik.")
elif input_manual:
    try:
        data = [float(x.strip()) for x in input_manual.split(",") if x.strip()]
    except:
        st.error("Pastikan semua input adalah angka dan dipisahkan dengan koma.")

if data:
    st.subheader("📌 Hasil Perhitungan Statistik")
    mean_val = np.mean(data)
    median_val = np.median(data)
    modus_val = Counter(data).most_common(1)[0][0]

    st.markdown(f"- **Mean (Rata-rata):** {mean_val:.2f}")
    st.markdown(f"- **Median:** {median_val:.2f}")
    st.markdown(f"- **Modus:** {modus_val:.2f}")

    # Visualisasi
    st.subheader("📉 Visualisasi Data")
    fig, ax = plt.subplots()
    sns.histplot(data, kde=True, bins=10, color="skyblue", ax=ax)
    ax.axvline(mean_val, color='r', linestyle='--', label=f'Mean: {mean_val:.2f}')
    ax.axvline(median_val, color='g', linestyle='-.', label=f'Median: {median_val:.2f}')
    ax.axvline(modus_val, color='orange', linestyle=':', label=f'Modus: {modus_val:.2f}')
    ax.legend()
    st.pyplot(fig)
else:
    st.info("Masukkan data manual atau unggah file CSV untuk melihat hasil.")
