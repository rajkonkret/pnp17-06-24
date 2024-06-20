class Human:
    """
    Klasa Human opisująca człowieka w pythonie
    """

    def __init__(self, imie, wiek, wzrost, plec="k"):
        """
        Metoda inicjalizująca (konstruktor)
        :param imie:
        :param wiek:
        :param wzrost:
        :param plec:
        """
        self.imie = imie
        self.wiek = wiek
        self.wzrost = wzrost
        self.plec = plec

    def powitanie(self):
        print("Nazywam się", self.imie)

    # dopisac metody wypisz_wiek, wypisz_wzrost
    def wypisz_wiek(self):
        print(f"Mam {self.wiek} lat.")

    def wypisz_wzrost(self):
        print(f'Mam {self.wzrost} cm wzrostu')

    def ruszaj(self):
        if self.plec == "k":
            print("Ruszyłam w drogę")
        else:
            print("Ruszyłęm w drogę")


# cz1 = Human()  # TypeError: Human.__init__() missing 3 required positional arguments: 'imie', 'wiek', and 'wzrost'
cz1 = Human("Ania", 30, 190)
print(cz1.wiek)
print(cz1.wzrost)
print(cz1.imie)
print(cz1.plec)
cz1.powitanie()
cz1.wypisz_wiek()
cz1.wypisz_wzrost()
# 30
# 190
# Ania
# k
# Nazywam się Ania
# Mam 30 lat.
# Mam 190 cm wzrostu
cz2 = Human("Radek", 40, 190, "m")
cz2.powitanie()
cz2.wypisz_wzrost()
cz2.wypisz_wiek()
# Nazywam się Radek
# Mam 190 cm wzrostu
# Mam 40 lat.
cz1.ruszaj()
cz2.ruszaj()
# Ruszyłam w drogę
# Ruszyłęm w drogę
