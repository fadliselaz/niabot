# contoh untuk mencari suatu string pada list
import random
# untuk pertanyaan gunakan split() saja,
# jangan split lines, karena pertanyaan mengandung banyak string..

with open("tanyaNama.txt", "r") as tr:
    tanyaNama = tr.read().split()

with open("jawabNama.txt", "r") as jn:
    jawabNama = jn.read().splitlines()

with open("niaBingung.txt", "r") as nb:
    niaBingung = nb.read().splitlines()

# if tanyaNama.count("bodo") > 0:
#     print("ada coy")
#     print(tanyaNama)
# elif tanyaNama.count("contoh") > 0:
#     print("ada juga coy")
# else:
#     print("ngak ada..!!!")
#     print(tanyaNama)

while True:
    # print(tanyaNama)
    x = input("tanya : ")
    y = x.split()
    result = any(elem in tanyaNama for elem in y)
    if result:
        print(random.choice(jawabNama))
    else:
        print(random.choice(niaBingung))
