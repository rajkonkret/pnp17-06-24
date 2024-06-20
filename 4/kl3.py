class Car:
    """
    Klasa opsująca samochód w pythonie
    """

    def __init__(self, model, year):
        """
        Konstruktor
        :param moel:
        :param year:
        """
        self.model = model
        self.year = year
        # hermetyzacja
        self.__predkosc = 0  # pole jako prywatne

    # enkapsulacja - wystawienie metod do odczytu i zapisu pól w sposób kontrolowany
    def gaz(self):
        self.__predkosc += 10

    def licznik(self):
        print(f"Prędkość wynosi {self.__predkosc} km/h")

    def hamuj(self):
        self.__predkosc -= 10


car1 = Car("Ford Fiesta", 1990)
print(car1.model)
print(car1.year)
# Ford Fiesta
# 1990
car1.gaz()
car1.gaz()
car1.gaz()
car1.gaz()
car1.gaz()
# po oznaczeniu predkosc jako prywatnej: __predkosc
# nie ma możliwości dostęu do tego pola poza klasą
# AttributeError: 'Car' object has no attribute '__predkosc'. Did you mean: '_Car__predkosc'?
# print(car1.__predkosc)  # 50 odczyt pola się nie uda
car1.licznik()  # Prędkość wynosi 50 km/h
car1.__predkosc = 0  # storzył pole o tej nazwie o zasiegu globalnym
car1.licznik()  # Prędkość wynosi 50 km/h
car1.hamuj()
car1.hamuj()
car1.hamuj()
car1.hamuj()
car1.hamuj()
car1.licznik()  # Prędkość wynosi 0 km/h
print(car1.__predkosc)  # 0
