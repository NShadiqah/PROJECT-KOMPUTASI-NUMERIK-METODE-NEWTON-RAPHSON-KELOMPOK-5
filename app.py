# app.py
import streamlit as st
import pandas as pd
from newton_raphson import metode_Newton_Raphson
from plot_utils import plot_function
from background_utils import load_background_image, add_bg_from_local

# Path file gambar latar belakang
bg_image_path = "wp.jpg"  # Pastikan file ini ada di folder yang sama

# Memuat gambar latar belakang
bg_image = load_background_image(bg_image_path)

# Menambahkan gambar latar belakang
add_bg_from_local(bg_image)

# Bagian aplikasi Streamlit
st.title("Metode Newton-Raphson dengan Streamlit")

# Input dari pengguna
persamaan = st.text_input("Masukkan persamaan (contoh: x*2 - 4*x + 3):", "x*2 - 4*x + 3")
tebakan_awal = st.number_input("Masukkan tebakan awal (x0):", value=1.0)
toleransi_e = st.number_input("Masukkan toleransi error (e):", value=0.001, format="%.3f")

# Tombol untuk memulai kalkulasi
if st.button("Hitung"):
    with st.spinner('Menghitung akar...'):
        results, x_values = metode_Newton_Raphson(tebakan_awal, toleransi_e, persamaan)
    
    # Menampilkan tabel hasil iterasi
    results_df = pd.DataFrame(results)
    st.write("### Hasil Iterasi Newton-Raphson:")
    st.dataframe(results_df)  # Menampilkan dalam bentuk tabel interaktif

    # Menampilkan grafik f(x) dan iterasi
    plot_function(persamaan, x_values)
