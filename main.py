from Autokolcsonzo import Autokolcsonzo
from Szemelyauto import Szemelyauto
from Teherauto import Teherauto
from datetime import datetime, date
from Auto import Auto


# Előkészítés
kolcsonzo = Autokolcsonzo("Autó kölcsönző")

def elokeszites():
    kolcsonzo.auto_felvetel(Szemelyauto("ABC123", "Opel", 30000, 5, 2000))
    kolcsonzo.auto_felvetel(Teherauto("ERT456", "Ford", 25000, 2, 4500))
    kolcsonzo.auto_felvetel(Szemelyauto("JKB742", "Skoda", 35000, 5, 1500))

    kolcsonzo.auto_berles(kolcsonzo.autok[0], 2, datetime(2025, 5, 21))
    kolcsonzo.auto_berles(kolcsonzo.autok[1], 3, datetime(2025, 4, 20))
    kolcsonzo.auto_berles(kolcsonzo.autok[2], 5, datetime(2025, 4, 28))
    kolcsonzo.auto_berles(kolcsonzo.autok[1], 4, datetime(2025, 3, 22))


elokeszites()

def kezdo_felulet():
    print("\n1. Autó bérlése\n"
          "2. Bérlés lemondása\n"
          "3. Bérlések listázása")

    x = None

    while type(x) is not int or int(x) <= 0 or int(x) > 3:
        try:
            x = int(input())
        except:
            print("Helytelen számot adtál meg")



    if x == 1:
        auto_berles_felulet()
    elif x == 2:
        berles_lemondasa_felulet()
    elif x == 3:
        berlesek_listazasa_felulet()
    else:
        kezdo_felulet()

def auto_berles_felulet():
    kolcsonzo.autok_listazasa()
    print("\n0. Vissza")


    sorszam = None

    while type(sorszam) is not int:
        try:
            sorszam = int(input("Melyik sorszámú autót szeretnéd kibérelni?"))

            if sorszam == 0:
                kezdo_felulet()
        except:
            print("Számot adj meg")

    napok_szama = None
    datum = None

    while int(sorszam) <= 0 or sorszam > len(kolcsonzo.autok):
        print("Nincs ilyen sorszám")
        sorszam = int(input("Melyik sorszámú autót szeretnéd kibérelni? "))
        if sorszam == 0:
            kezdo_felulet()

    while type(napok_szama) is not int or napok_szama <= 0:
        try:
            napok_szama = int(input("Hány napig szeretnéd kibérelni? "))
            if napok_szama == 0:
                kezdo_felulet()
        except:
            print("Helytelen számot adtál meg")

    while datum is None:
        try:
            datum = datetime.strptime(str(input("Add meg a dátumot hogy mikortól akarod kibérelni (év-hó-nap): ")), '%Y-%m-%d')
            if datum == 0:
                kezdo_felulet()
        except:
            print("Helytelen dátumot adtál meg")
    print(kolcsonzo.auto_berles(kolcsonzo.autok[sorszam-1], napok_szama, datum))
    kezdo_felulet()


def berles_lemondasa_felulet():
    kolcsonzo.berlesek_listazasa()
    print("0. Vissza")
    sorszam = None

    while sorszam is None:
        try:
            sorszam = int(input())
            print(sorszam)
        except:
            print("Helytelen sorszámot adtál meg")

    if int(sorszam) == 0:
        kezdo_felulet()

    while int(sorszam) < 0 or int(sorszam) > len(kolcsonzo.berlesek):
        print("Helytelen sorszámot adtál meg")

    kolcsonzo.berles_lemondasa(sorszam-1)
    print("Sikeresen lemondtad a bérlést")
    kezdo_felulet()

def berlesek_listazasa_felulet():
    kolcsonzo.berlesek_listazasa()

    input("irj valamit a visszalépéshez ")
    kezdo_felulet()

kezdo_felulet()
