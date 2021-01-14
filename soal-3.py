print("Silahkan input nilai teori dan praktek Anda untuk mengecek kelulusan.")
teo = float(input("Input nilai Ujian Teori  : "))
pra = float(input("Input nilai Ujian Praktek: "))

if    teo >= 70 and pra >= 70:
        print("Selamat Anda Lulus!")
elif  teo >= 70 and pra < 70:
        print("Anda harus mengulang Ujian Praktek.")
elif  teo < 70 and pra >= 70:
        print("Anda harus mengulang Ujian Teori")
else: #teo < 70 and pra < 70
        print("Anda harus mengulang Ujian Praktek dan Teori.")