# funkcja lambda - skrócony zapis funkcji
# zwraca wynik
# funkcja anonimowa, mozliwosc deklaracji w miejscy wykonania

def odejmij2(a, b):
    return a - b


print(odejmij2(4, 5))  # -1

odejmij = lambda a, b: a - b
print(odejmij(4, 5))  # -1

oblicz_vat = lambda cena, vat=23: cena * (100 + vat) / 100
print(oblicz_vat(1000))
print(oblicz_vat(1000, 8))
print(oblicz_vat(vat=15, cena=10000))
# 1230.0
# 1080.0
# 11500.0

wiek = lambda x: "dziecko" if x < 10 else ("nastolatek" if x < 18 else "dorosły")
print(wiek(9))  # dziecko
print(wiek(10))  # nastolatek
print(wiek(17))  # nastolatek
print(wiek(18))  # dorosły
print(wiek(25))  # dorosły

lista = [1, 2, 5, 34, 56, 100, 200, 500]
# wypisanie tej listy z wartoscmi pomnożonymi przez 2

l = []
for i in lista:
    l.append(int(i) * 2)
print(l)  # [2, 4, 10, 68, 112, 200, 400, 1000]

print([i * 2 for i in lista])  # [2, 4, 10, 68, 112, 200, 400, 1000]


def zmien(x):
    return x * 2


l2 = []
for i in lista:
    l2.append(zmien(i))
print(l2)  # [2, 4, 10, 68, 112, 200, 400, 1000]

# funkcje wyższego rzędu
# map() - bierze elemnt z kolekcji, wykonuje funkcje dla zadanego argumentu
print(f"Zastsowanie map(): {list(map(zmien, lista))}")
# Zastsowanie map(): [2, 4, 10, 68, 112, 200, 400, 1000]
# uzycie lambda jako funkcji anonimowej, zadeklarowanej w miejscu wykonania
print(f"Zastsowanie map(): {list(map(lambda x: x * 2, lista))}")
# Zastsowanie map(): [2, 4, 10, 68, 112, 200, 400, 1000]
print(f"Zastsowanie map(): {list(map(lambda x: x * 4, lista))}")
print(f"Zastsowanie map(): {list(map(lambda x: x * 14, lista))}")

# filtrowanie danych
l3 = []
for i in lista:
    if i < 3:
        l3.append(i)
print(l3)  # [1, 2]

# filter() - pobiera element z kolekcji
# zwraca spełniający warunek
print(f"Zastosowanie filter() {list(filter(lambda x: x < 3, lista))}")
# Zastosowanie filter() [1, 2]
print(f"Zastosowanie filter() {list(filter(lambda x: x < 3, lista))}")
# l4 = []
# l4.append(lambda x: x < 3)
# print(l4)  # [<function <lambda> at 0x0000020BD649BBA0>]
# print(f"Zastosowanie filter() {list(map(lambda x: x < 3, lista))}")
# # Zastosowanie filter() [True, True, False, False, False, False, False, False]
# def zmien2(x):
#     return x < 3
# x > 200
# x > 5 i x < 100
print(f"Zastosowanie filter() {list(filter(lambda x: x > 100, lista))}")
# Zastosowanie filter() [200, 500]
print(f"Zastosowanie filter() {list(filter(lambda x: x > 5 and x < 100, lista))}")
# Zastosowanie filter() [34, 56]
print(f"Zastosowanie filter() {list(filter(lambda x: 5 < x < 100, lista))}")
# Zastosowanie filter() [34, 56]
