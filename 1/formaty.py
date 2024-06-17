user = "Tomek"  # str
wiek = 39  # int
wersja = 3.900001  # float - liczby zmiennoprzecinowe
print(type(wersja))  # <class 'float'>
liczba = 678123456345  # int

print("Witaj %s masz teraz %d lat" % (user, wiek))
# Witaj Tomek masz teraz 39 lat
# sprawdza typy !!!
# print("Witaj %d masz teraz %s lat" % (user, wiek))  # TypeError: %d format: a real number is required, not str
# %s - str
# %d - digit

print("Witaj %(user)s, masz teraz %(wiek)d lat." % {'user': user, 'wiek': wiek})
print("Witaj %(user)s, masz teraz %(age)d lat." % {'user': user, 'age': wiek})
# Witaj Tomek, masz teraz 39 lat.
# Witaj Tomek, masz teraz 39 lat.

print(f"Witaj {user}, masz teraz {wiek} lat.")  # Witaj Tomek, masz teraz 39 lat.
print("Witaj {}, masz teraz {} lat.".format(user, wiek))  # Witaj Tomek, masz teraz 39 lat.

print("Używamy wersji pythona %i" % 3)  # %i int
# przy %f zaokrągla przy wyświetlaniu
print("Używamy wersji pythona %f" % 3.9)  # %f float, Używamy wersji pythona 3.900000
print("Używamy wersji pythona %.1f" % 3.9)  # %f float, Używamy wersji pythona 3.9
print("Używamy wersji pythona %.2f" % 3.9)  # %f float, Używamy wersji pythona 3.90
print("Używamy wersji pythona %.0f" % 3.9)  # %f float, Używamy wersji pythona 4
print("Używamy wersji pythona %.f" % 3.9)  # %.f 0 miejsc po przecinku, Używamy wersji pythona 4
x = 3.14
print("Zero miejsc po przecinku %.f" % x)  # Zero miejsc po przecinku 3
print("X się nie zmieniło", x)  # X się nie zmieniło 3.14

y = round(x)
print('x = ', x)
print('y = ', y)
# x =  3.14
# y =  3

x = 3.1415
print(round(x, 3))
int_part, fract_part = divmod(x, 1)
print(int_part, fract_part)  # 3.0 0.14150000000000018

x_int = int(x)
x_fract = x - x_int
print(x_int, x_fract)  # 3 0.14150000000000018

print(f"Używamy wersji pythona {wersja}")
print(f"Używamy wersji pythona {wersja:.1f}")
print(f"Używamy wersji pythona {wersja:.2f}")
print(f"Używamy wersji pythona {wersja:.0f}")
# Używamy wersji pythona 3.900001
# Używamy wersji pythona 3.9
# Używamy wersji pythona 3.90
# Używamy wersji pythona 4

print(f"{user:>10}")  # "     Tomek"
print(f"{user:<20}")  # "Tomek               "
print(f"{user:^20}")  # "       Tomek        "
print(f"{user:*^20}")  # *******Tomek********

print(liczba)  # 678123456345
print("Nasza duża liczba {:,}".format(liczba))  # Nasza duża liczba 678,123,456,345
print("Nasza duża liczba {:,}".format(liczba).replace(",", "."))  # Nasza duża liczba 678.123.456.345
print("Nasza duża liczba {:,}".format(liczba).replace(",", " "))  # Nasza duża liczba 678 123 456 345

print(f"Nasza duża liczba {liczba:,}")
print(f"Nasza duża liczba {liczba:,}".replace(",", "."))
print(f"Nasza duża liczba {liczba:,}".replace(",", " "))
# Nasza duża liczba 678,123,456,345
# Nasza duża liczba 678.123.456.345
# Nasza duża liczba 678 123 456 345

liczba_2 = 123_456_789_123
print(liczba_2)  # 123456789123
print(type(liczba_2))  # <class 'int'>
