import smtplib

file = "receiver_list.txt"

# command untuk menambah list email ke txt file
def input_email():
        finput = open(file, 'a+')
        email = input("Tambahkan List Email Penerima: ")
        finput.write('\n'+email)
        print("Email berhasil ditambah.")
        print("=============================================")

#command untuk melihat data email penerima
def show_email_list():
        fshow = open(file, 'r')
        contents = fshow.read()
        print("=============================================")
        print("LIST EMAIL PENERIMA: ")
        print(contents)
        print("=============================================")
        fshow.close()

# referensi : https://www.youtube.com/watch?v=sXjpkcF7rPQ&ab_channel=johangodinho
def send_email():
        femail = open(file, 'r')
        rec_list = [] #referensi: https://www.kite.com/python/answers/how-to-convert-each-line-in-a-text-file-into-a-list-in-python
        for line in femail:
            stripped_line = line.strip()
            line_list = stripped_line.split()
            rec_list.append(line_list)
        sender_email = input(str("Masukkan Email Gmail Anda: "))
        sender_password = input(str("Masukkan Password Gmail Anda: "))
        print("Logging in...")
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, sender_password)
        print("LOGIN SUCCESSFUL!")
        recepient = rec_list
        subject = input(str("Subject Email: "))
        body = input(str("Message (Tekan 'Enter' untuk kirim): "))
        message = f"Subject: {subject}\n\n{body}"
        print("Mengirim Email...")
        server.sendmail(sender_email, recepient, message)
        print("Email Berhasil Dikirim!")
        server.quit()


#untuk menu
while True:
    print("SILAHKAN PILIH MENU")
    print("1. Menambah List Email Penerima")
    print("2. Lihat List Email Penerima")
    print("3. Kirim Email ke Semua Email Penerima")
    print("4. Keluar Program")
    input_menu = input("Pilih menu: ")
    if input_menu == "1":
        input_email()
    elif input_menu == "2":
        show_email_list()
    elif input_menu == "3":
        send_email()
    elif input_menu == "4":
        print("Program Selesai")
        break
    else:
        print("Menu Tidak Tersedia, coba lagi!")

