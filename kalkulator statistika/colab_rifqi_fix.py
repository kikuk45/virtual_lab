import streamlit as st

def hitung_rata_rata(angka_list):
    if len(angka_list) == 0:
        return 0
    return sum(angka_list) / len(angka_list)

st.title("📊 Kalkulator Rata-rata")
st.write("Masukkan angka-angka yang dipisahkan dengan koma, lalu tekan tombol hitung.")

input_angka = st.text_input("Masukkan angka:", value="4, 7, 8")

if st.button("Hitung Rata-rata"):
    try:
        angka_list = [float(angka.strip()) for angka in input_angka.split(',')]
        rata_rata = hitung_rata_rata(angka_list)
        st.success(f"Rata-rata dari angka yang dimasukkan adalah: {rata_rata}")
    except ValueError:
        st.error("Input tidak valid! Pastikan hanya memasukkan angka yang dipisahkan dengan koma.")
