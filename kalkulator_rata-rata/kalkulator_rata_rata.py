
import streamlit as st

st.title("Kalkulator Rata-Rata")
st.write("Masukkan angka-angka yang dipisahkan dengan koma.")

input_angka = st.text_input("Input", "10, 20, 30")

if st.button("Hitung Rata-Rata"):
    try:
        angka = [float(x.strip()) for x in input_angka.split(",")]
        rata_rata = sum(angka) / len(angka)
        st.success(f"Rata-rata dari data yang dimasukkan adalah: {rata_rata:.2f}")
    except:
        st.error("Input tidak valid. Pastikan hanya angka yang dipisahkan koma.")
