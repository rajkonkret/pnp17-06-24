# zbiór - set - przechowuje unikalne elementy
# nie zachowuje kolejności przy dodawaniu elementów
# nie posiada indeksu

lista = [44, 55, 66, 777, 33, 22, 11, 33, 11]
zbior = set(lista)  # set() - rzutowanie na zbiór (set)
print(zbior)  # {33, 66, 777, 11, 44, 22, 55}
print(type(zbior))  # <class 'set'>

# utworzenie pustego zbioru
zb2 = set()  # <class 'set'>
print(zb2)  # set()

# dodawnie elemntów do zbioru
zbior.add(33)
zbior.add(18)
zbior.add(18)
print(zbior)  # {33, 66, 777, 11, 44, 18, 22, 55}

# usunięcie elementu ze zbioru
zbior.remove(55)
print(zbior)  # {33, 66, 777, 11, 44, 18, 22}

# pop() -
print(zbior.pop())  # 33 usunięcie pierwszego elemntu
print(zbior)  # {66, 777, 11, 44, 18, 22}

zbior_copy = zbior.copy()
print(zbior_copy)
print(id(zbior))  # 1875380526816
print(id(zbior_copy))  # 1875380529504

zbior_2 = {667, 11, 44, 18, 52, 62, 999, 999, 12.24}
print(zbior_2)  # {999, 11, 44, 12.24, 18, 52, 667, 62}
print(type(zbior_2))  # <class 'set'>

# suma zbiorów
print(zbior | zbior_2)  # {66, 999, 777, 11, 44, 12.24, 18, 52, 22, 667, 62}
print(zbior)  # {66, 777, 11, 44, 18, 22}
print(zbior_2)  # {999, 11, 44, 12.24, 18, 52, 667, 62}
print(zbior.union(zbior_2))
# {66, 999, 777, 11, 44, 12.24, 18, 52, 22, 667, 62}

# część wspólna
print(zbior & zbior_2)  # {18, 11, 44}
print(zbior.intersection(zbior_2))  # {18, 11, 44}

# róznica
print(zbior - zbior_2)  # {777, 66, 22}
print(zbior.difference(zbior_2))
# ----

# łaczy zbiory, zmienia zbior bazowy
zbior.update(zbior_2)
print(zbior)  # {66, 999, 777, 11, 44, 12.24, 18, 52, 22, 667, 62}

lista = list(zbior_2)
print(lista)

krotka = tuple(zbior)
print(krotka)
# [999, 11, 44, 12.24, 18, 52, 667, 62]
# (66, 999, 777, 11, 44, 12.24, 18, 52, 22, 667, 62)
