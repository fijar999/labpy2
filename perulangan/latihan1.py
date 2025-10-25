# latihan1.py
# perulangan
# menyatakan absensi kehadiran

# jika salah memasukan NIM akan terus terulang sampai NIM benar

b = "Fijar"
while True:
    nim = input("masukan NIM: ")

    if nim.lower() == "end":
        print("menutup absensi")
        break

    if nim == "312510227":
        print(f"{b} hadir.\n")
    else:
        print("tidak dalam daftar.\n")

print()