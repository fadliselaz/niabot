import random
import time


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

while True:
    x = str.lower(input("masukan pilihan kamu: "))
    if x == "1":
        import niaBot
    elif x == "2":
        import info
    elif x == "3":
        import peraturan
    elif x == "4":
        import creator
    elif x == "5":
        exit()
