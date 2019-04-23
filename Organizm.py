import random
from abc import ABCMeta , ABC, abstractmethod


class Organizm(object):
    __metaclass__ = ABCMeta

    def __init__(self, x, y, swiat, gatunek):
        self.sila = 0
        self.inicjatywa = 0
        self.zywy = True
        self.wiek = 0
        self.polozenie = [x, y]
        self.swiat = swiat
        self.gatunek = gatunek

    def czyObronil(self, atakujacy):
        return False

    def dokadRuszyl(self):
        temp = list(self.polozenie)
        kierunek = random.randint(0, 4)
        if kierunek == 0:
            temp[0] += 1
        elif kierunek == 1:
            temp[0] -= 1
        elif kierunek == 2:
            temp[1] -= 1
        elif kierunek == 3:
            temp[1] += 1
        return temp

    def czyRuszyl(self):
        return True

    @abstractmethod
    def akcja(self):
        pass

    def kolizja(self, ofiara):
        if self == ofiara:
            return
        if ofiara.gatunek == self.gatunek:
            self.rozmnazaj()
        elif ofiara.sila <= self.sila:
            self.swiat.unsetOrganizm(ofiara)
            self.swiat.komunikaty.append("Walke wygrywa " + self.gatunek)
        else:
            ofiara.swiat.unsetOrganizm(self)
            self.swiat.komunikaty.append("Walke wygrywa " + ofiara.gatunek)
