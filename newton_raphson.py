# Import pustaka sympy untuk melakukan operasi turunan dan time untuk animasi
from sympy import symbols, diff
import time
import sys

# Fungsi untuk menghitung nilai dari persamaan f(x)
def hitung_f(x, ekspresi):
    return eval(ekspresi)

# Fungsi untuk menghitung turunan numerik f'(x)
def turunan_f(x, ekspresi):
    delta = 1e-5
    return (hitung_f(x + delta, ekspresi) - hitung_f(x, ekspresi)) / delta

# Fungsi animasi loading
def animasi_loading(durasi):
    animasi = "|/-\\"
    for _ in range(durasi):
        for frame in animasi:
            sys.stdout.write('\rLoading' + frame)
            sys.stdout.flush()
            time.sleep(0.2)
    print("\rSelesai!        ")

# Fungsi untuk menampilkan halaman tombol "Start"
def tampilkan_halaman_start():
    print("\033[94m=" * 90)
    print("\t\t\t+++++~~~~> \033[95mIMPLEMENTASI METODE NEWTON RAPHSON\033[0m <~~~~+++++")
    print("\033[94m=" * 90)
    input("\033[96mTekan ENTER untuk memulai... \033[0m")

# Fungsi untuk menampilkan halaman loading
def tampilkan_halaman_loading():
    print("\nMemulai aplikasi...")
    for i in range(3, 0, -1):
        print(f"Loading dalam {i}...")
        time.sleep(1)
    animasi_loading(5)  # Menampilkan animasi loading

# Fungsi untuk menerapkan metode Newton-Raphson
def newton_raphson(x_awal, toleransi, ekspresi):
    xn = x_awal
    langkah = 0

    # Tampilkan header tabel
    print("="*90)
    print("|{:<10} |{:<20} |{:<20} |{:<26}|".format("Langkah", "Xn", "F(Xn)", "F'(Xn)"))
    print("="*90)

    while True:
        nilai_fx = hitung_f(xn, ekspresi)
        nilai_fprim = turunan_f(xn, ekspresi)

        print("|{:<10} |{:<20.6f} |{:<20.6f} |{:<26.6f}|".format(langkah + 1, xn, nilai_fx, nilai_fprim))

        # Menambahkan animasi loading saat menghitung setiap iterasi
        animasi_loading(5)

        # Mengecek kondisi berhenti
        if abs(nilai_fx) < toleransi:
            hasil = xn
            if hasil is not None:
                print("="*90)
                print("\n\t\t\t    \/\/\/\/\ <<[HASIL PENGIRAAN]>> /\/\/\/\/")
                print("="*90)
                print(f"\033[92mAkar penyelesaian (Xn): {hasil}\033[0m")  # Teks hijau untuk hasil
                print(f"\033[92mNilai fungsi (f(Xn)): {hitung_f(hasil, ekspresi)}\033[0m")  # Teks hijau
                print(f"\033[93mDitemukan pada langkah ke-{langkah + 1}\033[0m")  # Teks kuning
                print("="*90)
            else:
                print("Metode Newton-Raphson gagal mencapai konvergensi dalam batas toleransi yang diberikan.")

            return xn

        # Update nilai xn dengan pendekatan baru
        xn = xn - nilai_fx / nilai_fprim
        langkah += 1

# Menampilkan halaman tombol "Start"
tampilkan_halaman_start()

# Menampilkan halaman loading
tampilkan_halaman_loading()

# Mengambil input dari pengguna
ekspresi = input("\033[96mMasukkan fungsi f(x): \033[0m")
print(f"\033[93mFungsi yang dimasukkan: {ekspresi}\033[0m")
x = symbols('x')  # Mendefinisikan 'x' sebagai variabel simbolis
ekspresi_f = eval(ekspresi)  # Mengevaluasi fungsi f(x) dari input pengguna
ekspresi_turunan = diff(ekspresi_f, x)  # Menghitung turunan dari f(x)
print(f"\033[92mTurunan fungsi f'(x): {ekspresi_turunan}\033[0m")
x_awal = float(input("\033[96mMasukkan tebakan awal (X0): \033[0m"))
toleransi = float(input("\033[96mMasukkan toleransi error (e): \033[0m"))

# Memanggil fungsi newton_raphson untuk mencari solusi
hasil_akhir = newton_raphson(x_awal, toleransi, ekspresi)
