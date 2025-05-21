from datetime import datetime, timedelta

from Berles import Berles
from Auto import Auto
class Autokolcsonzo:

    def __init__(self, nev):
        self.nev = nev
        self.autok = []
        self.berlesek = []

    def auto_felvetel(self, auto):
        self.autok.append(auto)

    def auto_berles(self, auto, napok_szama: int, datum: datetime):
        datum = datum - timedelta(days=1)
        if auto in self.autok:
            if not self.ki_van_berelve(auto):
                self.berlesek.append(Berles(auto, napok_szama, datum))
                return f"{auto.rendszam} rendszámú autó sikeresen ki lett bérelve. Bérlés ára: {napok_szama * auto.berleti_dij} Ft"
            elif self.ki_van_berelve(auto) and not self.valid_datum(auto, datum, napok_szama):
                self.berlesek.append(Berles(auto, napok_szama, datum))
                return f"{auto.rendszam} rendszámú autó sikeresen ki lett bérelve. Bérlés ára: {napok_szama * auto.berleti_dij} Ft"
            else:
                return f"{auto.rendszam} rendszámú autó ebben az időpontban nem lehet kibérelni."

        else:
            return f"Nincs ilyen autó"

    def ki_van_berelve(self, auto):
        for berles in self.berlesek:
            if berles.auto == auto:
                return True
        return False

    def valid_datum(self, auto, berles_kezdete, napok_szama):

        for berles in self.berlesek:
            if berles.auto == auto:
                berles_vege = berles_kezdete + timedelta(days=napok_szama)

                if berles.berles_vege >= berles_kezdete >= berles.berles_kezdete or berles.berles_vege >= berles_vege >= berles.berles_kezdete:
                    #print(f"Overlap van a dátumokban. Bérlés kezdete: {berles.berles_kezdete}, Bérlés Vége: {berles.berles_vege} | új bérlés kezdete: {berles_kezdete}, új bérlés vége: {berles_vege}")
                    return True
        return False

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
