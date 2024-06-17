# kolekcja
# lista - przechowuje wiele danych, róznego typy w tym samym momencie
# zachowuje kolejność przy dodawaniu elementów

lista = []  # pusta lista
print(lista)  # []
print(type(lista))  # <class 'list'>

pusta_lista = list()
print(type(pusta_lista))
print(pusta_lista)
# <class 'list'>
# []

# append()
lista.append("Radek")
lista.append("Maciek")
lista.append("Bartek")
lista.append("Zenek")
lista.append("Tomek")
print(lista)  # ['Radek', 'Maciek', 'Bartek', 'Zenek', 'Tomek']
#                   0        1          2        3        4
#                   -5       -4         -3       -2       -1
print(lista[0])  # pierwszy
print(lista[3])  # Zenek
# print(lista[8])  # IndexError: list index out of range
print(lista[-2])  # Zenek
print(len(lista))  # 5
print(lista[4])  # 5 - 1, Tomek
print(lista[-1])  # Tomek

# wypisac część listy (fragment) - slicing
print(lista[0:3])  # ['Radek', 'Maciek', 'Bartek'] 0,1,2
print(lista[:3])  # ['Radek', 'Maciek', 'Bartek']
print(lista[2:])  # ['Bartek', 'Zenek', 'Tomek'] 2,3,4
print(lista[:])  # ['Radek', 'Maciek', 'Bartek', 'Zenek', 'Tomek']

print(lista[-2:0])  # []
print(lista[0:-2])  # ['Radek', 'Maciek', 'Bartek']
print(lista[2:3])
print(lista[2:10])  # ['Bartek', 'Zenek', 'Tomek']
print(lista[7:10])  # []
print(lista[2:2])  # []
print(lista[0:3:2])  # ['Radek', 'Bartek'] co drugi start:stop:krok

lista_15 = list(range(15))  # range() - generuje liczby z zakresu 0..14
print(lista_15)  # ['Radek', 'Maciek', 'Bartek', 'Zenek', 'Tomek']
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
print(lista_15[-5:])  # pięć osattnich elemntów, [10, 11, 12, 13, 14]

print(lista)  # ['Radek', 'Maciek', 'Bartek', 'Zenek', 'Tomek']

# nadpisanie elementu na zadanym indeksie
lista[2] = "Mikołaj"
print(lista)  # ['Radek', 'Maciek', 'Mikołaj', 'Zenek', 'Tomek']

# wstawić pomiędzy dw ainne we wskazanym indeksie
lista.insert(1, "Bartek")
print(lista)  # ['Radek', 'Bartek', 'Maciek', 'Mikołaj', 'Zenek', 'Tomek']
lista.insert(11, "Zenek")
print(lista)  # ['Radek', 'Bartek', 'Maciek', 'Mikołaj', 'Zenek', 'Tomek', 'Zenek']

# sprawdzenie indeksu dla danego elementu
print(lista.index("Bartek"))  # indeks 1
indeks = lista.index("Mikołaj")
print(indeks)  # indeks 3

# usunięcie elementu po elemencie - pierwszy napotkany
lista.remove("Tomek")
print(lista)  # ['Radek', 'Bartek', 'Maciek', 'Mikołaj', 'Zenek', 'Zenek']
lista.remove("Zenek")
print(lista)  # ['Radek', 'Bartek', 'Maciek', 'Mikołaj', 'Zenek']
print("Zenek" in lista)  # True

# usunicie elemntu po indeksie - pop()
index = lista.index("Mikołaj")
print(index)  # 3
print(lista.pop(index))  # pop() mówi kogo usunął -> Mikołaj
print(lista)  # ['Radek', 'Bartek', 'Maciek', 'Zenek']
print(lista.pop())  # Zenek - usunie ostatniego z listy
print(lista)  # ['Radek', 'Bartek', 'Maciek']
lista.append("Anna")
lista.append("Tomek")
lista.append("Paulina")
print(lista)  # ['Radek', 'Bartek', 'Maciek', 'Anna', 'Tomek', 'Paulina']
print(lista.pop(-2))  # Tomek
print(lista)

a = 1
b = 3
a = b
print("a =", a, "b =", b)  # a = 3 b = 3
b = 7
print("a =", a, "b =", b)  # a = 3 b = 7

lista_copy = lista.copy()  # kopia elementów listy
lista_a = lista  # a = b, kopiowanie adresu w pamięci gdzie znajduje się lista (referencja)
lista.clear()  # b = 7, czyszczenie listy
print(lista_a)  # a, []
print(lista)  # b, []
print(lista_copy)  # ['Radek', 'Bartek', 'Maciek', 'Anna', 'Paulina']
print(id(lista_a))  # 2828549411200
print(id(lista))  # 2828549411200
print(id(lista_copy))  # 2828549731520

liczby = [54, 999, 34, 12, 22.34, 687]
print(liczby)
print(type(liczby))  # <class 'list'>

liczby.sort()  # sort() - sortowanie
print(liczby)  # [12, 22.34, 34, 54, 687, 999]

liczby_a = [54, 999, 34, 12, 22.34, 687, "A"]
# liczby_a.sort()  # TypeError: '<' not supported between instances of 'str' and 'int'

liczby.reverse()
print(liczby)  # [999, 687, 54, 34, 22.34, 12]

liczby.sort(reverse=True)
print(liczby)  # [999, 687, 54, 34, 22.34, 12]

liczby[3] = 6666
print(liczby[0:3])
print(liczby[-2])
# [999, 687, 54]
# 22.34

liczby.remove(54)
print(liczby)  # [999, 687, 6666, 22.34, 12]
print(liczby[::-1])  # [12, 22.34, 6666, 687, 999]

tekst = "Python"
lista1 = list(tekst)  # list()  rzutowanie na listę
print(lista1)  # ['P', 'y', 't', 'h', 'o', 'n'], rozpakowanie sekwencji

lista3 = [tekst]
print(lista3)  # ['Python']

krotka = tuple(liczby)  # tuple() rzutowanie na krotkę (tuplę)
print(type(krotka))  # <class 'tuple'>
print(krotka)  # (999, 687, 6666, 22.34, 12)
