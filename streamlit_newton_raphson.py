import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import base64
from sympy import symbols, diff, lambdify, sympify

# Fungsi untuk menghitung f(x) berdasarkan persamaan simbolik
def f(x, persamaan_lambdified):
    return persamaan_lambdified(x)

# Fungsi untuk menghitung turunan f(x) simbolik
def df(x, turunan_lambdified):
    return turunan_lambdified(x)

# Metode Newton-Raphson
def metode_Newton_Raphson(x0, tol_e, persamaan_lambdified, turunan_lambdified):
    x = x0
    iterasi = 0
    results = []
    x_values = [x]

    while True:
        fx = f(x, persamaan_lambdified)
        dfx = df(x, turunan_lambdified)

        results.append({"Iterasi": iterasi + 1, "Xn": x, "F(Xn)": fx, "F'(Xn)": dfx})

        if abs(fx) < tol_e:
            hasil = x
            results.append({"Iterasi": "Akar", "Xn": hasil, "F(Xn)": f(hasil, persamaan_lambdified), "F'(Xn)": ""})
            break

        x = x - fx / dfx
        x_values.append(x)
        iterasi += 1

    return results, x_values

# Fungsi untuk menampilkan grafik
def plot_function(persamaan_lambdified, x_values):
    x = np.linspace(min(x_values) - 1, max(x_values) + 1, 1000)
    y = [f(xi, persamaan_lambdified) for xi in x]

    plt.figure(figsize=(8, 6))
    plt.plot(x, y, label='f(x)')
    plt.axhline(y=0, color='r', linestyle='--')
    plt.scatter(x_values, [f(xi, persamaan_lambdified) for xi in x_values], color='green', label='Iterasi')

    for i, txt in enumerate(range(1, len(x_values) + 1)):
        plt.annotate(f'x{txt}', (x_values[i], f(x_values[i], persamaan_lambdified)))

    plt.legend()
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Grafik Fungsi dan Iterasi Newton-Raphson')
    st.pyplot(plt)

# Fungsi untuk memuat latar belakang dari file lokal
def load_background_image(image_path):
    with open(image_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Fungsi untuk menambahkan latar belakang
def add_bg_from_local(bg_image):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{bg_image}");
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Path file gambar latar belakang
bg_image_path = "wp.jpg"  # Pastikan file ini ada di folder yang sama

# Memuat gambar latar belakang
bg_image = load_background_image(bg_image_path)

# Menambahkan gambar latar belakang
add_bg_from_local(bg_image)

# Bagian aplikasi Streamlit
st.title("Metode Newton-Raphson dengan Streamlit")

# Input dari pengguna
persamaan_str = st.text_input("Masukkan persamaan (contoh: x**2 - 4*x + 3):", "x**2 - 4*x + 3")
tebakan_awal = st.number_input("Masukkan tebakan awal (x0):", value=1.0)
toleransi_e = st.number_input("Masukkan toleransi error (e):", value=1e-5)

# Parsing dan validasi persamaan
x = symbols('x')
try:
    persamaan = sympify(persamaan_str)
    turunan = diff(persamaan, x)
    persamaan_lambdified = lambdify(x, persamaan)
    turunan_lambdified = lambdify(x, turunan)

    st.write(f"Persamaan: {persamaan}")
    st.write(f"Turunan: {turunan}")

    # Tombol untuk memulai kalkulasi
    if st.button("Hitung"):
        with st.spinner('Menghitung akar...'):
            results, x_values = metode_Newton_Raphson(tebakan_awal, toleransi_e, persamaan_lambdified, turunan_lambdified)
        
        # Menampilkan tabel hasil iterasi
        results_df = pd.DataFrame(results)
        st.write("### Hasil Iterasi Newton-Raphson:")
        st.dataframe(results_df)  # Menampilkan dalam bentuk tabel interaktif

        # Menampilkan grafik f(x) dan iterasi
        plot_function(persamaan_lambdified, x_values)
except Exception as e:
    st.error(f"Error dalam persamaan: {e}")
