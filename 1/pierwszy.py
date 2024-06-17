import sys

print()  # wypisz/wydrukuj

print("Nazywam się Radek")
print('Nazywam się Radek')
# print('Nazywam się Radek")  # SyntaxError: unterminated string literal (detected at line 5)
# ctrl / - kometarz
print("Nazywam się 'Radek'")  # Nazywam się 'Radek'
print("Nazywam się 'Radek'")  # Nazywam się 'Radek'
print("Nazywam się 'Radek'")  # Nazywam się 'Radek'
print("Nazywam się 'Radek'")  # Nazywam się 'Radek'
print("Nazywam się 'Radek'")  # Nazywam się 'Radek'
print("Nazywam się 'Radek'")  # Nazywam się 'Radek'
print("Nazywam się 'Radek'")  # Nazywam się 'Radek'
print("Nazywam się 'Radek'")  # Nazywam się 'Radek'
# ctrl d - powielanie linijek

# type() - sprawdzenie typu danych
print(type("Nazywam się Radek"))  # <class 'str'> - dane tekstowe
print("39")
print(type("39"))  # <class 'str'>
print(39)
print(type(39))  # <class 'int'> liczby całkowite
print(sys.int_info)
# sys.int_info(
#     bits_per_digit=30,
#     sizeof_digit=4,
#     default_max_str_digits=4300,
#     str_digits_check_threshold=640
# )
print("39" + "39")  # 3939 - konkatenacja - łączenie stringów
print(39 + 39)  # 78
# print(39 + "39")  #  # TypeError: unsupported operand type(s) for +: 'int' and 'str'
# silne typowanie - nie zmienia sam typów
print(int("39") + 39)  # int() rzutowanie na int (zamiana)  # 78

print(5 * "4")  # 44444

# zmienna - pudełko, pojemnik na dane. Zmienna w jedej chwili może przechowywać jeden element
# snake_case
# typowanie dynamiczne - każdej chwili możemy dowolny typ wrzucić do zmiennej
name = "Radek"
print(type(name))  # <class 'str'>
print(name)  # Radek
print(name + "Kowalski")  # RadekKowalski

name = 39
print(type(name))  # <class 'int'>
print(name)  # 39
# print(name + "Kowalski")  # TypeError: unsupported operand type(s) for +: 'int' and 'str'
print(str(name) + "Kowalski")  # str() - rzutowanie na str, 39Kowalski
print(type(name))  # <class 'int'> nie zmienilismy zawartości zmiennej

name: str = 90  # to tylko podpowiedź
print(name)
print(type(name))  # <class 'int'>

age = 47
print(age)
print(type(age))  # <class 'int'>
