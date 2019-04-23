from operator import attrgetter

import pickle
import random

from Zwierzeta.Wilk import Wilk
from Zwierzeta.Owca import Owca
from Zwierzeta.Antylopa import Antylopa
from Zwierzeta.Zolw import Zolw
from Zwierzeta.Czlowiek import Czlowiek
from Zwierzeta.Lis import Lis
from Rosliny.Trawa import Trawa
from Rosliny.BarszczSosnowskiego import BarszczSosnowskiego
from Rosliny.Guarana import Guarana
from Rosliny.Mlecz import Mlecz
from Rosliny.WilczeJagody import WilczeJagody


class Swiat(object):
    def __init__(self, x, y, organizmy):
        self.x = x
        self.y = y
        self.organizmy = []
        self.inicjalizuj()
        self.komunikaty = []

    def getOrganizm(self, x, y):
        for organizm in self.organizmy:
            if organizm.polozenie[0] == x and organizm.polozenie[1] == y:
                return organizm
        return None

    def unsetOrganizm(self, organizm):
        try:
            self.organizmy.remove(organizm)
        except ValueError:
            pass

    def wykonajTure(self):
        OrganismOverload = 400

        self.organizmy = sorted(
            self.organizmy, key=attrgetter('inicjatywa', 'wiek'), reverse=True
        )

        rozmiar = len(self.organizmy)
        if rozmiar > OrganismOverload:
            pass

        for j in range(rozmiar):
            if j >= rozmiar:
                break
            current = self.organizmy[j]
            current.wiek += 1
            current.akcja()

            rozmiar = min([rozmiar, len(self.organizmy)])


    def wyczyscMape(self):
        self.organizmy = []

    def zapisz(self):
        with open("ZapisanyWorld.p", "wb") as file:
            pickle.dump(self, file)

    def wczytaj(self):
        with open("ZapisanyWorld.p", "rb") as file:
            copy = pickle.load(file)
            self.x = copy.x
            self.y = copy.y
            self.komunikaty = copy.komunikaty
            self.organizmy = copy.organizmy

            for organizm in self.organizmy:
                organizm.swiat = self


    def losujOrganizm(self, x, y):
        return random.choice([
            Wilk(x, y, self, 'wilk'),
            Owca(x, y, self, 'owca'),
            Lis(x, y, self, 'lis'),
            Zolw(x, y, self, 'zolw'),
            Antylopa(x, y, self, 'antylopa'),
            Guarana(x, y, self, 'guarana'),
            BarszczSosnowskiego(x, y, self, 'barszcz'),
            Mlecz(x, y, self, 'mlecz'),
            Trawa(x, y, self, 'trawa'),
            WilczeJagody(x, y, self, 'jagody')

        ])

    def inicjalizuj(self):
        for i in range(20):
            x, y = random.randint(0, self.x - 1), random.randint(0, self.y - 1)
            self.organizmy.append(self.losujOrganizm(x, y))
        x, y = random.randint(0, self.x - 1), random.randint(0, self.y - 1)
        self.organizmy.append(Czlowiek(x, y, self, 'CZLOWIEK'))

    def czyPlansza(self, x, y):
        if 0 <= x < self.x and 0 <= y < self.y:
            return True
        else:
            return False

    def znajdzCzlowieka(self):
        for o in self.organizmy:
            if o is not None and o.gatunek == 'CZLOWIEK':
                return o
        return None