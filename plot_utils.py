# plot_utils.py
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
from newton_raphson import f

# Fungsi untuk menampilkan grafik:
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
