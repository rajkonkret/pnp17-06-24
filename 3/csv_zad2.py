import csv

fields = []  # nazwy kolumn
rows = []  # dane z poszczególnych wierszy

# filename = 'records_2.csv'
filename = 'records_3.csv'

with open(filename, 'r') as f:
    csvreader = csv.reader(f)
    print(csvreader)  # <_csv.reader object at 0x00000236369D58A0> iterator
    # iterator - zwraca kolejne elementy
    # za kazym razem gdy go odczytuje zwraca następny elemnent
    # zapamiętuje gdzie skońćzył
    fields = next(csvreader)  # next() odczyt pojedynczego elemntu z iteratora
    # lista fields otrzyma dane z pierwszego wierszaw csv czyli kolumny
    for row in csvreader:  # dalsze odczytywanie iteratora zacznie się od elementu drugiego
        # print(row)
        rows.append(row)

print("Fields", fields)
print("Rows", rows)
# Fields ['name', 'branch', 'year', 'cgpa']
# Rows [['Radek', 'Coe', '2', '9.1']]
