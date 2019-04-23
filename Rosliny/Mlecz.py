from Roslina import Roslina
import random


class Mlecz(Roslina):
    def __init__(self, x, y, swiat, gatunek):
        Roslina.__init__(self, x, y, swiat, gatunek)
        self.sila = 0
        self.inicjatywa = 0
        self.gatunek = gatunek


    def rozmnazaj(self):
        temp = self.dokadRuszyl()
        if not self.swiat.czyPlansza(temp[0], temp[1]):
            return
        kolizyjny = self.swiat.getOrganizm(temp[0], temp[1])
        if kolizyjny is None:
            self.swiat.organizmy.append(Mlecz(temp[0], temp[1], self.swiat, self.gatunek))
            self.swiat.komunikaty.append("Rozmnozyl sie " + self.gatunek)

    def akcja(self):
        for i in range(3):
            Roslina.akcja(self)
