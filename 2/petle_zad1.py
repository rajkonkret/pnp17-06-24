# petle - możliwość wykonania wielokrotnie tego samego zadania
# for - petla iteracyjna
import random

for i in range(5):  # 0..4
    print(i)
# 0
# 1
# 2
# 3
# 4

for i in range(10):
    pass  # nic nie rób

for _ in range(5):  # _ niema zmienna
    print("Test")
    print(_)
# 0
# Test
# 1
# Test
# 2
# Test
# 3
# Test
# 4

for i in range(20):
    print(i * 2)

# lotto z pętlą
lista_kule = list(range(1, 50))

lista_wylosowane = []
for i in range(6):
    wyn = random.choice(lista_kule)
    lista_kule.remove(wyn)
    print(wyn)
    lista_wylosowane.append(wyn)

print(lista_wylosowane)  # [25, 37, 40, 35, 17, 12]

for i in range(10):
    if i % 2 == 0:  # modulo, reszta z dzielenia
        print(i, "parzysta")
# 0 parzysta
# 2 parzysta
# 4 parzysta
# 6 parzysta
# 8 parzysta

lista3 = [j for j in range(10) if j % 2 == 0]
print(lista3)  # [0, 2, 4, 6, 8]
for j in range(10):
    if j % 2 == 0:
        print("Do listy dodaj to j co spełnia warunek")

for c in lista_wylosowane:  # mozesz lista3
    if c > 10:
        print("Większe od 10", c)
    print(c)
# 5
# Większe od 10 45
# 45
# Większe od 10 11
# 11
# Większe od 10 49
# 49
# Większe od 10 30
# 30
# Większe od 10 39
# 39

for i in range(0, 10, 2):  # start, stop, krok
    print(i)

for i in range(10, 0, -2):  # odlicza do tyłu
    print(i)

for i in range(-10, 0):
    print(i)

for c in lista3:  # [0, 2, 4, 6, 8]
    if c == 2:
        c += 1
    print(c)
# 0
# 3
# 4
# 6
# 8
# spam += 1    spam = spam + 1
# spam -= 1    spam = spam - 1
# spam *= 1    spam = spam * 1
# spam /= 1    spam = spam / 1
# spam %= 1    spam = spam % 1

imiona = ['Radek', 'Tomek', "Zenek", "Ania"]
print(imiona)  # ['Radek', 'Tomek', 'Zenek', 'Ania']
print(type(imiona))  # <class 'list'>

for p in imiona:
    print(p)
# Radek
# Tomek
# Zenek
# Ania

# wyswietlic z tej listy w postaci 0 Radek
for p in imiona:
    print(imiona.index(p), p)
# 0 Radek
# 1 Tomek
# 2 Zenek
# 3 Ania
for i in range(len(imiona)):  # range(4) 0..3
    print(i, imiona[i])
# 0 Radek
# 1 Tomek
# 2 Zenek
# 3 Ania

# enumerate() - zwraca numer elementu i elemnt z kolekcji
for p in enumerate(imiona):
    print(p)
# (0, 'Radek')
# (1, 'Tomek')
# (2, 'Zenek')
# (3, 'Ania')
a, b = (0, 'Radek')
print(a, b)  # 0 Radek
for i, p in enumerate(imiona):
    print(i, p)
# 0 Radek
# 1 Tomek
# 2 Zenek
# 3 Ania
for i, p in enumerate(imiona, start=1):
    print(i, p)
# 1 Radek
# 2 Tomek
# 3 Zenek
# 4 Ania

ludzie = ['Radek', 'Arek', 'Tomek', "Zenek"]
wiek = [44, 55, 66, 23]

# Radek 44
for i in ludzie:
    print(i, wiek[ludzie.index(i)])
# Radek 44
# Arek 55
# Tomek 66
# Zenek 23
ludzie = ['Radek', 'Arek', 'Tomek', "Zenek", "Ania"]
wiek = [44, 55, 66, 23]
# for i in ludzie:
#     print(i, wiek[ludzie.index(i)])  # IndexError: list index out of range

# zip() - łączy kolekcje
for i in zip(ludzie, wiek):
    print(i)
# ('Radek', 44)
# ('Arek', 55)
# ('Tomek', 66)
# ('Zenek', 23)
for p, w in zip(ludzie, wiek):
    print(p, w)
# Radek 44
# Arek 55
# Tomek 66
# Zenek 23

# 0 Radek 44
for i in enumerate(zip(ludzie, wiek)):
    print(i)
# (0, ('Radek', 44))
# (1, ('Arek', 55))
# (2, ('Tomek', 66))
# (3, ('Zenek', 23))
a, b = 0, ('Radek', 44)
print(a, b)  # 0 ('Radek', 44)
c, d = ('Radek', 44)
print(c, d)  # Radek 44
(a, (c, d)) = (0, ('Radek', 44))
print(a, c, d)  # 0 Radek 44
for i, (o, w) in enumerate(zip(ludzie, wiek)):
    print(i, o, w)
# 0 Radek 44
# 1 Arek 55
# 2 Tomek 66
# 3 Zenek 23
