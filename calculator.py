import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from sympy import symbols, lambdify, diff, sympify

# Function untuk menghitung f(x) dan f'(x) menggunakan sympy
def hitung_fungsi(persamaan_str):
    try:
        x = symbols('x')
        persamaan = sympify(persamaan_str)
        f = lambdify(x, persamaan, 'numpy')
        df = lambdify(x, diff(persamaan, x), 'numpy')
        return f, df, None
    except Exception as e:
        return None, None, f"Error dalam parsing persamaan: {e}"

# Function untuk metode Newton Raphson
def metode_Newton_Raphson(x0, tol_e, f, df):
    x = x0
    iterasi = 0
    results = []

    while True:
        fx = f(x)
        dfx = df(x)

        # Menyimpan hasil ke dalam list
        results.append((iterasi + 1, round(x, 6), round(fx, 6), round(dfx, 6)))

        # Jika fx mendekati 0 atau dfx == 0 (untuk mencegah pembagian dengan nol)
        if abs(fx) < tol_e or dfx == 0:
            hasil = x
            results.append(("Akar", round(hasil, 6), round(f(hasil), 6), ""))
            break

        # Newton-Raphson formula: x = x - f(x) / f'(x)
        x = x - fx / dfx
        iterasi += 1

    return results

# Function untuk menampilkan hasil
def calculate():
    persamaan = entry_persamaan.get()
    try:
        tebakan_awal = float(entry_tebakan.get())
        toleransi_e = float(entry_toleransi.get())
    except ValueError:
        messagebox.showerror("Input Error", "Pastikan tebakan awal dan toleransi error berupa angka!")
        return

    # Menghitung f(x) dan f'(x) menggunakan sympy
    f, df, error_message = hitung_fungsi(persamaan)

    if error_message:
        messagebox.showerror("Error", error_message)
        return

    # Menjalankan metode Newton Raphson
    try:
        results = metode_Newton_Raphson(tebakan_awal, toleransi_e, f, df)
    except ZeroDivisionError:
        messagebox.showerror("Error", "Terjadi pembagian dengan nol, coba tebakan awal yang lain.")
        return

    # Menghapus data lama di treeview
    for item in tree.get_children():
        tree.delete(item)

    # Menambahkan hasil ke treeview
    for result in results:
        tree.insert("", tk.END, values=result)

# Setup UI
root = tk.Tk()
root.title("Kalkulator Metode Newton-Raphson")

# Frame untuk input
frame_input = tk.Frame(root)
frame_input.pack(pady=10)

# Input field for the equation
tk.Label(frame_input, text="Masukkan persamaan (f(x)):", anchor="w").grid(row=0, column=0, sticky="w")
entry_persamaan = tk.Entry(frame_input, width=30)
entry_persamaan.grid(row=0, column=1, padx=10)

# Input field for initial guess
tk.Label(frame_input, text="Masukkan tebakan awal (x0):", anchor="w").grid(row=1, column=0, sticky="w")
entry_tebakan = tk.Entry(frame_input)
entry_tebakan.grid(row=1, column=1, padx=10)

# Input field for tolerance
tk.Label(frame_input, text="Masukkan toleransi error (e):", anchor="w").grid(row=2, column=0, sticky="w")
entry_toleransi = tk.Entry(frame_input)
entry_toleransi.grid(row=2, column=1, padx=10)

# Button to calculate
calculate_button = tk.Button(root, text="Hitung", command=calculate)
calculate_button.pack(pady=10)

# Tabel untuk menampilkan hasil
columns = ("Iterasi", "Xn", "F(Xn)", "F'(Xn)")
tree = ttk.Treeview(root, columns=columns, show="headings", height=10)
tree.heading("Iterasi", text="Iterasi")
tree.heading("Xn", text="Xn")
tree.heading("F(Xn)", text="F(Xn)")
tree.heading("F'(Xn)", text="F'(Xn)")

# Pengaturan ukuran kolom
tree.column("Iterasi", width=80, anchor="center")
tree.column("Xn", width=100, anchor="center")
tree.column("F(Xn)", width=150, anchor="center")
tree.column("F'(Xn)", width=150, anchor="center")
tree.pack(padx=10, pady=10)

# Run the application
root.mainloop()
