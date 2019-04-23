from Zwierze import Zwierze
from random import shuffle

class Lis(Zwierze):
    def __init__(self, x, y, swiat, gatunek):
        Zwierze.__init__(self, x, y, swiat, gatunek)
        self.sila = 3
        self.inicjatywa = 7
        self.gatunek = gatunek

    def akcja(self):
        if not self.czyRuszyl():
            return

        x, y = self.polozenie

        mozliwePola = [(x, y + 1), (x, y - 1), (x - 1, y), (x + 1, y)]
        shuffle(mozliwePola)

        for pole in mozliwePola:
            ofiara = self.swiat.getOrganizm(pole[0], pole[1])

            if not self.swiat.czyPlansza(pole[0], pole[1]):
                return

            if ofiara is None:
                self.polozenie[0] = pole[0]
                self.polozenie[1] = pole[1]
                return
            elif ofiara != self and ofiara.sila < self.sila:
                self.kolizja(ofiara)
                return

    def rozmnazaj(self):
        temp = self.dokadRuszyl()
        if not self.swiat.czyPlansza(temp[0], temp[1]):
            return
        kolizyjny = self.swiat.getOrganizm(temp[0], temp[1])
        if kolizyjny is None:
            self.swiat.organizmy.append(Lis(temp[0], temp[1], self.swiat, self.gatunek))
            self.swiat.komunikaty.append("Rozmnozyl sie " + self.gatunek)