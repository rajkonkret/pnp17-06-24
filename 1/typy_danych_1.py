import sys

wiek = 47
rok = 2024
temp = 36.6

print(temp)
print(type(temp))  # <class 'float'>

print(5 * wiek)  # 235
print(5 * "wiek")  # wiekwiekwiekwiekwiek

print(wiek * rok)
print(wiek + rok)
print(wiek - rok)
print(wiek / rok)  # wynik dzielenia float, 0.023221343873517788
print(rok // wiek)  # 2024 // 47 = 43 całe, część całkowita z dzielenia
x = 3.14
print(x // 1)  # 3.0 - część całkowita z dzielenia
print(rok % wiek)  # modulo, reszta z dzielenia (jak na patyczkach) 3
print(2024 / 47)  # 43.06382978723404
print(43 * 47)  # 2021
# 2024 - 2021 = 3
print(5 % 2)  # 5 % 2 = 1
print(wiek ** rok)  # potęgowanie
# len() - dlugosc str, kolekcji
print(len(str(wiek ** rok)))  # długość 3385
print(54 - 5 * 43 + 4 / 2 + 4 / 2)  # -157.0
print(54 - 5 * 43 + (4 / 2 + 4) / 2)  # -158.0

# przy liczbach float mamy bład zaokrąglenia
print(0.2 + 0.8)  # 1.0
print(0.2 + 0.7)  # 0.8999999999999999
print(0.1 + 0.3)  # 0.4
print(0.1 + 0.2)  # 0.30000000000000004
print(sys.float_info)
# sys.float_info(max=1.7976931348623157e+308,
#                max_exp=1024,
#                max_10_exp=308,
#                min=2.2250738585072014e-308,
#                min_exp=-1021,
#                min_10_exp=-307,
#                dig=15, mant_dig=53,
#                epsilon=2.220446049250313e-16,
#                radix=2,
#                rounds=1)

print(f"Sprawdzenie zmiennej {temp} {wiek}")  # Sprawdzenie zmiennej 36.6 47
print(f"""
{wiek}
    {temp}""")
# "47
#     36.6"

# typ logiczny
# prawda, fałsz
# True, False
czy_znasz_python = True
print(type(czy_znasz_python))  # <class 'bool'> logiczny
# 1 - prawda, 0 - falsz
print(int(False))  # 0
print(int(czy_znasz_python))  # 1

x = 1
print(bool(x))  # bool() - zamiana na typ logiczny (rzutowanie), True
x = 100
print(bool(x))  # True
x = -10
print(bool(x))  # True
x = "radek"
print(bool(x))  # True
x = ''
print(bool(x))  # False
x = None  # nic, stan niokreslony -> null
print(bool(x))  # False

# działania logiczne
# and - i
print(True and True)  # True
print(True and False)  # False
print(False and True)  # False
print(False and False)  # False

# or - lub
print(True or True)  # True
print(True or False)  # True
print(False or True)  # True
print(False or False)  # False

# not - negacja
print(not True)  # False
print(not False)  # True

x = 0
print(not x == 1)  # == porównanie  True

a = 8
b = 6
print(f"Porównanie {a} > {b}", a > b)
print(f"Porównanie {a} < {b}", a < b)
print(f"Porównanie {a} == {b}", a == b)  # == równy
print(f"Porównanie {a} != {b}", a != b)  # różny
print(f"Porównanie {a} >= {b}", a >= b)  # różny
print(f"Porównanie {a} <= {b}", a <= b)  # różny
# Porównanie 8 > 6 True
# Porównanie 8 < 6 False
# Porównanie 8 == 6 False
# Porównanie 8 != 6 True
# Porównanie 8 >= 6 True
# Porównanie 8 <= 6 False
