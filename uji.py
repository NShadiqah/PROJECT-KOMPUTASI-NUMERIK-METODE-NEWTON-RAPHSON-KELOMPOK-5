import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from sympy import symbols, diff
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import time
import sys
import os

def f(x, persamaan):
    return eval(persamaan)

def df(x, persamaan):
    h = 1e-5
    return (f(x + h, persamaan) - f(x, persamaan)) / h

def metode_Newton_Raphson(x0, tol_e, persamaan):
    x = x0
    iterasi = 0
    results = []
    x_values = [x]

    while True:
        fx = f(x, persamaan)
        dfx = df(x, persamaan)

        results.append((iterasi + 1, x, fx, dfx))

        if abs(fx) < tol_e:
            hasil = x
            results.append(("Akar", hasil, f(hasil, persamaan), ""))
            break

        x = x - fx / dfx
        x_values.append(x)
        iterasi += 1

    return results, x_values

def calculate():
    try:
        persamaan = entry_persamaan.get()
        tebakan_awal = float(entry_tebakan.get())
        
        # Handle tolerance input for both dot and comma
        toleransi_e_str = entry_toleransi.get().replace(',', '.')
        toleransi_e = float(toleransi_e_str)

        x = symbols('x')
        in_fx = eval(persamaan)
        out_df = diff(in_fx, x)

        results, x_values = metode_Newton_Raphson(tebakan_awal, toleransi_e, persamaan)

        for item in tree.get_children():
            tree.delete(item)

        for result in results:
            tree.insert("", tk.END, values=result)

        plot_function(persamaan, x_values)
    except ValueError as e:
        messagebox.showerror("Input Error", f"Invalid input: {e}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def plot_function(persamaan, x_values):
    fig, ax = plt.subplots(figsize=(8, 6))
    
    x = np.linspace(min(x_values) - 1, max(x_values) + 1, 1000)
    y = [f(xi, persamaan) for xi in x]
    
    ax.plot(x, y, label='f(x)')
    ax.axhline(y=0, color='r', linestyle='--')
    ax.scatter(x_values, [f(xi, persamaan) for xi in x_values], color='green', label='Iterasi')
    
    for i, txt in enumerate(range(1, len(x_values) + 1)):
        ax.annotate(f'x{txt}', (x_values[i], f(x_values[i], persamaan)))
    
    ax.legend()
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')
    ax.set_title('Grafik Fungsi dan Iterasi Newton-Raphson')
    
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack()

def animasi_loading(durasi):
    animasi = "|/-\\"
    for _ in range(durasi):
        for frame in animasi:
            sys.stdout.write('\rLoading' + frame)
            sys.stdout.flush()
            time.sleep(0.2)
    print("\rSelesai!        ")

def tampilkan_halaman_start():
    print("\033[94m=" * 84)
    print("\t     +++++~>\033[95mIMPLEMENTASI METODE NEWTON RAPHSON\033[0m <~+++++")
    print("\033[94m=" * 84)
    input("\033[96mTekan ENTER untuk memulai... \033[0m")

def tampilkan_halaman_loading():
    print("\nMemulai aplikasi...")
    for i in range(3, 0, -1):
        print(f"Loading dalam {i}...")
        time.sleep(1)
    animasi_loading(5)  # Menampilkan animasi loading
    os.system('cls' if os.name == 'nt' else 'clear')

def start_application():
    tampilkan_halaman_start()
    tampilkan_halaman_loading()
    root.deiconify()  # Menampilkan window Tkinter

root = tk.Tk()
root.title("Kalkulator Metode Newton Raphson dengan Grafik")
root.withdraw()  # Menyembunyikan window Tkinter sementara

tk.Label(root, text="Masukkan persamaan (f(x)):").pack()
entry_persamaan = tk.Entry(root)
entry_persamaan.pack()

tk.Label(root, text="Masukkan tebakan awal (x0):").pack()
entry_tebakan = tk.Entry(root)
entry_tebakan.pack()

tk.Label(root, text="Masukkan toleransi error (e):").pack()
entry_toleransi = tk.Entry(root)
entry_toleransi.pack()

calculate_button = tk.Button(root, text="Hitung", command=calculate)
calculate_button.pack()

tree = ttk.Treeview(root, columns=("Iterasi", "Xn", "F(Xn)", "F'(Xn)"), show="headings")
tree.heading("Iterasi", text="Iterasi")
tree.heading("Xn", text="Xn")
tree.heading("F(Xn)", text="F(Xn)")
tree.heading("F'(Xn)", text="F'(Xn)")
tree.pack()

start_application()
root.mainloop()

