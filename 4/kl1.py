# klasy są elementem programowania obiektowego
# hermetyzacja, dziedzczenie, polimorfizm, abstrakcja
# klasa - przepis, szablon
# wskazuje minmum tego co powinien zawierac obiekt klasy
# pola, funkcje
# pola - zmienna
# obiekt - instancja klasy - element zbudowany wg przepisu (klasy)
# definicja klasy - nic sie nie wykona
class Human:
    """
    Klasa Human opisująca człowieka w pythonie
    """

    imie = ""
    wiek = None
    plec = "k"

    def powitanie(self):
        print("Nazywam się", self.imie)


help(Human)
print(Human.__doc__)  # Klasa Human opisująca człowieka w pythonie
print(print.__doc__)
# pydoc -b - uruchomienie serwra z dokumentacja projektu
# pydoc -w kl1 - plik htm z dokumntacja kl1
cz1 = Human()
print(cz1)  # <__main__.Human object at 0x000001FB0BA64F80>
print(cz1.plec)
print(cz1.imie)
print(cz1.wiek)
cz1.powitanie()
cz1.wiek = 45
cz1.imie = "Kasia"
print(cz1.plec)
print(cz1.imie)
print(cz1.wiek)
cz1.powitanie()  # Nazywam się Kasia

# stworzyc obiek klasy Human odmiennej płci
# nadać wiek i imię
cz2 = Human()
cz2.imie = "Radek"
cz2.wiek = 45
cz2.plec = "m"
print(cz2.plec)
print(cz2.imie)
print(cz2.wiek)
cz2.powitanie()
# k
# Kasia
# 45
# Nazywam się Kasia
# m
# Radek
# 45
# Nazywam się Radek
