dictionary = {'imie': "Radek", 'nazwisko': "Kowalski"}

# wyswietla klucze
for i in dictionary:
    print(i)
# imie
# nazwisko

for k in dictionary.keys():
    print(k)
# imie
# nazwisko


# wyswietlenie wartości
for v in dictionary.values():
    print(v)
# Radek
# Kowalski

for i in dictionary.items():
    print(i)
# ('imie', 'Radek')
# ('nazwisko', 'Kowalski')

for k, v in dictionary.items():  # items() - pary
    print(k, "=>", v)
# imie => Radek
# nazwisko => Kowalski
# sep
#         string inserted between values, default a space.
#       end
#         string appended after the last value, default a newline.
for k, v in dictionary.items():  # items() - pary
    print(k, v, sep="=>")
# imie=>Radek
# nazwisko=>Kowalski
print("Radek", end='')
print("Tomek")  # RadekTomek
print("Nastęny")
# RadekTomek
# Nastęny

dictionary_2 = {'name': 'imie', 'company': "Inna"}
d = {}
for k, v in dictionary_2.items():
    d[v] = k
print(d)  # {'Radek': 'imie', 'Kowalski': 'nazwisko'}

print(dictionary_2)
print(d)
print({value: key for key, value in dictionary_2.items()})
# {'name': 'imie', 'company': 'Inna'}
# {'imie': 'name', 'Inna': 'company'}
# {'imie': 'name', 'Inna': 'company'}
