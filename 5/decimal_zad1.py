# przykład użycia Decimal
import decimal
from decimal import Decimal

kwota1 = Decimal('10.25')
kwota2 = Decimal('5.50')
precyzja = Decimal('0.00')

suma = kwota1 + kwota2
print("Suma:", suma)  # Suma: 15.75

roznica = kwota1 - kwota2
print("Różnica: ", roznica)  # Różnica:  4.75
print("Róznica z precyzją 2:", roznica.quantize(precyzja))  # Róznica z precyzją 2: 4.75

podatek = Decimal('0.23')
kwota_z_podatkiem = kwota1 * (1 + podatek)
print("Kwota z podatkiem", kwota_z_podatkiem)  # Kwota z podatkiem 12.6075
print("Kwota z podatkiem", kwota_z_podatkiem.quantize(precyzja))  # Kwota z podatkiem 12.61

a = Decimal('1.2345')
b = Decimal('2.3456')

c = a + b
print("Wynik", c)  # Wynik 3.5801
preyzja2 = Decimal('0.001')
print("Wynik zaokrąglony", c.quantize(preyzja2))  # Wynik zaokrąglony 3.580
