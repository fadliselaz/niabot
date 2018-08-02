def startNia():
    import random
    import time
    import tanyaJawab as tj

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
        if x in tj.listTanya1:
            print("\n")
            print(nb + rc(tj.jawab1))
            print("\n")

        elif x in tj.listTanya2:
            print("\n")
            print(nb + rc(tj.jawab2))
            print("\n")

        elif x in tj.listTanya3:
            print("\n")
            print(nb + rc(tj.jawab3))
            print("\n")

        else:
            print("\n")
            print(nb + rc(tj.niaBingung))
            time.sleep(2)
            print("\n")
            print(pc + rc(tj.pc))
            print("\n")
