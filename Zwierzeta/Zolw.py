from Zwierze import Zwierze
import random


class Zolw(Zwierze):
    def __init__(self, x, y, swiat, gatunek):
        Zwierze.__init__(self, x, y, swiat, gatunek)
        self.sila = 2
        self.inicjatywa =1
        self.gatunek = gatunek

    def czyRuszyl(self):
        if random.randint(0, 4) == 1: # wybieramy po prostu jakas wartosc aby byla mniejsza szansa
            return True
        else:
            return False

    def czyObronil(self, atakujacy):
        GranicznaSila = 5
        if atakujacy.sila < GranicznaSila:
            self.swiat.komunikaty.append("Zolw sie obronil")
            return True
        else:
            return False

    def rozmnazaj(self):
        temp = self.dokadRuszyl()
        if not self.swiat.czyPlansza(temp[0], temp[1]):
            return
        kolizyjny = self.swiat.getOrganizm(temp[0], temp[1])
        if kolizyjny is None:
            self.swiat.organizmy.append(Zolw(temp[0], temp[1], self.swiat, self.gatunek))
            self.swiat.komunikaty.append("Rozmnozyl sie " + self.gatunek)