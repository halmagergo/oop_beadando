from Autokolcsonzo import Autokolcsonzo
from Szemelyauto import Szemelyauto
from Teherauto import Teherauto
from datetime import date, datetime
from Auto import Auto


# Előkészítés
kolcsonzo = Autokolcsonzo("Autó kölcsönző")

def elokeszites():
    kolcsonzo.auto_felvetel(Szemelyauto("ABC123", "Opel", 30000, 5, 2000))
    kolcsonzo.auto_felvetel(Teherauto("ERT456", "Ford", 25000, 2, 4500))
    kolcsonzo.auto_felvetel(Szemelyauto("JKB742", "Skoda", 35000, 5, 1500))

    kolcsonzo.auto_berles(kolcsonzo.autok[0], date(2025, 7, 21))
    kolcsonzo.auto_berles(kolcsonzo.autok[1], date(2025, 8, 20))
    kolcsonzo.auto_berles(kolcsonzo.autok[2], date(2025, 9, 28))
    kolcsonzo.auto_berles(kolcsonzo.autok[1], date(2025, 10, 22))


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

    while type(sorszam) is not int or sorszam <= 0 or sorszam > len(kolcsonzo.autok):
        try:
            sorszam = int(input("Melyik sorszámú autót szeretnéd kibérelni?"))

            if sorszam == 0:
                kezdo_felulet()
        except:
            print("Számot adj meg")

    datum = None

    while datum is None:
        try:
            d = input("Add meg a dátumot hogy mikortól akarod kibérelni (év-hó-nap): ")
            try:
                if int(d) == 0:
                    kezdo_felulet()
            except:
                pass
            d = datetime.strptime(d, '%Y-%m-%d').date()
            if d >= date.today():
                datum = d
                print(kolcsonzo.auto_berles(kolcsonzo.autok[sorszam - 1], datum))
            else:
                print("A dátum nem lehet a mainál régebbi")
        except:
            print("Helytelen dátumot adtál meg")

    kezdo_felulet()


def berles_lemondasa_felulet():
    kolcsonzo.berlesek_listazasa()
    print("0. Vissza")
    sorszam = None

    while type(sorszam) is not int or sorszam > len(kolcsonzo.berlesek) or sorszam < 0:
        try:
            sorszam = int(input("Melyik sorszámú bérlést szeretnéd törölni? "))
            if int(sorszam) == 0:
                kezdo_felulet()
        except:
            print("Helytelen sorszámot adtál meg")

    kolcsonzo.berles_lemondasa(int(sorszam)-1)
    print("Sikeresen lemondtad a bérlést")
    kezdo_felulet()

def berlesek_listazasa_felulet():
    kolcsonzo.berlesek_listazasa()

    kezdo_felulet()

kezdo_felulet()
