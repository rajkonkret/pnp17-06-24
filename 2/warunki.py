# instrukcje warunkowe
# instrukcje sterowania przepływem programu
# if
# w zależnosci od warunku wykonuje jedna lub druga operacje

odp = True
# odp = False
if odp:
    print("Brawo")
    print("Brawo")
    print("Brawo")
    print("Brawo")

print("Dalsza częśc programu")

odp = "Radek"
if odp == "Radek":
    print("To jest Radek")

print(odp == "Radek")  # True

print(bool(odp))  # True
if odp:
    print("To jest", odp)  # To jest Radek

if odp == "Tomek":
    print("To jest Tomek")
else:  # w przeciwnym przypadku
    print("To nie jest Tomek")
# To nie jest Tomek

# podatek = 0
# zarobki = int(input("Podaj dochód"))
# if zarobki < 10000:
#     podatek = 0
# elif zarobki < 30000:
#     podatek = 0.2
# elif zarobki < 100000:  # od 10000 do 99999
#     podatek = 0.4  # 40%
# else:
#     podatek = 0.9
#
# print(f"Podatek wynosi {podatek * zarobki}")
# # dodac przedział 10000 do 29999 podatek 0.2

suma_zam = 150
if suma_zam > 100:
    rabacik = 25

print("Rabat wynosi", rabacik)  # Rabat wynosi 25
rabat = 25 if suma_zam > 100 else 0
print("Rabat wynosi", rabat)  # Rabat wynosi 25

# zasymulujemy system zbierania logów
# zmienne będa przechowywac dane, które przyszły z zewnętrznego systemu
# email, console, inny
# dla console: "Stało sę coś strasznego"
# dla email: "System email"
# poziomy ważnosci error, medium, inny
# wzależności od poziomu ważnosci dodamy do listy opis komunikatu
# np.: "Wystąpił bład error"
lista_b = []
alert_system = 'email'
error = 'error'
if alert_system == 'console':
    print("Stało się coś strasznego")
elif alert_system == 'email':
    print("Sytem email")
    if error == 'error':
        lista_b.append('Wystąpił bład typu error')
    elif error == 'medium':
        lista_b.append("Wystąpiło ostrzeżenie")
    else:
        lista_b.append("Bład inny")
else:
    print("inny system")

print(lista_b)
# ['Wystąpił bład typu error']

# napisac test z.... historii

punkty = 0
odp = input("Podaj date Chrztu polski")
if odp == '966':
    print("Odpowiedź prawidłowo")
    punkty += 1  # punkty = punkty + 1
else:
    print("Masz to w książce na stronie 23")

print('Punkty', punkty)
