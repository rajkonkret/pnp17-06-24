# funkcja - wydzielony fragment kodu, można go wywołać w dowolnym momencie
# deklarqacja funkcji musi być wcześniej niż wywołanie
# w miejscu deklaracji funkcja się nie wykonuje
# żeby funkcję wykonać trzeba ją wywołać

a = 6
b = 8


# deklaracja funkcji - tu się nie wykona
# słowko def nazwa funkcji nawiasy
# PEP8 wymaga by były dwie puste linie
def dodaj():  # funkcja bez argumentów
    print(a + b)  # użyła wartości zmiennych globalnych


def dodaj2(a, b):  # funkcja z dwoma argumentami obowiązkowymi
    print(a + b)


def odejmij(a, b, c=0):  # funkcja z domyslnym argumentem c o wartości 0
    print(a - b - c)


# wywołanie funkcji
# nazwa funkji i nawiasy ()
dodaj()  # 14
# dodaj2()  # TypeError: dodaj2() missing 2 required positional arguments: 'a' and 'b'
# argumenty przekazywane po pozycji
dodaj2(5, 7)  # 12, musimy obowiązkowo przekazać dwa argumenty
odejmij(1, 2, 3)  # -4
odejmij(1, 2)  # -1 c=0
# argumenty nazwane
odejmij(c=9, b=9, a=76)  # 58
odejmij(b=9, a=87)  # 78
# argumenty mieszane
odejmij(1, c=9, b=9)
# odejmij(a=1, b=9, 6)  # SyntaxError: positional argument follows keyword argument
print(dodaj())  # None
# print(dodaj() + dodaj2(6, 7))
# TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'
