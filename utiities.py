import json
import position
from os import listdir
from period import Period
from period import PeriodEncoder
from position import Position
import os
import os.path


def get_template_positions() -> Position:
    p = [position.Position("Ubezpieczenie zycie", 511.02, "Ubezpieczenie na zycie prudential od Ewki"),
         position.Position("Czynsz+garaz", 436.48, "Opata za czynsz + garaz"),
         position.Position("Fundusz remontowy + garaz", 85.28, "oplata za fundusz remontowy + garaz"),
         position.Position("Prad", desc="Oplata za prad"),
         position.Position("Internet", 89, "Oplata za internet Moico"),
         position.Position("Telefon", desc="Oplata za telefon Nju mobile"),
         position.Position("ZUS", 1684, desc="Oplata na ZUS"),
         position.Position("Ksiegowy", 110, desc="Oplata za uslugi ksiegowe"),
         position.Position("Podatek dochodowy", desc="Podatek dochodowy"), position.Position("VAT", desc="VAT")]

    return p

