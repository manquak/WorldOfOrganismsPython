from Zwierze import Zwierze
import random


class Antylopa(Zwierze):
    def __init__(self, x, y, swiat, gatunek):
        Zwierze.__init__(self, x, y, swiat, gatunek)
        self.sila = 4
        self.inicjatywa = 4
        self.gatunek = gatunek

    def dokadRuszyl(self):
        temp = list(self.polozenie)
        kierunek = random.randint(0, 8)
        if kierunek == 0:
            temp[0] += 1
        elif kierunek == 1:
            temp[0] -= 1
        elif kierunek == 2:
            temp[1] -= 1
        elif kierunek == 3:
            temp[1] += 1
        elif kierunek == 4:
            temp[0] += 2
        elif kierunek == 5:
            temp[0] -= 2
        elif kierunek == 6:
            temp[1] += 2
        elif kierunek == 7:
            temp[1] -= 2
        return temp

    def czyObronil(self, atakujacy):
        if random.randint(0, 2) == 1: # szansa na ucieczke antylopy
            flaga = False
            for i in range(8):
                while flaga is False:
                    temp = self.dokadRuszyl()
                    ofiara = self.swiat.getOrganizm(temp[0], temp[1])
                    if not self.swiat.czyPlansza(temp[0], temp[1]):
                        return
                    if ofiara is None:
                        self.polozenie[0] = temp[0]
                        self.polozenie[1] = temp[1]
                        flaga = True

            if flaga is True:
                self.swiat.komunikaty.append("Antylopa ucieka!")
                return True
        else:
            self.swiat.komunikaty.append("Antylopie nie udalo sie uciec")
            return False


    def rozmnazaj(self):
        temp = self.dokadRuszyl()
        if not self.swiat.czyPlansza(temp[0], temp[1]):
            return
        kolizyjny = self.swiat.getOrganizm(temp[0], temp[1])
        if kolizyjny is None:
            self.swiat.organizmy.append(Antylopa(temp[0], temp[1], self.swiat, self.gatunek))
            self.swiat.komunikaty.append("Rozmnozyl sie " + self.gatunek)