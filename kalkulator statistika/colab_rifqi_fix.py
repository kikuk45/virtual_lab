import streamlit as st
import math
from collections import Counter

def hitung_statistika(data):
    """
    Menghitung dan mengembalikan metrik statistika dasar dari list angka.
    """
    if not data:
        return {
            "rata_rata": None,
            "median": None,
            "modus": "Tidak ada data untuk dihitung",
            "rentang": None,
            "variansi": None,
            "standar_deviasi": None
        }

    data.sort() # Pastikan data terurut untuk median dan rentang
    n = len(data)

    # 1. Rata-rata (Mean)
    rata_rata = sum(data) / n

    # 2. Median
    if n % 2 == 0:
        median = (data[n // 2 - 1] + data[n // 2]) / 2
    else:
        median = data[n // 2]

    # 3. Modus (Mode)
    hitungan = Counter(data)
    maks_frekuensi = 0
    for freq in hitungan.values():
        if freq > maks_frekuensi:
            maks_frekuensi = freq

    modus = [k for k, v in hitungan.items() if v == maks_frekuensi]
    if len(modus) == len(data):
        modus_str = "Tidak ada modus unik (semua angka muncul dengan frekuensi yang sama)"
    else:
        modus_str = ', '.join(f'{m:.4f}' for m in sorted(modus))

    # 4. Rentang (Range)
    rentang = data[-1] - data[0]

    # 5. Variansi
    selisih_kuadrat = [(x - rata_rata) ** 2 for x in data]
    variansi = sum(selisih_kuadrat) / (n - 1 if n > 1 else 1)

    # 6. Standar Deviasi
    standar_deviasi = math.sqrt(variansi)

    return {
        "rata_rata": rata_rata,
        "median": median,
        "modus": modus_str,
        "rentang": rentang,
        "variansi": variansi,
        "standar_deviasi": standar_deviasi
    }

# --- Aplikasi Streamlit ---
st.set_page_config(page_title="Kalkulator Statistika", layout="centered")

st.title("📊 Kalkulator Statistika Sederhana")
st.markdown("---")

st.write(
    """
    Selamat datang di kalkulator statistika sederhana!
    Masukkan angka-angka Anda di bawah, pisahkan dengan koma (misalnya: `10, 20, 30, 40, 50`).
    """
)

# Input pengguna
input_data_str = st.text_area("Masukkan angka-angka Anda:", value="1, 2, 3, 4, 5", height=100)

data_list = []
pesan_error = ""

if st.button("Hitung Statistika"):
    try:
        # Proses input data
        angka_str = input_data_str.split(',')
        data_list = [float(x.strip()) for x in angka_str if x.strip()] # Filter out empty strings
        
        if not data_list:
            pesan_error = "Anda belum memasukkan angka yang valid."
        else:
            # Hitung statistika
            hasil = hitung_statistika(data_list)

            st.markdown("---")
            st.subheader("📝 Hasil Perhitungan")

            # Tampilkan hasil
            if hasil["rata_rata"] is not None:
                st.write(f"**Rata-rata (Mean):** `{hasil['rata_rata']:.4f}`")
            if hasil["median"] is not None:
                st.write(f"**Median:** `{hasil['median']:.4f}`")
            st.write(f"**Modus:** `{hasil['modus']}`")
            if hasil["rentang"] is not None:
                st.write(f"**Rentang (Range):** `{hasil['rentang']:.4f}`")
            if hasil["variansi"] is not None:
                st.write(f"**Variansi:** `{hasil['variansi']:.4f}`")
            if hasil["standar_deviasi"] is not None:
                st.write(f"**Standar Deviasi:** `{hasil['standar_deviasi']:.4f}`")

    except ValueError:
        pesan_error = "Input tidak valid. Pastikan Anda hanya memasukkan angka dan pisahkan dengan koma."
    except Exception as e:
        pesan_error = f"Terjadi kesalahan yang tidak terduga: {e}"

if pesan_error:
    st.error(pesan_error)

st.markdown("---")
st.caption("Dibuat dengan ❤️ oleh Python dan Streamlit")
