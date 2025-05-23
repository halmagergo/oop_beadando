from datetime import date

from Auto import Auto
class Berles(Auto):

    def __init__(self, auto, berles_datum:date):
        self.auto = auto
        self.berles_datum =  berles_datum

    def __str__(self):
        return f"Rendszám: {self.auto.rendszam}, " \
               f"Bérlés napja: {self.berles_datum} "

