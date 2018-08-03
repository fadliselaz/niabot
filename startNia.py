def startNia():
    import random
    import time
    import tanyaJawab
    from tanyaRumah import tanyaRumah

    rc = random.choice

    while True:
        nb = "Nia bilang : "
        pc = "Pakar Cinta bilang : "

        print("\n")
        x = str.lower(input("tulis sesuatu mblo..: "))

        print("\n")
        # print(x)
        print("Nia mengetik...")
        time.sleep(1)
        if x in tanyaNama:
            print("\n")
            print(nb + rc(jawabNama))
            print("\n")


        else:
            print("\n")
            print(nb + rc(niaBingung))
            time.sleep(2)
            print("\n")
            print(pc + rc(pc))
            print("\n")
