# funkcję obliczającą średnią
def liczby(name=None, *cyfry):
    print(cyfry)  # (11, 2, 3)
    suma = 0
    count = len(cyfry)
    suma_p = sum(cyfry)
    print(suma_p)  # 16
    try:
        for c in cyfry:
            suma += c
        avg = suma / count
    except Exception as e:
        print("Bład", e)
    else:
        print(f"Średnia dla ucznia {name}  wynosi {avg}")
    finally:
        print("Zakończono obliczenia")


liczby()
liczby("Raadek", 1)
liczby("Tomek", 11, 2)
liczby("Zenek", 11, 2, 3)
# ()
# Bład division by zero
# Zakończono obliczenia
# (1,)
# Średnia dla ucznia Raadek  wynosi 1.0
# Zakończono obliczenia
# (11, 2)
# Średnia dla ucznia Tomek  wynosi 6.5
# Zakończono obliczenia
# (11, 2, 3)
# Średnia dla ucznia Zenek  wynosi 5.333333333333333
# Zakończono obliczenia
# ctrl / - komentowanie zaznaczonego fragmentu
