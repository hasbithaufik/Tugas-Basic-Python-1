print("=====SELAMAT DATANG=====\n")
namauser = []
kontakuser = []


def input_data():
        nama = str(input("Input Nama: "))
        namauser.append(nama)
        kontak = str(input("Input Nomor Kontak: "))
        kontakuser.append(kontak)
        print("====================")
        print("Data sudah ditambah!")
        print("====================")

def print_data():
    print("======DAFTAR KONTAK USER======")
    for i in range(len(namauser)):
        print(f"-----User ke: {i+1}-----")
        print("Nama: {}".format(namauser[i]))
        print("Kontak: {}".format(kontakuser[i]))
        print("-------------------------")

while True:
    print("Silahkan pilih menu: ")
    print("1. Perlihatkan Daftar Kontak")
    print("2. Tambah Daftar Kontak")
    print("3. Keluar\n")
    input_menu = int(input("Pilih Menu: "))
    if input_menu == 1:
        print_data()
    elif input_menu == 2:
        input_data()
    elif input_menu == 3:
        print("Program Selesai, Sampai Jumpa! ")
        break
    else:
        print("Menu tidak tersedia, coba lagi!")

