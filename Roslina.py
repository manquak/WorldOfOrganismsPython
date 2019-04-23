from Organizm import Organizm
import random

class Roslina(Organizm):
    def __init__(self, x, y, swiat, gatunek):
        Organizm.__init__(self, x, y, swiat, gatunek)
        self.inicjatywa = 0

    def akcja(self):
        szansa = random.randint(0, 10)
        if szansa == 1:  # szansa 1/10 jedna z rozsiania
            self.rozmnazaj()
            self.wiek += 1

