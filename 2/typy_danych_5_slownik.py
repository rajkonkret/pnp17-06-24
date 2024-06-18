# słownik - para klucz wartosc
# {'user': 'Radek', 'wiek':50}
# słownik jest odpowiednikiem jsona
# klucze nie mogą się powtarzać

# pusty słownik
dictionary = dict()
print(dictionary)  # {}
print(type(dictionary))  # <class 'dict'>

dictionary1 = {}
print(dictionary1)  # {}

print(dictionary.keys())
print(dictionary.values())
print(dictionary.items())
# dict_keys([])
# dict_values([])
# dict_items([])

# dodanie do słownika
dictionary['imie'] = "Radek"
print(dictionary)  # {'imie': 'Radek'}
dictionary['wiek'] = 37
print(dictionary)  # {'imie': 'Radek', 'wiek': 37}

# nadpisanie elementu
dictionary['imie'] = "Tomek"
print(dictionary)  # {'imie': 'Tomek', 'wiek': 37}

# wypisanie elementu
print(dictionary['imie'])  # Tomek
print(dictionary.keys())
print(dictionary.values())
print(dictionary.items())
# dict_keys(['imie', 'wiek'])
# dict_values(['Tomek', 37])
# dict_items([('imie', 'Tomek'), ('wiek', 37)])
# print(dictionary['name'])  # KeyError: 'name'
print(dictionary.get('name'))  # None
print(dictionary.get('name', 'default'))  # default

dictionary.update({'date': '12-12-2024'})
print(dictionary)  # {'imie': 'Tomek', 'wiek': 37, 'date': '12-12-2024'}

dict_small = {'x': 2}
dict_small.update([('y', 3), ('z', 4)])
print(dict_small)  # {'x': 2, 'y': 3, 'z': 4}

# input() - pobiera dane np.: od użytkownika
# tekst = input("Wpisz tekst")  # str()
# print(tekst)

# napisac program słownik pol-ang
# zbior danych - w słowniku
# wyswietlic klucze
# pobrac  słowko od uzytkownika
# wypisać tłumaczenie
dict_pol_ang = {'kot': 'cat', 'pies': 'dog', 'jabłko': 'apple'}
print(dict_pol_ang.keys())
odp = input("Podaj słówko do przetłumaczenia")
# print(dict_pol_ang[odp.replace(" ", "").lower()])
print(dict_pol_ang.get(odp.replace(" ", "").lower(), "nie ma takiego słowka"))

# aplikacja kalkulator
# pobrac dwie liczby
# wypisac wynik (np.: dodawanie)
a = input("Podaj pierwszą liczbę")
b = int(input("Podaj drugą liczbę"))
print(float(a) + b)

c = input("Podaj operacje")
dzialanie = str(a) + c + str(b)
print(dzialanie)
print(eval(dzialanie))
# 5-6
# -1
print(eval("3*30+15/45"))  # 90.33333333333333
