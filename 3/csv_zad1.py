# pliki csv
# plik tekstowy w którym wartości są oddzielone znakiem podziału (,;tab)
# Kowalski,Jan,Kłodzko
# Nowak,Zenon,Szczecin
# Brzęczyszczykiewicz,Grzegorz,Chrząszczyżewoszyce

import csv

filename = 'records.csv'
row = ['Radek', 'Coe', 2, '9.1']
fields = ['name', 'branch', 'year', 'cgpa']

dictionary = dict(zip(fields, row))
print(dictionary)  # {'name': 'Radek', 'branch': 'Coe', 'year': 2, 'cgpa': '9.1'}

with open(filename, 'w', newline='') as csv_f:
    csvwriter = csv.writer(csv_f)
    csvwriter.writerow(fields)
    csvwriter.writerow(row)

filename_2 = 'records_2.csv'
with open(filename_2, 'w', newline='') as f:
    csvwriter = csv.DictWriter(f, fieldnames=fields)
    csvwriter.writeheader()
    csvwriter.writerow(dictionary)

dict_list = [
    {'name': 'Radek', 'branch': 'Coe', 'year': 2, 'cgpa': '9.1'},
    {'name': 'Tomek', 'branch': 'Cow', 'year': 3, 'cgpa': '9'},
    {'name': 'Ania', 'branch': 'Cos', 'year': 5, 'cgpa': '0.1'},
    {'name': 'Zenek', 'branch': 'Cot', 'year': 12, 'cgpa': '19.1'},
    {'name': 'Wladek', 'branch': 'Coy', 'year': 21, 'cgpa': '95.1'},
]

filename_3 = 'records_3.csv'
with open(filename_3, 'w', newline='') as f:
    csvwriter = csv.DictWriter(f, fieldnames=fields)
    csvwriter.writeheader()
    csvwriter.writerows(dict_list)
