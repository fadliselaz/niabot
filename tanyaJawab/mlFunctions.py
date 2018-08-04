def niaMl():
    print("""
    ************************
    * Nia Machine Learning *
    ************************

    Penambahan pertanyaan,
    dan jawaban Nia..

    Silakan masukan Tema
    pertanyaan yang anda
    mau tambahkan..

    1. Nama
    2. Rumah
    3. Gender

    """)

    while True:
        x = input("Masukan pilhan anda: ")
        if "1" in x:
            tanyaNama()
        elif "2" in x:
            tanyaRumah()
        elif "3" in x:
            tanyaGender()

        else:
            exit()


def tanyaGender():
    with open("tanyaGender.txt", "a") as tn:
        print("silakan tanyakan pertanyaan \nmengenai Gender.. \nTekan 9 untuk keluar")
        while True:
            x = input("tanya Gender: ")
            if x == "9":

                niaMl()
            else:
                tn.write(x + "?" + "\n")

def tanyaNama():
    with open("tanyaNama.txt", "a") as tn:
        print("silakan tanyakan pertanyaan \nmengenai Nama.. \nTekan 9 untuk keluar")
        while True:
            x = input("tanya Nama: ")
            if x == "9":

                niaMl()
            else:
                tn.write(x + "?" + "\n")

def tanyaRumah():
    with open("tanyaRumah.txt", "a") as tn:
        print("silakan tanyakan pertanyaan \nmengenai Rumah.. \nTekan 9 untuk keluar")
        while True:
            x = input("tanya Rumah: ")
            if x == "9":
                niaMl()
            else:
                tn.write(x + "?" + "\n")
