# plot_utils.py
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
from newton_raphson import f

# Fungsi untuk menampilkan grafik:
def plot_function(persamaan, x_values):
    # Membuat rentang nilai x yang lebih luas dari rentang nilai input iterasi
    x = np.linspace(min(x_values) - 1, max(x_values) + 1, 1000)
    # Menghitung nilai y dari fungsi f(x) untuk setiap nilai x
    y = [f(xi, persamaan) for xi in x]
    
    # Setup figure dan axis
    fig, ax = plt.subplots(figsize=(8, 6))
    
    # Plot fungsi f(x)
    ax.plot(x, y, label='f(x)', color='blue', linewidth=2)
    
    # Menambahkan garis horizontal di y = 0 untuk sumbu x
    ax.axhline(y=0, color='r', linestyle='--', linewidth=1)
    
    # Plot iterasi sebagai titik-titik hijau
    ax.scatter(x_values, [f(xi, persamaan) for xi in x_values], color='green', zorder=5, label='Iterasi')
    
    # Menambahkan label ke setiap titik iterasi
    for i, x_val in enumerate(x_values):
        ax.annotate(f'x{i+1}', (x_val, f(x_val, persamaan)), textcoords="offset points", xytext=(0, 10),
                    ha='center', fontsize=9, color='black', weight='bold')

    # Menambahkan grid untuk memudahkan pembacaan
    ax.grid(True, which='both', linestyle='--', linewidth=0.7, alpha=0.7)
    
    # Mengatur label dan judul plot
    ax.set_xlabel('x', fontsize=12)
    ax.set_ylabel('f(x)', fontsize=12)
    ax.set_title('Grafik Fungsi dan Iterasi Newton-Raphson', fontsize=14, weight='bold')
    
    # Menambahkan legenda
    ax.legend()
    
    # Menampilkan plot di Streamlit
    st.pyplot(fig)

