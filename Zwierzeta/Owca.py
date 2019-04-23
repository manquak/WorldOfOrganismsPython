from Zwierze import Zwierze


class Owca(Zwierze):
    def __init__(self, x, y, swiat, gatunek):
        Zwierze.__init__(self, x, y, swiat, gatunek)
        self.sila = 4
        self.inicjatywa =4
        self.gatunek = gatunek

    def rozmnazaj(self):
        temp = self.dokadRuszyl()
        if not self.swiat.czyPlansza(temp[0], temp[1]):
            return
        kolizyjny = self.swiat.getOrganizm(temp[0], temp[1])
        if kolizyjny is None:
            self.swiat.organizmy.append(Owca(temp[0], temp[1], self.swiat, self.gatunek))
            self.swiat.komunikaty.append("Rozmnozyl sie " + self.gatunek)
