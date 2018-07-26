import random

#Zar tahmini yapan program
# Eger dogruysa puanı 1 arttıran yanlissa 1 azaltan program
def menu():
    print("""1-oyna\n2-çıkış""")

    secim = int(input("secim yap:"))
    while True:
        if secim == 1:
            zar_at()
        elif secim == 2:
            break
        else:
            print("yanlıs secim")


def zar_at():
    puan = 0
    while True:
        sayi = random.randint(1, 6)
        # print("uretilen:{}".format(sayi))
        tahminin = int(input("tahmin:"))
        if sayi == tahminin:
            print("dogru bildin")
            puan += 1
        else:
            print("yanlıs bildin")
            puan -= 1
        print("puanın:{}".format(puan))


def main():
    menu()


main()