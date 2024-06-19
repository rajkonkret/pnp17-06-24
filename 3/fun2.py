# funkcje zwracające wynik
# konczą się słowkiem return
# gdy napotka return wychodzi z funkcji i zwraca dane do miejsca wywołania
def dodaj(a, b):
    return a + b  # return zwraca wynik


def odejmij(a=0, b=0, c=0):
    return a - b - c


def oblicz_vat(cena, vat=23):
    return cena * (100 + vat) / 100


print(dodaj(5, 9))
wyn = dodaj(6, 9)
print("wynik", wyn)
print(odejmij())
print(odejmij(1))
print(odejmij(1, 2))
print(odejmij(1, 2, 3))
print(odejmij(c=9))
print(oblicz_vat(1000))
print(oblicz_vat(1000, 8))
print(oblicz_vat(vat=9, cena=8000))
# 1230.0
# 1080.0
# 8720.0

zm = oblicz_vat(1000)
print("Cena z vat", zm)  # Cena z vat 1230.0
if zm == 1230:
    print("Ok")

print(dodaj(5, 6) + dodaj(7, 90))  # 108
