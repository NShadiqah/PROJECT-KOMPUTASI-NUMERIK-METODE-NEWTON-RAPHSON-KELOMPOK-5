import streamlit as st
import pandas as pd
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

# Selamat Datang
st.title('Selamat Datang di Program Kelompok 5')
st.write(''' 
### Program ini menggunakan Metode Newton-Raphson untuk mencari akar persamaan dengan interaksi yang dinamis. 
Anda bisa memasukkan persamaan dan beberapa nilai tebakan awal untuk melihat hasilnya! 
''')

# Membuat garis pemisah
st.markdown("---")

# Input persamaan dari pengguna
st.header('Langkah 1: Masukkan Persamaan Anda')
user_input = st.text_input('Masukkan persamaan f(x) (contoh: x**3 - 4*x + 1):', value='x**3 - 4*x + 1')
x_symbol = sp.symbols('x')

# Mengubah input pengguna menjadi fungsi f(x) dan turunan f'(x)
try:
    f_expr = sp.sympify(user_input)  # Parsing fungsi dari input pengguna
    f_prime_expr = sp.diff(f_expr, x_symbol)  # Turunan fungsi
except sp.SympifyError:
    st.error("Input persamaan tidak valid! Silakan masukkan persamaan yang benar.")
    st.stop()

# Fungsi f(x) dari input pengguna
def f(x):
    """
    Evaluasi fungsi f(x) dari input pengguna.
    """
    return float(f_expr.subs(x_symbol, x))

# Fungsi turunan f'(x) dari input pengguna
def f_prime(x):
    """
    Evaluasi fungsi turunan f'(x) dari input pengguna.
    """
    return float(f_prime_expr.subs(x_symbol, x))

# Metode Newton-Raphson dengan hasil per iterasi
def newton_raphson(x0, e, n):
    """
    Metode Newton-Raphson untuk mencari akar dari fungsi f(x), dengan hasil per iterasi.
    """
    # Simpan hasil setiap iterasi dalam list of dictionaries
    results = []
    
    for i in range(n):
        fx0 = f(x0)  # Hitung nilai fungsi pada titik x0
        fpx0 = f_prime(x0)  # Hitung nilai turunan fungsi pada titik x0
        
        # Menghindari pembagian dengan nol
        if fpx0 == 0:
            st.error("Turunan nol, tidak bisa melanjutkan!")
            return None, results
        
        # Newton-Raphson: x1 = x0 - fx0 / fpx0
        x1 = x0 - fx0 / fpx0
        
        # Menyimpan hasil iterasi ke dalam tabel
        results.append({
            'Iterasi': i + 1,
            'x_n': x0,
            'f(x_n)': fx0,
            '|x_{n+1} - x_n|': abs(x1 - x0)
        })
        
        # Cek apakah hasilnya sudah mendekati akar sesuai toleransi error
        if abs(x1 - x0) < e:
            st.success(f"Akar ditemukan: {x1} pada iterasi ke-{i + 1}")
            return x1, results
        
        # Update nilai x0 dengan hasil x1
        x0 = x1
    
    st.error("Akar tidak ditemukan dalam jumlah iterasi maksimum.")
    return None, results

# Input dari pengguna
st.header('Langkah 2: Masukkan Parameter Anda')
x0_values = st.text_input('Masukkan nilai-nilai awal tebakan akar (x0), dipisahkan dengan koma:', value='2.0, 1.5, -1.0')
x0_list = [float(x.strip()) for x in x0_values.split(',')]
e = st.number_input('Masukkan nilai toleransi error (e):', value=0.0001, format="%.5f")
n = st.number_input('Masukkan jumlah maksimum iterasi (n):', value=100, step=1)

# Tombol eksekusi
if st.button('Hitung Akar'):
    combined_results = []
    
    # Looping over each x0 in the list of guesses
    for x0 in x0_list:
        st.write(f"### Hasil untuk x0 = {x0}")
        akar, results = newton_raphson(x0, e, n)
        
        # Jika akar ditemukan atau iterasi dijalankan
        if results:
            # Menampilkan hasil dalam bentuk tabel
            df = pd.DataFrame(results)
            st.write("Hasil tiap iterasi:")
            st.table(df)
            
            # Plotting grafik konvergensi
            st.write("Grafik konvergensi:")
            iterasi = df['Iterasi']
            x_n_values = df['x_n']
            
            plt.figure(figsize=(8, 6))
            plt.plot(iterasi, x_n_values, marker='o', linestyle='-', label=f'x0 = {x0}')
            plt.xlabel('Iterasi')
            plt.ylabel('Nilai x_n')
            plt.grid(True)
            combined_results.append(results)
    
    # Menampilkan grafik keseluruhan
    plt.title('Konvergensi Newton-Raphson untuk Beberapa x0')
    plt.legend()
    st.pyplot(plt)

# Membuat garis pemisah di bagian akhir
st.markdown("---")

# Penutup
st.write("### Terima kasih telah menggunakan Program Kelompok 5!")
st.write("Silakan coba berbagai persamaan dan nilai awal untuk mendapatkan hasil yang optimal.")
