import pandas

# pip install pandas

data = pandas.read_csv('records_3.csv', delimiter=";")
print(data)
#      name branch  year  cgpa
# 0   Radek    Coe     2   9.1
# 1   Tomek    Cow     3   9.0
# 2    Ania    Cos     5   0.1
# 3   Zenek    Cot    12  19.1
# 4  Wladek    Coy    21  95.1
print(data.columns)  # Index(['name', 'branch', 'year', 'cgpa'], dtype='object')
print(data.values)
# [['Radek' 'Coe' 2 9.1]
#  ['Tomek' 'Cow' 3 9.0]
#  ['Ania' 'Cos' 5 0.1]
#  ['Zenek' 'Cot' 12 19.1]
#  ['Wladek' 'Coy' 21 95.1]]
print(data.items)
# <bound method DataFrame.items of      name branch  year  cgpa
# 0   Radek    Coe     2   9.1
# 1   Tomek    Cow     3   9.0
# 2    Ania    Cos     5   0.1
# 3   Zenek    Cot    12  19.1
# 4  Wladek    Coy    21  95.1>
