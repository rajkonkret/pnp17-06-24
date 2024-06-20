# dziedziczenie
# przejcie cech innej klasy, nadpisanie, modyfikacja, rozszerzyc

class Pojazd:
    def __init__(self, kolor):
        self.kolor = kolor

    def info(self):
        print("Kolor:", self.kolor)


class Samochod(Pojazd):
    """
    Klasa Samochód
    """

    def __init__(self, kolor, marka=None):
        super().__init__(kolor)  # musimy wywołać konstruktor z klasy wyzszej: super() - klasa wyższa
        self.marka = marka

    def info(self):
        super().info()  # możemy wywołac metode info() z klasy wyzszej (super())
        print("Marka:", self.marka)


poj = Pojazd("czerwony")
poj.info()

car1 = Samochod("zielony")
car1.info()
# Kolor: czerwony
# Kolor: zielony
car2 = Samochod("Biały", "Fiat")
car2.info()
# Kolor: czerwony
# Kolor: zielony
# Marka: None
# Kolor: Biały
# Marka: Fiat

# polimorfizm - możliwość wykorzystania wspolnych cech obiektów klas dziedziczących ze wspólnej klasy
lista = [poj, car2, car1]
for i in lista:
    print(i.kolor)

for i in lista:
    print(i.info())
# czerwony
# Biały
# zielony
# Kolor: czerwony
# None
# Kolor: Biały
# Marka: Fiat
# None
# Kolor: zielony
# Marka: None
# None