data = []   

def masukan_user():
    user = input("Masukan User : ")
    pw = input("Masukan Password : ")

    if [user, pw] in data:
        print("Login Berhasil!\n")
        return True
    else:
        print("Akun tidak ditemukan!\n")
        return False
        

def buat_akun():
    user = input("Masukan User : ")
    pw = input("Masukan Password : ")
    konfirmasi = input("Konfirmasi Password : ")

    while konfirmasi != pw:
        print("Password tidak sama, coba lagi!")
        konfirmasi = input("Konfirmasi Password : ")

    data.append([user, pw])
    print("Akun berhasil dibuat!\n")

while True:
    akun = input("Sudah Punya Akun [Y/N] : ").lower()

    if akun == "y":
        if masukan_user():   
            break

    elif akun == "n":
        buat_akun()
        print("Silakan login kembali.\n")  

    else:
        print("Pilihan tidak valid!\n")


film_Weekday = {
    "1": ["Kapten Kapten", 100000],
    "2": ["Mantap Bosku", 50000],
    "3": ["Ea Ea Eaaaa", 75000]
}

film_Weekend = {
    "1": ["Kapten Kapten", 100000],
    "2": ["Mantap Bosku", 50000],
    "3": ["Ea Ea Eaaaa", 75000],
    "4": ["Anjay Gurinjay", 120000],
    "5": ["Kurang Gizi", 25000]
}

print("---------- Selamat Datang di Bioskop! -----------")
hari = input("Mau Hari Apa [Senin - Minggu ]: ").lower()


if hari in ["senin", "selasa", "rabu", "kamis", "jumat"]:
    print("\nSilakan Pilih Judul Film!")
    for kode, info in film_Weekday.items():
        print(f"{kode}. {info[0]} - Rp.{info[1]:,.0f}")

    pilihan = input("\nMasukkan kode film: ")
    jumlah = int(input("Jumlah Beli : "))

    if pilihan in film_Weekday:
        judul = film_Weekday[pilihan][0]
        harga = jumlah * film_Weekday[pilihan][1]
        print(f"\nKamu memilih film: {judul}")
        print(f"Harga tiket: Rp {harga:,.0f}")
    else:
        print("\nKode film tidak ditemukan!")


elif hari in ["sabtu", "minggu"]:
    print("\nSilakan Pilih Judul Film!")
    for kode, info in film_Weekend.items():
        print(f"{kode}. {info[0]} - Rp.{info[1]}")

    pilihan = input("\nMasukkan kode film: ")
    jumlah = int(input("Jumlah Beli : "))

    if pilihan in film_Weekend:
        judul = film_Weekend[pilihan][0]
        harga = jumlah * film_Weekend[pilihan][1]
        diskon = harga * 0.1
        total = harga - diskon
        print(f"\nKamu memilih film: {judul}")
        print(f"Harga tiket: Rp.{harga:,.0f}")
        print(f"Diskon : Rp.{diskon:,.0f}")
        print(f"Total Harga : Rp.{total:,.0f}")
    else:
        print("\nKode film tidak ditemukan!")

print("-"*50)
