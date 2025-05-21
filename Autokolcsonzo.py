import datetime

from Berles import Berles
from Auto import Auto
class Autokolcsonzo:

    def __init__(self, nev):
        self.nev = nev
        self.autok = []
        self.berlesek = []

    def auto_felvetel(self, auto):
        self.autok.append(auto)

    def auto_berles(self, rendszam, napok_szama: int, datum: datetime.datetime):
        if self.letezo_auto(rendszam) and not self.letezo_berles(rendszam):



    def letezo_auto(self, rendszam):
        for auto in self.autok:
            if auto.rendszam == rendszam:
                return True
        return False

    def letezo_berles(self, rendszam):
        for berles in self.berlesek:
            if berles.auto.rendszam == rendszam:
                return True
        return False

    def autok_listazasa(self):
        for auto in self.autok:
            print(auto)

    def berlesek_listazasa(self):

        for berles in self.berlesek:
            print(f"{berles.rendszam}")


