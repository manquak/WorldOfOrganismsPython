import random
from Roslina import Roslina

class BarszczSosnowskiego(Roslina):
    def __init__(self, x, y, swiat, gatunek):
        Roslina.__init__(self, x, y, swiat, gatunek)
        self.sila = 10
        self.inicjatywa = 0
        self.gatunek = gatunek

    def rozmnazaj(self):
        temp = self.dokadRuszyl()
        if not self.swiat.czyPlansza(temp[0], temp[1]):
            return
        kolizyjny = self.swiat.getOrganizm(temp[0], temp[1])
        if kolizyjny is None:
            self.swiat.organizmy.append(BarszczSosnowskiego(temp[0], temp[1], self.swiat, self.gatunek))
            self.swiat.komunikaty.append("Rozmnozyl sie " + self.gatunek)


    def akcja(self):
        self.zabijNiepotrzebnego(self.polozenie[0], self.polozenie[1])
        szansa = random.randint(0, 10)
        if szansa == 1:
            self.rozmnazaj()
        self.wiek += 1


    def zabij(self, x, y):
        if self.swiat.czyPlansza(x, y):
            kolizyjny = self.swiat.getOrganizm(x, y)
            if kolizyjny is not None and kolizyjny.gatunek is not 'barszcz' and not isinstance(kolizyjny, Roslina):
                kolizyjny.zywy = False
                self.swiat.unsetOrganizm(kolizyjny)
                self.swiat.komunikaty.append("Barszcz zabil " + kolizyjny.gatunek)


    def zabijNiepotrzebnego(self, x, y):
        lewo = {}
        prawo = {}
        gora = {}
        dol = {}
        lewo[0] = x-1
        lewo[1] = y
        prawo[0] = x+1
        prawo[1] = y
        gora[0] = x
        gora[1] = y-1
        dol[0] = x
        dol[1] = y+1
        self.zabij(lewo[0], lewo[1])
        self.zabij(prawo[0], prawo[1])
        self.zabij(gora[0], gora[1])
        self.zabij(dol[0], dol[1])

