from Zwierze import Zwierze
class Czlowiek(Zwierze):
    def __init__(self, x, y, swiat, gatunek):
        Zwierze.__init__(self, x, y, swiat, gatunek)
        self.sila = 4
        self.inicjatywa =5
        self.gatunek = gatunek
        self.licznikMocy = 0
        self.moc = False
        self.cooldown = 0
        self.next_x = 0
        self.next_y = 0



    def akcja(self):
        if self.licznikMocy == 5:
            self.moc = False
            self.licznikMocy = 0
            self.swiat.komunikaty.append("Wylaczono supermoc!")
            self.cooldown = 5
        if self.moc is True:
            self.licznikMocy += 1
        if self.moc is False and self.cooldown > 0:
            self.cooldown -= 1

        temp = {}
        temp[0] = self.next_x
        temp[1] = self.next_y
        nowy_x = self.polozenie[0]+temp[0]
        nowy_y = self.polozenie[1]+temp[1]

        if self.swiat.czyPlansza(nowy_x, nowy_y):
            kolizyjny = self.swiat.getOrganizm(nowy_x, nowy_y)

            if kolizyjny is None: # jesli wolne pole
                self.polozenie[0] = nowy_x
                self.polozenie[1] = nowy_y
                self.wiek += 1
                return
            elif kolizyjny.czyObronil(self): # jesli obronil
                self.wiek += 1
            elif kolizyjny != self: # jesli jakis inny organizm w kolizji
                if self.moc is True:
                    self.swiat.komunikaty.append("Czlowiek odstaszyl napastnika!")
                    kolizyjny.polozenie[0] = nowy_x
                    kolizyjny.polozenie[1] = nowy_y
                else:
                    self.kolizja(kolizyjny)
                    self.polozenie[0] = nowy_x
                    self.polozenie[1] = nowy_y





    def supermoc(self):
        if self.moc is True:
            self.swiat.komunikaty.append("Moc juz zostala aktywowana!")
        elif self.cooldown == 0:
            self.swiat.komunikaty.append("Aktywowano supermoc czlowieka!")
            self.moc = True
        else:
            self.swiat.komunikaty.append("Nie mozesz jeszcze uzyc mocy!")

    def czyObronil(self, atakujacy):
        if self.moc is True:
            flaga = False
            for i in range(4): # 4 bo tylko 4 kierunki
                while flaga is False:
                    temp = atakujacy.dokadRuszyl()
                    pole = self.swiat.getOrganizm(temp[0], temp[1])

                    if not self.swiat.czyPlansza(temp[0], temp[1]):
                        return
                    if pole is not None:
                        atakujacy.polozenie[0] = temp[0]
                        atakujacy.polozenie[1] = temp[1]
                        flaga = True

            if flaga:
                self.swiat.komunikaty.append("Czlowiek odstraszyl napastnika!")
            else:
                self.swiat.komunikaty.append("Czlowiek nie mogl uciec.")
            return True
        return False

