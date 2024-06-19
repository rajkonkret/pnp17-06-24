# while - pętla sterowana warunkiem

licznik = 0
while True:
    print("Komunikat 1 !!!")
    licznik += 1
    if licznik > 10:
        break

print(licznik)  # 11

licznik = 0
while licznik < 10:
    licznik += 1
    print("Komunikat 2 !! !! !!")

# password = input("Podaj hasło")
# while password != 'secret':
#     password = input("Błedne hasło. Podaj ponownie")

print("Hasło prawidłowe")

lista = []
lista_int = []
while True:
    wej = input("Podaj liczbę")  # str
    if not wej.isnumeric():  # if all characters in the string are numeric
        break
    lista.append(wej)
    lista_int.append(int(wej))

print(lista)  # ['222', '333', '1', '45', '66']
print(lista_int)  # [222, 333, 1, 45, 66]
