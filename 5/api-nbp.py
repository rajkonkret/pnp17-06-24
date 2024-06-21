# HTTP GET
import requests

url = 'http://api.nbp.pl/api/exchangerates/rates/A/EUR/'
response = requests.get(url)
print(response)  # <Response [200]>
# 2xx ok
# 3xx przekierowanie
# 4xx 404 - błedny adres, 400 Bad Request - złe parametry w zapytaniu
# 5XX  - błedy po tronie serwera 500 Internal Server Error
print(response.text)  # odczytanie jsona
# {"table":"A","currency":"euro","code":"EUR","rates":[{"no":"119/A/NBP/2024","effectiveDate":"2024-06-20","mid":4.3238}]}
response_data = response.json()
print(response_data)
# print(type(response_data))
# {'table': 'A', 'currency': 'euro', 'code': 'EUR',
#  'rates': [{'no': '119/A/NBP/2024', 'effectiveDate': '2024-06-20', 'mid': 4.3238}]}
# currency, effectiveDate, mid
print(response_data['currency'])  # euro
print(response_data['rates'])
# [{'no': '119/A/NBP/2024', 'effectiveDate': '2024-06-20', 'mid': 4.3238}]
print(response_data['rates'][0])
# {'no': '119/A/NBP/2024', 'effectiveDate': '2024-06-20', 'mid': 4.3238}
print(response_data['rates'][0]['effectiveDate'])  # 2024-06-20
print(response_data['rates'][0]['mid'])  # 4.3238
