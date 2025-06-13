
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Kalkulator Rata-Rata", page_icon="📊", layout="centered")

st.title("📊 Kalkulator Rata-Rata Interaktif")
st.subheader("Masukkan angka-angka dan lihat grafik batangnya!")

st.markdown("Pisahkan setiap angka dengan koma, contoh: `10, 20, 30`")

input_angka = st.text_input("📥 Masukkan angka:", "10, 20, 30")

if st.button("🔍 Hitung Rata-Rata"):
    try:
        angka = [float(x.strip()) for x in input_angka.split(",")]
        rata_rata = sum(angka) / len(angka)
        st.success(f"✅ Rata-rata dari data adalah: {rata_rata:.2f}")

        # Membuat DataFrame untuk grafik batang
        df = pd.DataFrame({"Angka": angka}, index=[f"Data {i+1}" for i in range(len(angka))])
        st.markdown("### 📈 Grafik Batang Nilai")
        st.bar_chart(df)

    except:
        st.error("❌ Input tidak valid. Pastikan hanya angka yang dipisahkan koma.")

st.markdown("---")
st.markdown("""<div style='text-align: center; color: gray; font-size: 14px;'>
Dibuat dengan ❤️ oleh [Nama Kamu]
</div>""", unsafe_allow_html=True)
