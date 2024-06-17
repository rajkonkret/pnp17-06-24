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
