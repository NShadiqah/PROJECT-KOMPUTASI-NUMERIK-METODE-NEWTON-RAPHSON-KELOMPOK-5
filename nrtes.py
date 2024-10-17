import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from sympy import symbols, diff

# Function untuk menghitung nilai f(x)
def f(x, persamaan):
    return eval(persamaan)

# Function untuk mencari f'(x)
def df(x, persamaan):
    h = 1e-5
    return (f(x + h, persamaan) - f(x, persamaan)) / h

# Function untuk metode Newton Raphson
def metode_Newton_Raphson(x0, tol_e, persamaan):
    x = x0
    iterasi = 0
    results = []

    while True:
        fx = f(x, persamaan)
        dfx = df(x, persamaan)

        # Menyimpan hasil ke dalam list
        results.append((iterasi + 1, x, fx, dfx))

        if abs(fx) < tol_e:
            hasil = x
            results.append(("Akar", hasil, f(hasil, persamaan), ""))
            break

        x = x - fx / dfx
        iterasi += 1

    return results

# Function untuk menampilkan hasil
def calculate():
    persamaan = entry_persamaan.get()
    tebakan_awal = float(entry_tebakan.get())
    toleransi_e = float(entry_toleransi.get())

    x = symbols('x')
    in_fx = eval(persamaan)
    out_df = diff(in_fx, x)

    # Menjalankan metode Newton Raphson
    results = metode_Newton_Raphson(tebakan_awal, toleransi_e, persamaan)

    # Menghapus data lama di treeview
    for item in tree.get_children():
        tree.delete(item)

    # Menambahkan hasil ke treeview
    for result in results:
        tree.insert("", tk.END, values=result)

# Setup UI
root = tk.Tk()
root.title("Kalkulator Metode Newton Raphson")

# Input field for the equation
tk.Label(root, text="Masukkan persamaan (f(X)):").pack()
entry_persamaan = tk.Entry(root)
entry_persamaan.pack()

# Input field for initial guess
tk.Label(root, text="Masukkan tebakan awal (X0):").pack()
entry_tebakan = tk.Entry(root)
entry_tebakan.pack()

# Input field for tolerance
tk.Label(root, text="Masukkan toleransi error (e):").pack()
entry_toleransi = tk.Entry(root)
entry_toleransi.pack()

# Button to calculate
calculate_button = tk.Button(root, text="Hitung", command=calculate)
calculate_button.pack()

# Tabel untuk menampilkan hasil
tree = ttk.Treeview(root, columns=("Iterasi", "Xn", "F(Xn)", "F'(Xn)"), show="headings")
tree.heading("Iterasi", text="Iterasi")
tree.heading("Xn", text="Xn")
tree.heading("F(Xn)", text="F(Xn)")
tree.heading("F'(Xn)", text="F'(Xn)")
tree.pack()

# Run the application
root.mainloop()
