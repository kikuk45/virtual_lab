
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Konfigurasi halaman
st.set_page_config(
    page_title="Kalkulator Rata-Rata Interaktif",
    page_icon="📊",
    layout="centered"
)

# Judul aplikasi
st.title("📊 Kalkulator Rata-Rata Interaktif")
st.markdown("Masukkan angka-angka yang dipisahkan dengan koma, lalu lihat hasil rata-ratanya dan grafik batang visualisasinya.")
st.markdown("---")

# Pilihan warna grafik
warna = st.selectbox("🎨 Pilih Tema Warna Grafik", ["viridis", "rocket", "magma", "coolwarm", "crest", "flare"])

# Input angka
input_angka = st.text_input("📝 Masukkan angka (pisahkan dengan koma):", "70, 80, 90")

if st.button("🔍 Hitung Rata-Rata & Tampilkan Grafik"):
    try:
        angka = [float(x.strip()) for x in input_angka.split(",") if x.strip()]
        if angka:
            rata_rata = sum(angka) / len(angka)

            st.success(f"✅ Rata-rata: **{rata_rata:.2f}**")

            st.info(f'''
**📈 Statistik Tambahan:**
- Jumlah Data: {len(angka)}
- Nilai Maksimum: {max(angka)}
- Nilai Minimum: {min(angka)}
''')

            # DataFrame
            df = pd.DataFrame({"Nilai": angka, "Index": [f"Data {i+1}" for i in range(len(angka))]})

            # Grafik batang
            fig, ax = plt.subplots(figsize=(10, 5))
            sns.barplot(x="Index", y="Nilai", data=df, palette=warna, ax=ax)

            for p in ax.patches:
                ax.annotate(f'{p.get_height():.2f}', (p.get_x() + p.get_width()/2., p.get_height()),
                            ha='center', va='center', xytext=(0, 8), textcoords='offset points', fontsize=9)

            ax.set_title("Visualisasi Data", fontsize=14, weight='bold')
            ax.set_xlabel("Data")
            ax.set_ylabel("Nilai")
            st.pyplot(fig)

        else:
            st.warning("⚠️ Silakan masukkan setidaknya satu angka yang valid.")

    except Exception as e:
        st.error(f"❌ Terjadi kesalahan: {e}")

st.markdown("---")
st.markdown("<center><sub>Dibuat dengan ❤️ oleh Virtual Lab</sub></center>", unsafe_allow_html=True)
