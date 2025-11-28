import time
from datetime import timedelta
from datetime import date
from colorama import Fore, Style, Back

produk = {
    1: "Mesin Cuci",
    2: "Kulkas    ",
    3: "AC        ",
    4: "Dispenser ",
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




keranjang = []

print("="*70)
print("                          ELEKTRONIK KITA                             ")
print("="*70)

print("Id | Nama Produk        | Harga")
print("-"*70)
for i in produk:
    print(f"{i:<3}| {produk[i]:18} | Rp {harga[i]:,}")
print("-"*70)

# ============================
# INPUT PRODUK
# ============================
while True:
    pilih_id = int(input("Pilih Id produk: "))
    if pilih_id not in produk:
        print("Id tidak valid!")
        continue

    jumlah = int(input(f"Masukan Jumlah Pembelian {produk[pilih_id]}: "))

    keranjang.append({
        "produk": produk[pilih_id],
        "harga": harga[pilih_id],
        "jumlah": jumlah
    })

    lagi = input("Tambah produk lain? (Y/N): ")
    if lagi.lower() != "y":
        break

print("-"*70)
nama = input("Nama Penerima : ")
alamat = input("Alamat Penerima : ")
tlp = input("No Hp: ")

total_barang = 0

# ============================
# TAMPILKAN DETAIL PRODUK
# ============================
print("="*70)
print("No | Nama Barang        | Harga Satuan   | Jumlah | Total")
print("-"*70)

no = 1
for item in keranjang:
    subtotal = item["harga"] * item["jumlah"]
    total_barang += subtotal

    print(f"{no:<3}| {item['produk']:18} | Rp {item['harga']:12,} | {item['jumlah']:6} | Rp {subtotal:,}")
    no += 1

print("-"*70)

# ============================
# DISKON
# ============================
if total_barang >= 20000000:
    diskon = int(total_barang * 0.10)
    persen = "10%"
elif total_barang >= 10000000:
    diskon = int(total_barang * 0.05)
    persen = "5%"
else:
    diskon = 0
    persen = "0%"

# ============================
# METODE PENGIRIMAN
# ============================
print("\n============================================================")
print("                      Metode Pengiriman                       ")
print("="*60)

for i in kurir:
    print(f"{i:<3}| {kurir[i]}")
print("-"*60)

pilih_kirim = int(input("Pilih metode pengantaran: "))

if pilih_kirim == 1:
    metode_kirim = "Ambil di Toko"
    ongkir = 0
    estimasi = "Langsung Bisa Diambil"
elif pilih_kirim == 2:
    metode_kirim = "Kurir Instan"
    ongkir = 70000
    estimasi = "Dikirim Langsung"
elif pilih_kirim == 3:
    metode_kirim = "Kurir Reguler"
    ongkir = 40000
    estimasi = "Tiba ± 5 Jam"
else:
    metode_kirim = "Ambil di Toko"
    ongkir = 0
    estimasi = "Langsung Bisa Diambil"

total_bayar = total_barang - diskon
total_akhir = total_bayar + ongkir


print("-"*60)
print(f"Jumlah Bayar  : Rp {total_barang:,.0f}")
print(f"Diskon {persen:<4}   : Rp {diskon:,.0f}")
print(f"Total Bayar   : Rp {total_bayar:,.0f}")
print(f"Ongkir        : Rp {ongkir:,.0f}")
print(f"Total Akhir   : Rp {total_akhir:,.0f}")
print("-"*60)

# ============================
# LOADING
# ============================
tgl = date.today()
tgl_garansi = tgl.replace(year = tgl.year + 2)
for i in range(1, 11):
    print(f"Loading: {i*10}%", end="\r")
    time.sleep(0.2)

konfir = input("\nApakah anda yakin ingin melakukan pembayaran? (Y/N): ")

if konfir.lower() == "y":
    while True:
        bayar = int(input("Masukan Jumlah Bayar : "))

        if bayar > total_akhir:
            kembalian = bayar - total_akhir
            print("\nPembayaran Berhasil!")
            print(f"Anda Membayar Sebesar Rp.{bayar:,.0f}")
            print(f"Kembalian Anda : Rp.{kembalian:,.0f}")
            break

        elif bayar == total_akhir:
            print("\nPembayaran Berhasil!")
            print(f"Anda Membayar Sebesar Rp.{bayar:,.0f}")
            print("Uang Anda Pas")
            break

        else:
            print("Uang Anda Kurang! Silakan masukan ulang.")
else:
    print("\nPembayaran dibatalkan")

# ============================
# STRUK
# ============================
print(Back.WHITE + "")
print(Fore.YELLOW + "\n===================== ELEKTRONIK KITA ======================")
print(tgl)
print("\nNama Penerima :", nama)
print("Alamat        :", alamat)
print("No HP         :", tlp)
print("Pengantaran   :", metode_kirim)
print("Estimasi      :", estimasi)
print("-"*60)

no = 1
for item in keranjang:
    print(f"{no}. {item['produk']} x{item['jumlah']}  = Rp {(item['harga'] * item['jumlah']):,}")
    no += 1

print("-"*60)
print(f"Diskon       : Rp {diskon:,.0f}")
print(f"Total Bayar  : Rp {total_bayar:,.0f}")
print(f"Ongkir       : Rp {ongkir:,.0f}")
print(f"Total Akhir  : Rp {total_akhir:,.0f}")
print(f"Uang Anda    : Rp.{bayar:,.0f}")
print(f"Kembalian    : Rp.{kembalian:,.0f}")
print("\n                       TERIMA KASIH")
print(f"PERHATIAN! MASA GARANSI ANDA BERLAKU 2 TAHUN, MAKA TANGGAL KADALUARSA GARANSI ANDA : {tgl_garansi}")
print(Style.RESET_ALL)



