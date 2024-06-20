# zrobic klasę Dom
# metraz, kolor, liczba_okien
# pola mają być prywatne
# wystawić metody do odczytu i zapisu tych pól
# dodać komentarz - dokumentację
# stworzyc obiekty tej klasy
# wykorzystać ich funkcje
class Dom:
    """
    Klasa opisująca dom w pythonie
    """

    def __init__(self, metraz, kolor, liczba_okien):
        """

        :param metraz:
        :param kolor:
        :param liczba_okien:
        """
        self.__metraz = metraz
        self.__kolor = kolor
        self.__licba_okien = liczba_okien

    def mam_kolor(self):
        print(f"Mam kolor {self.__kolor}")

    def mam_metraz(self):
        print(f"Mam metraz {self.__metraz} m2")

    def mam_okna(self):
        print(f"Liczba okien {self.__licba_okien} szt.")

    def zmien_kolor(self):
        odp = input("Podaj nowy kolor")
        self.__kolor = odp
        self.mam_kolor()
        self.__farba()

    def zmien_metraz(self):
        odp = int(input("Podaj nowy metraż"))
        self.__metraz = odp
        self.mam_metraz()

    def zmien_okna(self):
        odp = int(input("Podaj liczbę okien"))
        self.__licba_okien = odp
        self.mam_okna()

    def __farba(self):
        print("Zabrakło farby")


dom1 = Dom(200, "biały", 15)
dom1.mam_metraz()  # Mam metraz 200 m2
dom1.zmien_metraz()
# Mam metraz 200 m2
# Podaj nowy metraż500
# Mam metraz 500 m2
dom1.zmien_kolor()
# Mam metraz 200 m2
# Podaj nowy metraż500
# Mam metraz 500 m2
# Podaj nowy kolorzielony
# Mam kolor zielony
# Po dodaniu metody prywatnej __farba()
# Mam metraz 200 m2
# Podaj nowy metraż300
# Mam metraz 300 m2
# Podaj nowy kolorczerwony
# Mam kolor czerwony
# Zabrakło farby
