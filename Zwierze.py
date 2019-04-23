from Organizm import Organizm
class Zwierze(Organizm):
    def __init__(self, x, y, swiat, gatunek):
        Organizm.__init__(self, x, y, swiat, gatunek)



    def akcja(self):
        if not self.czyRuszyl():
            return
        temp = self.dokadRuszyl()
        ofiara = self.swiat.getOrganizm(temp[0], temp[1])

        if not self.swiat.czyPlansza(temp[0], temp[1]):
            return

        if ofiara is None:
            self.polozenie[0] = temp[0]
            self.polozenie[1] = temp[1]
            return
        elif ofiara.czyObronil(self):
            self.wiek += 1
        elif ofiara != self:
            self.polozenie[0] = temp[0]
            self.polozenie[1] = temp[1]

            self.kolizja(ofiara)
        elif self.gatunek == ofiara.gatunek:
            self.wiek += 1
            self.rozmnazaj()
