a = 10
b = 10


def dodaj():
    a = 7  # zmienne lokalne
    b = 9
    print(a + b)


def dodaj2():
    print(a + b)


def dodaj3():
    global a  # print(f"Wartość a z góry wynosi {a}")  # Wartość a z góry wynosi 9
    a = 9  # a jest globalne, zmieni wartość globalnej zmiennej a
    b = 8
    print(a + b)


print(f"Wartość a z góry wynosi {a}")  # Wartość a z góry wynosi 10
dodaj()  # 16
print(f"Wartość a z góry wynosi {a}")  # Wartość a z góry wynosi 10
dodaj2()  # 20
print(f"Wartość a z góry wynosi {a}")  # Wartość a z góry wynosi 10
dodaj3()  # 17
print(f"Wartość a z góry wynosi {a}")  # Wartość a z góry wynosi 9
dodaj2()  # 19
