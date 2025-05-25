from datetime import date, timedelta

from Berles import Berles
from Auto import Auto
class Autokolcsonzo:

    def __init__(self, nev):
        self.nev = nev
        self.autok = []
        self.berlesek = []

    def auto_felvetel(self, auto):
        self.autok.append(auto)

    def auto_berles(self, auto, datum: date):

        if auto in self.autok:
            if not self.ki_van_berelve(auto):
                self.berlesek.append(Berles(auto, datum))
                return f"{auto.rendszam} rendszámú autó sikeresen ki lett bérelve. Bérlés ára: {auto.berleti_dij} Ft"
            elif self.ki_van_berelve(auto) and self.valid_datum(auto, datum):
                self.berlesek.append(Berles(auto, datum))
                return f"{auto.rendszam} rendszámú autó sikeresen ki lett bérelve. Bérlés ára: {auto.berleti_dij} Ft"
            else:
                return f"{auto.rendszam} rendszámú autó ebben az időpontban nem lehet kibérelni."

        else:
            return f"Nincs ilyen autó"

    def ki_van_berelve(self, auto):
        for berles in self.berlesek:
            if berles.auto == auto:
                return True
        return False

    def valid_datum(self, auto, datum: date):

        for berles in self.berlesek:
            if berles.auto == auto and datum == berles.berles_datum:
                print(date.today())
                return False
        return True

    def autok_listazasa(self):
        print(f"Autók ({len(self.autok)} db):")
        for i in range(len(self.autok)):
            print(f"{i+1}. {self.autok[i]}")


    def berlesek_listazasa(self):
        print(f"Bérlések ({len(self.berlesek)} db):")
        for i in range(len(self.berlesek)):
            print(f"{i+1}. {self.berlesek[i]}")


    def berles_lemondasa(self, index):
        self.berlesek.pop(index)
        return f"{index} indexű bérlés ki lett törölve."
