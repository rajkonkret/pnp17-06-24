from abc import ABC, abstractmethod


class Ptak(ABC):
    """
    Klasa opisująca ptaka w Pythonie
    """

    def __init__(self, gatunek, szybkosc):
        self.gatunek = gatunek
        self.szybkosc = szybkosc

    def latam(self):
        print("Tu", self.gatunek, "Lecę z szybkoscią", self.szybkosc)

    @abstractmethod
    def wydaj_odglos(self):
        pass


class Kura(Ptak):
    def __init__(self, gatunek):
        super().__init__(gatunek, 0)

    def latam(self):
        print("Tu", self.gatunek, "Ja nie latam.")

    def wydaj_odglos(self):
        print("Ko ko kok o ko")

    def dziobanie(self):
        print("Tu", self.gatunek, "idę sobie podziobać")


class Orzel(Ptak):
    def wydaj_odglos(self):
        print("Kierr kier kir")

    def polowanie(self):
        print("Tu", self.gatunek, "Rozpoczynam polowanie.")


class Sowa(Ptak):
    """
    Klasa Sowa
    """


# Po oznaczeniu metody jako abstrakcyjnej
# klasa abstrakcyjna - nie można tworzyć obiektów takiej klasy
# TypeError: Can't instantiate abstract class Ptak without an implementation for abstract method 'wydaj_odglos'
# orzel1 = Ptak("Orzel Bielik", 45)
# orzel1.latam()  # Tu Orzel Bielik Lecę z szybkoscią 45
# orzel1.wydaj_odglos()
#
# kur1 = Ptak("Kura domowa", 0)
# kur1.latam()  # Tu Kura domowa Lecę z szybkoscią 0
# kur1.wydaj_odglos()

kur2 = Kura("Kura domowa")
kur2.latam()  # Tu Kura domowa Ja nie latam.
kur2.wydaj_odglos()  # Ko ko kok o ko
orzel2 = Orzel("Orzeł Bielik", 55)
orzel2.latam()
orzel2.wydaj_odglos()
# Tu Orzeł Bielik Lecę z szybkoscią 55
# Kierr kier kir
# Tu Kura domowa Ja nie latam.
# Ko ko kok o ko
# Tu Orzeł Bielik Lecę z szybkoscią 55
# Kierr kier kir
#
# TypeError: Can't instantiate abstract class Sowa without an implementation for abstract method 'wydaj_odglos'
# sowa = Sowa("Sowa", 15)
orzel2.polowanie()
kur2.dziobanie()
# Tu Orzeł Bielik Rozpoczynam polowanie.
# Tu Kura domowa idę sobie podziobać
