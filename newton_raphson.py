# newton_raphson.py
import numpy as np

# Fungsi untuk menghitung f(x) berdasarkan persamaan yang dimasukkan
def f(x, persamaan):
    return eval(persamaan)

# Fungsi untuk menghitung turunan f(x) 
def df(x, persamaan):
    h = 1e-5
    return (f(x + h, persamaan) - f(x, persamaan)) / h

# Metode Newton-Raphson
def metode_Newton_Raphson(x0, tol_e, persamaan):
    x = x0
    iterasi = 0
    results = []
    x_values = [x]

    while True:
        fx = f(x, persamaan)
        dfx = df(x, persamaan)

        results.append({"Iterasi": iterasi + 1, "Xn": x, "F(Xn)": fx, "F'(Xn)": dfx})

        if abs(fx) < tol_e:
            hasil = x
            results.append({"Iterasi": "Akar", "Xn": hasil, "F(Xn)": f(hasil, persamaan), "F'(Xn)": ""})
            break

        x = x - fx / dfx
        x_values.append(x)
        iterasi += 1

    return results, x_values
