import requests
import json

url = 'https://randomuser.me/api/'

response = requests.get(url)
print(response)  # <Response [200]>
# 2xx ok
# 3xx przekierowanie
# 4xx 404 - błedny adres, 400 Bad Request - złe parametry w zapytaniu
# 5XX  - błedy po tronie serwera 500 Internal Server Error
print(response.text)  # odczytanie jsona
response_data = response.json()
print(response_data)
user = response_data['results'][0]
print(user)
print(type(user))  # <class 'dict'>
# {'gender': 'male', 'name': {'title': 'Mr', 'first': 'Aaron', 'last': 'West'},
#  'location': {'street': {'number': 6005, 'name': 'Taylor St'}, 'city': 'St. Petersburg', 'state': 'Michigan',
#               'country': 'United States', 'postcode': 59206,
#               'coordinates': {'latitude': '88.1660', 'longitude': '-98.2255'},
#               'timezone': {'offset': '-4:00', 'description': 'Atlantic Time (Canada), Caracas, La Paz'}},
#  'email': 'aaron.west@example.com',
#  'login': {'uuid': '0f49dd68-0b8c-4d20-8d1c-dd89d8831207', 'username': 'bigpeacock845', 'password': 'stephani',
#            'salt': 'aSIW1kbW', 'md5': '188a1fe12ecf2bb27ce1ffbc02fa7df7',
#            'sha1': '64d34cba72c856f92342391c2bd6a3518226dceb',
#            'sha256': 'e65e1d7cea133f8495cd9f310c761b96284a3a8faba2f58462cc6ef4b084aac6'},
#  'dob': {'date': '1992-02-19T03:06:16.627Z', 'age': 32},
#  'registered': {'date': '2013-04-28T00:36:14.864Z', 'age': 11},
#  'phone': '(855) 301-0461', 'cell': '(549) 504-0944', 'id': {'name': 'SSN', 'value': '531-66-7335'},
#  'picture': {'large': 'https://randomuser.me/api/portraits/men/61.jpg',
#              'medium': 'https://randomuser.me/api/portraits/med/men/61.jpg',
#              'thumbnail': 'https://randomuser.me/api/portraits/thumb/men/61.jpg'}, 'nat': 'US'}
with open('random_user_data.json', 'w') as f:
    json.dump(user, f, indent=4)

print("Imię: ", user['name']['first'])
print("Nazwisko: ", user['name']['last'])
print(user['picture'])
# {'large': 'https://randomuser.me/api/portraits/women/80.jpg',
#  'medium': 'https://randomuser.me/api/portraits/med/women/80.jpg',
#  'thumbnail': 'https://randomuser.me/api/portraits/thumb/women/80.jpg'}
photo_url = user['picture']['large']
print(photo_url)
response_photo = requests.get(photo_url)
with open('user_photo.jpg', 'wb') as f:
    f.write(response_photo.content)
print("Zdjęcie zostało zapisane")
