# wyjątki
# print(5 / 0)
# Traceback (most recent call last):
#   File "C:\Users\CSComarch\PycharmProjects\pdnp17-06-24\2\wyjatki.py", line 2, in <module>
#     print(5 /0 )
#           ~~^~
# ZeroDivisionError: division by zero
numer = 90
try:
    # print(numer / 0)
    # print(5 / "00")
    # print("A" + 9)
    wynik = 5 / 1
except ZeroDivisionError:
    print("Dzielenie przez zero")
except TypeError:
    print("Bład typu")
except ValueError:
    print("Bład wartości")
except Exception as e:
    print("Bład", e)
else:  # wykona się tylko wtedy gdy nie bedzie błedu
    print("Wynik", wynik)  # Wynik 5.0
finally:  # wykona się zawsze
    print("Obliczenia wykonane")

print("Program nadal działa")
# Dzielenie przez zero
# Program nadal działa
# try - except [else - finally]
