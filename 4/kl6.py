# Pracownik - imie, nazwisko, pensja
# Manager - imie, nazwisko, pensja, premia
# przedstaw_sie()
# oblicz_pensje()
class Pracownik:
    def __init__(self, imie, nazwisko, pensja):
        self.imie = imie
        self.nazwisko = nazwisko
        self.pensja = pensja

    def przedstaw_sie(self):
        print(f"Nazywam się {self.imie} {self.nazwisko}")

    def oblicz_pensje(self):
        return self.pensja


class Manager(Pracownik):
    """
    Manager dziedziczy po Pracownik
    """

    def __init__(self, imie, nazwisko, pensja, premia):
        super().__init__(imie, nazwisko, pensja)
        self.premia = premia

    def oblicz_pensje(self):
        return self.pensja + self.premia


pracownik = Pracownik("Jan", "Kowalski", 5000)
pracownik.przedstaw_sie()
print(f"Pensja {pracownik.imie} {pracownik.nazwisko} wynosi {pracownik.oblicz_pensje()}")
# Nazywam się Jan Kowalski
# Pensja Jan Kowalski wynosi 5000

manago = Manager("Anna", "Nowak", 15000, 5000)
manago.przedstaw_sie()
print(f"Pensja {manago.imie} {manago.nazwisko} wynosi {manago.oblicz_pensje()}")
# Nazywam się Anna Nowak
# Pensja Anna Nowak wynosi 20000

lista_pracowncy = [pracownik, manago]
for p in lista_pracowncy:
    print(f"Pensja {p.imie} {p.nazwisko} wynosi {p.oblicz_pensje()}")
# Pensja Jan Kowalski wynosi 5000
# Pensja Anna Nowak wynosi 20000
