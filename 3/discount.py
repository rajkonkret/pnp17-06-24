from datetime import date, datetime, timedelta

today = date.today()
print(today)  # 2024-06-19

time = datetime.now()
print("Aktualny czas:", time)  # Aktualny czas: 2024-06-19 11:49:35.698482
print(type(time))  # <class 'datetime.datetime'>

# tomorrow = today + 1  # TypeError: unsupported operand type(s) for +: 'datetime.date' and 'int'
# days=0, seconds=0, microseconds=0,
#                 milliseconds=0, minutes=0, hours=0, weeks=0
tomorrow = today + timedelta(days=1)
print(f"Jutro będzie {tomorrow}")  # Jutro będzie 2024-06-20

print(time.time())
print(today.day)
# 11:54:42.059192
# 19
formatted_date = datetime.now().strftime("%d/%m/%Y")
print("Sformatowana data", formatted_date)  # Sformatowana data 19/06/2024

formatted_time = datetime.now().strftime('%H:%M')
print("Czas", formatted_time)  # Czas 11:57

# zadanie domowe - wyswietlic czas w formacie 12h

# zamiana stringa na obiekt typu datetime
date_object = datetime.strptime("19/06/2024", '%d/%m/%Y')
print(date_object)  # 2024-06-19 00:00:00
print(type(date_object))  # <class 'datetime.datetime'>

products = [
    {'sku': 1, 'exp_date': today, 'price': 100.0},
    {'sku': 2, 'exp_date': today, 'price': 200.0},
    {'sku': 3, 'exp_date': tomorrow, 'price': 500},
    {'sku': 4, 'exp_date': today, 'price': 24.80},
]

# print(products)
for p in products:
    # print(p)  # {'sku': 4, 'exp_date': datetime.date(2024, 6, 19), 'price': 24.8}
    # print(p['price'])
    if p['exp_date'] != today:
        continue
    p['price'] *= 0.8  # price = price * 0.8
    print(f"""
Price for sku {p['sku']}
is now {p['price']}""")
# Price for sku 1
# is now 80.0
#
# Price for sku 2
# is now 160.0
#
# Price for sku 4
# is now 19.840000000000003
