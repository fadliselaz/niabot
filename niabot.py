import random
import time
from functions import *


while True:
    print("""
    ====================
    =  N I A  -  B O T =
    ====================
       version 1.1.0
         Create By
       MTID Dev Team

    ----------------------
    pilih menu dibawah ini
    ----------------------
    1 . Chatting dengan Nia
    2 . info / Apa sih ini?
    3 . Peraturan
    4 . Creator
    5 . Keluar
    """)
    x = str.lower(input("masukan pilihan kamu: "))
    if x == "1":
        startNia()

    elif x == "2":
        info()

    elif x == "3":
        peraturan()

    elif x == "4":
        creator()

    elif x == "5":
        exit()
