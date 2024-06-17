# krotka - tupla - kolekcja niemutowalna
# pozwala lepiej wykorzystac pamiec komputera
# krotka jednoelemntowa - zmienna (stała)

tupla = ("Radek")
print(type(tupla))  # <class 'str'>

tupla_2 = ("Radek",)  # PEP8 prosi w jedoelemntowych uzywac nawiasów
print(type(tupla_2))  # <class 'tuple'>

tupla_3 = "Radek",
print(type(tupla_3))  # <class 'tuple'>

tupla_liczby = (43, 55, 22.34, 11, 200)
print(tupla_liczby)

# tupla_liczby[2] = 0  # TypeError: 'tuple' object does not support item assignment

print(tupla_liczby.count(11))  # 1
print(tupla_liczby.index(11))  # 3

# del tupla_liczby[0]  # TypeError: 'tuple' object doesn't support item deletion
del tupla_liczby  # usunięcie calej tupli
# print(tupla_liczby)  # NameError: name 'tupla_liczby' is not defined

# rozpakowanie tupli (krotki)
tup = 1, 2  # tupla
a, b = 1, 2
print(a, b)
a, b = tup  # a, b = 1, 2
print(a, b)

tup_1 = 1, 2, 3
# a, b = tup_1  # ValueError: too many values to unpack (expected 2)
# print(a, b)

a, *b = tup_1
print(a, b)  # 1 [2, 3]  * worek na pozostałe dane
print(len(tup_1))  # 3

tupla_names = "Radek", "Tomek", "Ania", "Zenek"
name1, name2, *name3 = tupla_names
print(name1, name2, name3)  # Radek Tomek ['Ania', 'Zenek']

name1, *name2, name3 = tupla_names
print(name1, name2, name3)  # Radek ['Tomek', 'Ania'] Zenek

*name1, name2, name3 = tupla_names
print(name1, name2, name3)  # ['Radek', 'Tomek'] Ania Zenek

lista = list(tupla_names)
print(lista)  # ['Radek', 'Tomek', 'Ania', 'Zenek']
print(type(lista))  # <class 'list'>

# sortowanie tupli zwraca listę
print(sorted(tupla_names))  # ['Ania', 'Radek', 'Tomek', 'Zenek']
