from tkinter import *
from tkinter.ttk import Frame, Button, Label
from Swiat import *

class Grafika(Frame):
    def __init__(self, parent, swiat):
        Frame.__init__(self, parent)
        self.buttons = {}
        self.komunikaty = Listbox()
        self.frameworld = swiat
        self.fKomunikaty = swiat.komunikaty
        self.parent = parent
        self.initUI()
        self.master.bind_all('<Key>', self.keypressed)
        self.narysujSwiat()


    def initUI(self):
        self.parent.title("Konrad Paniec")
        self.grid()
        self.columnconfigure(1, weight=1)
        self.columnconfigure(3, pad=7)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(5, pad=7)

        lbl = Label(self, text="Plansza:")
        lbl.grid(pady=4, padx=5)

        self.komunikaty = Listbox(self, height=31, width=40)
        for k in self.fKomunikaty:
            self.komunikaty.insert(END, k)
        self.komunikaty.grid(row=3, column=1)

        odspet = Label(self, text='Wydarzenia')
        odspet.grid(row=0, column=1)

        bframe = Frame(self)
        buttons = {}
        for i in range(self.frameworld.x):
            buttons[i] = {}
            for j in range(self.frameworld.y):
                buttons[i][j] = Button(bframe, width=6, command=lambda x=i, y=j: self.dodajorganizm(x, y))
                buttons[i][j].grid(row=i, column=j)
        self.buttons = buttons
        bframe.grid(row=3, column=0)


    def nowagra(self):
        for organizm in self.frameworld.organizmy:
            x, y = organizm.polozenie
            self.buttons[x][y].config(text='')
        self.frameworld.wyczyscMape()
        self.frameworld.inicjalizuj()
        self.narysujSwiat()


    def zapiszgre(self):
        self.frameworld.zapisz()

    def wczytajgre(self):
        self.frameworld.wczytaj()
        self.narysujSwiat()

    def dodajorganizm(self, x, y):  # Dodawanie do planszy myszka
        def dodawanie(*args):
            dodawany = variable.get()

            if dodawany == 'wilk':
                self.frameworld.organizmy.append(Wilk(x, y, self.frameworld, 'wilk'))
            elif dodawany == 'guarana':
                self.frameworld.organizmy.append(Guarana(x, y, self.frameworld, 'guarana'))
            elif dodawany == 'mlecz':
                self.frameworld.organizmy.append(Mlecz(x, y, self.frameworld, 'mlecz'))
            elif dodawany == 'trawa':
                self.frameworld.organizmy.append(Trawa(x, y, self.frameworld, 'trawa'))
            elif dodawany == 'lis':
                self.frameworld.organizmy.append(Lis(x, y, self.frameworld, 'lis'))
            elif dodawany == 'wilcze jagody':
                self.frameworld.organizmy.append(WilczeJagody(x, y, self.frameworld, 'jagody'))
            elif dodawany == 'antylopa':
                self.frameworld.organizmy.append(Antylopa(x, y, self.frameworld, 'antylopa'))
            elif dodawany == 'barszcz':
                self.frameworld.organizmy.append(BarszczSosnowskiego(x, y, self.frameworld, 'barszcz'))
            elif dodawany == 'owca':
                self.frameworld.organizmy.append(Owca(x, y, self.frameworld,'owca'))
            elif dodawany == 'zolw':
                self.frameworld.organizmy.append(Zolw(x, y, self.frameworld, 'zolw'))

            self.narysujSwiat()
            w.destroy()

        variable = StringVar(self.parent)
        variable.set("Dodaj Organizm")

        w = OptionMenu(self.parent, variable, "wilk", "owca", "barszcz", "mlecz", "guarana", "trawa", "zolw", "lis",
                       "antylopa", "wilcze jagody")
        w.grid(column=0, row=0)
        variable.trace("w", dodawanie)


    def keypressed(self, event):

        czlowiek = self.frameworld.znajdzCzlowieka()
        if czlowiek is not None:
            if event.keysym == 'Right':
                czlowiek.next_x = 0
                czlowiek.next_y = 1
            elif event.keysym == 'Down':
                czlowiek.next_x = 1
                czlowiek.next_y = 0
            elif event.keysym == 'Up':
                czlowiek.next_x = -1
                czlowiek.next_y = 0
            elif event.keysym == 'Left':
                czlowiek.next_x = 0
                czlowiek.next_y = -1
            elif event.keysym == 'm':
                czlowiek.supermoc()
                czlowiek.next_x = 0
                czlowiek.next_y = 0

        self.komunikaty.delete(0, END)
        for k in reversed(self.fKomunikaty):
            self.komunikaty.insert(END, k)
        #self.fKomunikaty.clear()

        self.frameworld.wykonajTure()
        self.narysujSwiat()


    def narysujSwiat(self):
        for i in range(self.frameworld.x):
            for j in range(self.frameworld.y):
                self.buttons[i][j].config(text=' ')

        for organizm in self.frameworld.organizmy:
            x, y = organizm.polozenie
            self.buttons[x][y].config(text=organizm.gatunek)






szerokosc = int(input("Podaj szerokosc"))
wysokosc = int(input("Podaj wysokosc"))
swiat = Swiat(wysokosc, szerokosc, None)
root = Tk()
menubar = Menu(root)

b = Grafika(root, swiat)
menubar.add_command(label="Nowa gra", command=b.nowagra)
menubar.add_command(label="Zapisz gre", command=b.zapiszgre)
menubar.add_command(label="Wczytaj gre", command=b.wczytajgre)
root.config(menu=menubar)
root.mainloop()
