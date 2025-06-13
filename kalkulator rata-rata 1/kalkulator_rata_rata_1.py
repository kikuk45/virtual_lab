import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(
    page_title="Kalkulator Rata-Rata dengan Grafik",
    page_icon=":bar_chart:",
    layout="wide",
)

st.title("📊 Kalkulator Rata-Rata Interaktif")
st.markdown("Masukkan angka-angka yang dipisahkan koma untuk menghitung rata-rata dan melihat grafiknya.")
st.markdown("---")


warna = st.selectbox("🎨 Pilih Warna Grafik", ["viridis", "rocket", "magma", "coolwarm", "flare", "crest"])

input_angka = st.text_input("Masukkan Angka (pisahkan dengan koma):", "10, 20, 30")

if st.button("Hitung & Tampilkan"):
    try:
        angka_str = [x.strip() for x in input_angka.split(",")]
        angka = [float(x) for x in angka_str if x]

        if not angka:
            st.error("❌ Tidak ada angka yang dimasukkan.")
        else:
            rata_rata = sum(angka) / len(angka)
            st.success(f"✅ Rata-rata: **{rata_rata:.2f}**")

            
            st.info(f"""
**📌 Statistik Tambahan:**
- Jumlah Data: {len(angka)}
- Nilai Tertinggi: {max(angka)}
- Nilai Terendah: {min(angka)}
""")

            df = pd.DataFrame({'Nilai': angka, 'Indeks': range(len(angka))})
            st.subheader("📊 Grafik Batang")

            fig, ax = plt.subplots(figsize=(10, 6))
            sns.barplot(x=df['Indeks'], y=df['Nilai'], palette=warna, ax=ax)
            ax.set_xlabel("Indeks Data", fontsize=12)
            ax.set_ylabel("Nilai", fontsize=12)
            ax.set_title("Visualisasi Angka", fontsize=14, fontweight='bold')

            for p in ax.patches:
                ax.annotate(f'{p.get_height():.2f}', (p.get_x() + p.get_width() / 2., p.get_height()),
                            ha='center', va='center', xytext=(0, 5), textcoords='offset points', fontsize=10)

            plt.tight_layout()
            st.pyplot(fig)

    except ValueError:
        st.error("❌ Input tidak valid. Gunakan angka dipisahkan koma.")
    except Exception as e:
        st.error(f"Terjadi kesalahan: {e}")

st.markdown("---")
st.markdown("Dibuat dengan ❤️ menggunakan Streamlit")
