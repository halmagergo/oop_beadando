from Autokolcsonzo import Autokolcsonzo
from Szemelyauto import Szemelyauto
from Teherauto import Teherauto
from datetime import datetime
from Auto import Auto

kolcsonzo = Autokolcsonzo("bót")

kolcsonzo.auto_felvetel(Szemelyauto("ABC123", "valami", 5000, 2, 2000))
kolcsonzo.auto_felvetel(Teherauto("ERT456", "banán", 7000, 4, 4500))
print(kolcsonzo.autok_listazasa())




