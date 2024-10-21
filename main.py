import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import base64

# Fungsi untuk menghitung f(x) berdasarkan persamaan yang dimasukkan
def f(x, persamaan):
    return eval(persamaan)

# Fungsi untuk menghitung turunan(fx)
def df(x, persamaan):
    h = 1e-5
    return (f(x + h, persamaan) - f(x, persamaan)) / h

# Metode Newton-Raphson
def metode_Newton_Raphson(x0, tol_e, persamaan):
    x = x0
    iterasi = 0
    results = []
    x_values = [x]

    # Memulai loop tak terbatas untuk iterasi metode Newton-Raphson
    while True:
        # Menghitung nilai fungsi f(x) menggunakan nilai x saat ini dan persamaan
        fx = f(x, persamaan)

        # Menghitung turunan dari fungsi f'(x) menggunakan nilai x saat ini dan persamaan
        dfx = df(x, persamaan)

        # Menambahkan hasil iterasi saat ini (nomor iterasi, nilai x, f(x), dan f'(x)) ke dalam list 'results'
        results.append({"Iterasi": iterasi + 1, "Xn": x, "F(Xn)": fx, "F'(Xn)": dfx})

        # Memeriksa apakah nilai absolut dari f(x) lebih kecil dari tingkat toleransi (tol_e)
        if abs(fx) < tol_e:
            # Menyimpan nilai x saat ini sebagai akar (hasil)
            hasil = x

            # Menambahkan hasil akhir (akar ditemukan) ke dalam list 'results'
            results.append({"Iterasi": "Akar", "Xn": hasil, "F(Xn)": f(hasil, persamaan), "F'(Xn)": ""})

            # Keluar dari loop karena akar sudah ditemukan
            break

        # Memperbarui nilai x menggunakan rumus Newton-Raphson: x = x - f(x) / f'(x)
        x = x - fx / dfx

        # Menambahkan nilai x yang baru ke dalam list 'x_values' untuk melacak perubahan nilai x
        x_values.append(x)

        # Menambah nilai iterasi sebanyak 1
        iterasi += 1

    # Mengembalikan dua nilai: hasil (semua iterasi dan perhitungan) dan nilai-nilai x yang dilacak selama proses
    return results, x_values

# Fungsi untuk menampilkan grafik
def plot_function(persamaan, x_values):
    x = np.linspace(min(x_values) - 1, max(x_values) + 1, 1000)
    y = [f(xi, persamaan) for xi in x]

    plt.figure(figsize=(8, 6))
    plt.plot(x, y, label='f(x)')
    plt.axhline(y=0, color='r', linestyle='--')
    plt.scatter(x_values, [f(xi, persamaan) for xi in x_values], color='green', label='Iterasi')

    for i, txt in enumerate(range(1, len(x_values) + 1)):
        plt.annotate(f'x{txt}', (x_values[i], f(x_values[i], persamaan)))

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
persamaan = st.text_input("Masukkan persamaan (contoh: x*2 - 4*x + 3):", "x*2 - 4*x + 3")
tebakan_awal = st.number_input("Masukkan tebakan awal (x0):", value=1.0)
toleransi_e = st.number_input("Masukkan toleransi error (e):", value=1e-5)

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
