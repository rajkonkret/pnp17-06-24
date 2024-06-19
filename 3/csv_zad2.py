import csv

fields = []  # nazwy kolumn
rows = []  # dane z poszczególnych wierszy

# filename = 'records_2.csv'
filename = 'records_3.csv'

with open(filename, 'r') as f:
    dialect = csv.Sniffer().sniff(f.read(1024))  # wyszukanie znaku podziału w pliku csv
    print(dialect.delimiter)  # ;
    print(dialect.quotechar)  # "
    f.seek(0)  # zerujemy odczyt na początek pliku (f.read() odczytało wczesniej 1024 znaki)
    # csvreader = csv.reader(f, delimiter=";")
    csvreader = csv.reader(f, delimiter=dialect.delimiter)
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
# Fields ['name;branch;year;cgpa']
# Rows [['Radek;Coe;2;9.1'], ['Tomek;Cow;3;9'],
# ['Ania;Cos;5;0.1'], ['Zenek;Cot;12;19.1'],
# ['Wladek;Coy;21;95.1']]
# Fields['name', 'branch', 'year', 'cgpa']
# Rows[['Radek', 'Coe', '2', '9.1'],
# ['Tomek', 'Cow', '3', '9'],
# ['Ania', 'Cos', '5', '0.1'],
# ['Zenek', 'Cot', '12','19.1'],
