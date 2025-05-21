from datetime import datetime, timedelta

from Auto import Auto
class Berles(Auto):

    def __init__(self, auto, napok_szama:int, berles_kezdete:datetime):
        self.auto = auto
        self.napok_szama = napok_szama
        self.berles_kezdete = berles_kezdete
        self.berles_vege = berles_kezdete + timedelta(days=napok_szama)

    def __str__(self):
        return f"Rendszám: {self.auto.rendszam} " \
               f"Napok Száma: {self.napok_szama} " \
               f"Bérlés Kezdete: {self.berles_kezdete} " \
               f"Bérlés Vége: {self.berles_vege}"

