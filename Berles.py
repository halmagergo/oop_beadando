import datetime

from Auto import Auto
class Berles(Auto):

    def __init__(self, auto, napok_szama:int, berles_kezdete:datetime.datetime):
        self.auto = auto
        self.napok_szama = napok_szama
        self.berles_kezdete = berles_kezdete

    def berles_koltsege(self):
        return self.napok_szama * self.berleti_dij



