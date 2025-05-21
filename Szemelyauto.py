from Auto import Auto


class Szemelyauto(Auto):

    def __init__(self, rendszam, tipus, berleti_dij, ajtok_szama, suly):
        super().__init__(rendszam, tipus, berleti_dij)
        self.ajtok_szama = ajtok_szama
        self.suly = suly

    def __str__(self):
        return f"Rendszám: {self.rendszam}" \
               f" Tipus: {self.tipus}" \
               f" Bérleti díj: {self.berleti_dij} Ft" \
               f" Ajtók száma: {self.ajtok_szama}" \
               f" Súly: {self.suly} Kg"


