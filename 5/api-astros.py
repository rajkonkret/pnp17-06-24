# REST API - sposób komunikacji między klientem a serwerem
# GET, POST, PUT/PATCH, DELETE - metody http
# GET - pobierz (json, xml)
# POST - zapisz, można wysłać tresc do serwera (json, xml)
# PUT, PATCH - update
# DELETE - usunięcie
# przeglądarka używa GET

import requests

# pip install requests

url = 'http://api.open-notify.org/astros.json'
response = requests.get(url)
print(response)  # <Response [200]>
# 2xx ok
# 3xx przekierowanie
# 4xx 404 - błedny adres, 400 Bad Request - złe parametry w zapytaniu
# 5XX  - błedy po tronie serwera 500 Internal Server Error
print(response.text)  # odczytanie jsona
response_data = response.json()
print(response_data)
print(type(response_data))  # <class 'dict'>
print(response_data['people'])
# [{'craft': 'ISS', 'name': 'Oleg Kononenko'}, {'craft': 'ISS', 'name': 'Nikolai Chub'},
#  {'craft': 'ISS', 'name': 'Tracy Caldwell Dyson'}, {'craft': 'ISS', 'name': 'Matthew Dominick'},
#  {'craft': 'ISS', 'name': 'Michael Barratt'}, {'craft': 'ISS', 'name': 'Jeanette Epps'},
#  {'craft': 'ISS', 'name': 'Alexander Grebenkin'}, {'craft': 'ISS', 'name': 'Butch Wilmore'},
#  {'craft': 'ISS', 'name': 'Sunita Williams'}, {'craft': 'Tiangong', 'name': 'Li Guangsu'},
#  {'craft': 'Tiangong', 'name': 'Li Cong'}, {'craft': 'Tiangong', 'name': 'Ye Guangfu'}]
print(response_data.keys())  # dict_keys(['people', 'number', 'message'])
for k, v in response_data.items():
    print(k, "=>", v)

print(response_data['people'])  # dostajemy listę
for i in response_data['people']:
    print(i)
# {'craft': 'ISS', 'name': 'Oleg Kononenko'}
# {'craft': 'ISS', 'name': 'Nikolai Chub'}
# {'craft': 'ISS', 'name': 'Tracy Caldwell Dyson'}
# {'craft': 'ISS', 'name': 'Matthew Dominick'}
# {'craft': 'ISS', 'name': 'Michael Barratt'}
# {'craft': 'ISS', 'name': 'Jeanette Epps'}
# {'craft': 'ISS', 'name': 'Alexander Grebenkin'}
# {'craft': 'ISS', 'name': 'Butch Wilmore'}
# {'craft': 'ISS', 'name': 'Sunita Williams'}
# {'craft': 'Tiangong', 'name': 'Li Guangsu'}
# {'craft': 'Tiangong', 'name': 'Li Cong'}
# {'craft': 'Tiangong', 'name': 'Ye Guangfu'}

print(response_data['people'][1])  # {'craft': 'ISS', 'name': 'Nikolai Chub'}
print(response_data['people'][1]['name'])  # Nikolai Chub
