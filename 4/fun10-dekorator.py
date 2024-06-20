# dekorator - wykorzystuje mechanizm funkcji zagnieżdżonej
# dekorator przyjmuje funkcje i dodaje nową funkcjonalność
def dekor(func):
    def wew():
        print('Dekorujemy')
        return func()

    return wew


def uppercase_decorator(func):
    def wrapper():
        result = func()
        return result.upper()

    return wrapper


@dekor
def hej():
    print("Hej")


@uppercase_decorator
def greeting():
    return "Hello World!!!"


hej()  # Hej
# Po dodaniu dekoratora do funkcji wynik jest
# Dekorujemy
# Hej
print(greeting())  # Hello World!!!
# po udekorowaniu HELLO WORLD!!!
