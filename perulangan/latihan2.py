# latihan2.py
# perulangan
# menentukan bilangan ganjil/genap

while True:
    angka = input("masukan angka: ")

    if angka == "end":
        print("menutup")
        break

    if angka.isdigit():
        angka = int(angka)
        if angka % 2 == 0:
            print(f"{angka} adalah bilangan genap.\n")
        else:
            print(f"{angka} adalah bilangan ganjil.\n")
    else:
        print("input tidak valid! silahkan memasukan angka atau 'end' untuk keluar.\n")

