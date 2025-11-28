import time
from datetime import date
from colorama import Fore, Style, Back

data = []        # Data user
current_user = ""
riwayat_file = "riwayat.txt"

# ============================================
# SIMPAN & LOAD USER
# ============================================
def simpan_user_ke_file():
    with open("user.txt", "w", encoding="utf-8") as f:
        for user, pw in data:
            f.write(f"{user},{pw}\n")

def load_user_dari_file():
    try:
        with open("user.txt", "r", encoding="utf-8") as f:
            for line in f:
                user, pw = line.strip().split(",")
                data.append([user, pw])
    except FileNotFoundError:
        pass

# Panggil load
load_user_dari_file()

# ============================================
# LOGIN & REGISTER
# ============================================
def login():
    global current_user

    while True:
        print("\n=== LOGIN ===")
        user = input("Masukan User : ")
        pw = input("Masukan Password : ")

        if [user, pw] in data:
            current_user = user
            print("Login Berhasil!\n")
            return True
        else:
            print("Akun tidak ditemukan!\n")
            return False

def register():
    print("\n=== REGISTRASI ===")
    user = input("Masukan Username : ")
    pw = input("Masukan Password : ")
    konfirmasi = input("Konfirmasi Password : ")

    while konfirmasi != pw:
        print("Password tidak sama, coba lagi!")
        konfirmasi = input("Konfirmasi Password : ")

    data.append([user, pw])
    simpan_user_ke_file()
    print("Akun berhasil dibuat!\n")

# ============================================
# DATA PRODUK
# ============================================
produk = {
    1: "Mesin Cuci",
    2: "Kulkas",
    3: "AC",
    4: "Dispenser",
    5: "Television",
}

harga = {
    1: 5000000,
    2: 5000000,
    3: 4000000,
    4: 1200000,
    5: 2000000,
}

kurir = {
    1: "Ambil di toko",
    2: "Kurir Instan",
    3: "Kurir Reguler",
}

# ============================================
# MENAMPILKAN PRODUK
# ============================================
def tampilkan_produk():
    print("="*60)
    print("                     ELEKTRONIK KITA")
    print("="*60)
    print("Id | Nama Produk        | Harga")
    print("-"*60)
    for i in produk:
        print(f"{i:<3}| {produk[i]:18} | Rp {harga[i]:,}")
    print("-"*60)

# ============================================
# FUNGSI BELANJA
# ============================================
def belanja():
    keranjang = []
    tampilkan_produk()

    while True:
        pilih_id = int(input("Pilih Id Produk: "))
        if pilih_id not in produk:
            print("Id tidak valid!")
            continue

        jumlah = int(input(f"Jumlah {produk[pilih_id]}: "))

        keranjang.append({
            "produk": produk[pilih_id],
            "harga": harga[pilih_id],
            "jumlah": jumlah
        })

        lagi = input("Tambah produk lain? (Y/N): ")
        if lagi.lower() != "y":
            break

    # DATA PENERIMA
    nama = input("Nama Penerima : ")
    alamat = input("Alamat        : ")
    tlp = input("No HP         : ")

    # HITUNG TOTAL
    total_barang = sum(item["harga"] * item["jumlah"] for item in keranjang)

    # DISKON
    if total_barang >= 20000000:
        diskon = total_barang * 0.10
    elif total_barang >= 10000000:
        diskon = total_barang * 0.05
    else:
        diskon = 0

    # METODE PENGIRIMAN
    print("\n=== METODE PENGIRIMAN ===")
    for i in kurir:
        print(f"{i}. {kurir[i]}")

    pilih_kirim = int(input("Pilih: "))

    if pilih_kirim == 1:
        metode_kirim = "Ambil di Toko"
        ongkir = 0
        estimasi = "Langsung Bisa Diambil"
    elif pilih_kirim == 2:
        metode_kirim = "Kurir Instan"
        ongkir = 70000
        estimasi = "Dikirim Langsung"
    else:
        metode_kirim = "Kurir Reguler"
        ongkir = 40000
        estimasi = "Tiba ± 5 Jam"

    total_bayar = total_barang - diskon
    total_akhir = total_bayar + ongkir

    # PEMBAYARAN
    print("\n=== PEMBAYARAN ===")
    print(f"Total Harga : Rp {total_barang:,}")
    print(f"Diskon      : Rp {diskon:,}")
    print(f"Ongkir      : Rp {ongkir:,}")
    print(f"Total Bayar : Rp {total_akhir:,}")

    while True:
        bayar = int(input("Masukan Jumlah Bayar: "))

        if bayar >= total_akhir:
            kembalian = bayar - total_akhir
            print("\nPembayaran Berhasil!")
            break
        else:
            print("Uang kurang!")

    # CETAK STRUK
    cetak_struk(keranjang, nama, alamat, tlp, metode_kirim, estimasi, diskon, total_bayar, ongkir, total_akhir, bayar, kembalian)

# ============================================
# CETAK STRUK + SIMPAN RIWAYAT
# ============================================
def cetak_struk(keranjang, nama, alamat, tlp, metode_kirim, estimasi, diskon, total_bayar, ongkir, total_akhir, bayar, kembalian):

    tgl = date.today()

    print("\nStruk berhasil dicetak ke riwayat.txt")

    with open(riwayat_file, "a", encoding="utf-8") as s:

        s.write("===================== ELEKTRONIK KITA ======================\n")
        s.write(f"{tgl}\n")
        s.write(f"Nama Pengguna : {current_user}\n")
        s.write(f"Nama Penerima : {nama}\n")
        s.write(f"Alamat        : {alamat}\n")
        s.write(f"No HP         : {tlp}\n")
        s.write(f"Pengantaran   : {metode_kirim}\n")
        s.write(f"Estimasi      : {estimasi}\n")
        s.write("------------------------------------------------------------\n")

        for i, item in enumerate(keranjang, start=1):
            subtotal = item['harga'] * item['jumlah']
            s.write(f"{i}. {item['produk']} x{item['jumlah']} = Rp {subtotal:,}\n")

        s.write("------------------------------------------------------------\n")
        s.write(f"Diskon       : Rp {diskon:,}\n")
        s.write(f"Total Bayar  : Rp {total_bayar:,}\n")
        s.write(f"Ongkir       : Rp {ongkir:,}\n")
        s.write(f"Total Akhir  : Rp {total_akhir:,}\n")
        s.write(f"Uang Anda    : Rp {bayar:,}\n")
        s.write(f"Kembalian    : Rp {kembalian:,}\n")
        s.write("============================================================\n\n")

# ============================================
# MENU UTAMA
# ============================================
def menu_utama():
    while True:
        print("\n===== MENU UTAMA =====")
        print("1. Belanja")
        print("2. Lihat Produk")
        print("3. Logout")
        print("4. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            belanja()

        elif pilihan == "2":
            tampilkan_produk()

        elif pilihan == "3":
            print("Logout berhasil!\n")
            return  # kembali ke menu login

        elif pilihan == "4":
            print("Terima kasih telah menggunakan aplikasi!")
            exit()
        else:
            print("Pilihan tidak valid!")

# ============================================
# PROGRAM UTAMA
# ============================================
while True:
    print("\n====== SELAMAT DATANG ======")
    print("1. Login")
    print("2. Register")
    print("3. Keluar")

    pilih = input("Pilih menu: ")

    if pilih == "1":
        if login():
            menu_utama()

    elif pilih == "2":
        register()

    elif pilih == "3":
        print("Terima kasih!")
        break

    else:
        print("Pilihan tidak valid!")
