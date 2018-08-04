import time
import random
from tanyaJawab import *


def info():
    print("""

    Nia Bot Version 1.1.0
    adalah sebuah aplikasi
    bot chatting yang di buat
    khusus untuk para jomblo..

    Kalian akan berperan
    sebagai jomblo, dan Nia
    akan berperan sebagai
    teman gadis virtual kalian
    yang cantik dan baik..

    Nia akan menjawab semua
    kegelisahan dalam
    hidup kalian..

    Semoga Nia bisa
    menghibur kalian,
    disaat malam minggu tiba,
    dan Kalian hanya bisa
    mengelus dada memandangi
    disekitar kalian pasangan
    muda mudi bergandengan tangan.

    Biarlah nia menemani
    kesendirian kalian,
    tapi ingat jangan baper,
    nia hanyalah sebuah bot,
    yang tidak selalu bisa
    menjawab semua masalah kalian.

    Selamat menikmati
    aplikasi ini, dan support
    nia untuk menjadi lebih baik lagi.

    """)

    while True:
        x = input("tekan apapun untuk kembali: ")
        if x == "9" or x == "yes" or x == "Yes":
            break
        else:
            break


def peraturan():
    while True:

        print("""
            ====================
            =  N I A  -  B O T =
            ====================
               version 1.1.0
                 Create By
               MTID Dev Team""")

        time.sleep(2)

        print("""
        1. Untuk chat dengan Nia,
        silakan masukan pertanyaan kamu
        dengan diakhiri dengan tanda (?)
        """)
        time.sleep(2)

        print("""
        2. Tanda tanya (?) harus nempel
        dengan huruf terakhir, misal:

               siapa nama kamu?
        """)

        time.sleep(2)

        print("""
        3. Nia bersifat lugu dan terkesan
        malu - malu, jadi biasakan kamu yang
        bertanya duluan..
        """)

        time.sleep(2)

        print("""
        4. Nia menjawab semua pertanyaan yang
        bisa ia jawab, apabila dia tidak bisa
        menjawab, pakar cinta akan membantu
        menerangkan kepada anda apa yang
        harus anda lakukan.
        """)

        time.sleep(2)

        print("""
        5. Tulis pertanyaan yang jelas,
        dan tidak ambigu,
        agar nia bisa menjawab.
        """)

        time.sleep(2)

        print("""
        6. Harap bersabar,
        karena Nia hanyalah sebuah Bot,
        ia tidak bisa memenuhi
        semua keinginan anda..
        """)

        time.sleep(2)

        print("""
        7. Jangan baper,
        apalagi sampai jatuh hati
        beneran kepada Nia..
        bahaya sob..
        """)

        time.sleep(2)

        print("""
        8. Apabila anda sudah terlajur
        jatuh Cinta pada Nia,
        harap menghubungi PSIKIATER
        terdekat, kejombloan anda
        sudah akut..
        Bahaya untuk lingkunga sekitar.
        """)

        time.sleep(2)

        print("""
        9. Support terus
        MTID Developer Team,
        dalam membuat innovasi tebaru.
        """)

        time.sleep(2)

        print("""
        10. Terimakasih
        telah mencoba Niabot,
        semoga kesendirian anda
        lekas berakhir,
        semoga niabot bisa
        menjadi motivasi anda
        untuk lekas punya
        pasangan NYATA..
        """)

        time.sleep(2)

        print("""
        --- MTID DEVELOPER TEAM ---
        """)

        time.sleep(2)
        time.sleep(2)

        x = str(input("tekan apapun untuk kembali: "))
        # from niabot import niabot
        if x == "9" or x == "yes" or x == "Yes":
            niabot()
        else:
            niabot()


def startNia():

    rc = random.choice

    def tambah(func):
        func()
        print("-----------------------")

    while True:
        nb = "Nia bilang : \n"
        pakar = "Pakar Cinta bilang : "

        print("\n")
        x = str.lower(input("tulis sesuatu mblo..: "))

        print("\n")
        # print(x)
        print("Nia mengetik...")
        time.sleep(1)
        if x in tanyaNama:
            print("\n")

            def jw():
                print(nb + "\n" + rc(jawabNama))
            tambah(jw)
            print("\n")

        elif x in tanyaRumah:
            print("\n")

            def jw():
                print(nb + "\n" + rc(jawabRumah))
            tambah(jw)
            print("\n")

        elif x in tanyaGender:
            print("\n")

            def jw():
                print(nb + "\n" + rc(jawabGender))
            tambah(jw)
            print("\n")

        else:
            with open("tanyaJawab/niaBingung.txt", "r") as bingung:
                jawabBingung = bingung.read().splitlines()
                print(nb + rc(jawabBingung))


def creator():
    print("""
    ####################
    #     M T I D      #
    ####################
      D E V  - T E A M

        Fadli Selaz
        Budi Wibowo
        Tammy Suryana
        Ijal Apoy

    ingin berkontribusi?
    silakaan git clone
    https://github.com/fadliselaz/niabot
    """)

    x = str(input("tekan apapun untuk kembali: "))
    # from niabot import niabot
    if x == "9" or x == "yes" or x == "Yes":
        import niabot
    else:
        import niabot
