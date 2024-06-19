import json

# json = {"name" : "Radek"}
# obiekt typu para klucz-wartosc
# odpowiednikiem jsona w python jest słownik

person_dict = {'name': 'Radek', 'age': 40, 'czy_pali': None}
# json - {"name": "Radek", "age": 40, "czy_pali": null}
print(type(person_dict))  # <class 'dict'>

with open('nasza_dane.json', 'w') as f:
    json.dump(person_dict, f)

# upiekszanie
with open('nasza_dane.json', 'w') as f:
    json.dump(person_dict, f, indent=4)
# {
#     "name": "Radek",
#     "age": 40,
#     "czy_pali": null
# }

# posortowanie po kluczu
with open('nasza_dane.json', 'w') as f:
    json.dump(person_dict, f, indent=4, sort_keys=True)
# {
#     "age": 40,
#     "czy_pali": null,
#     "name": "Radek"
# }

with open('nasza_dane.json', 'r') as fh:
    data = json.load(fh)

print(data)  # {'age': 40, 'czy_pali': None, 'name': 'Radek'}
print(type(data))  # <class 'dict'>

print(data['name'])
print(data.get('name'))  # Radek

json_text = json.dumps(data)
print(json_text)  # {"age": 40, "czy_pali": null, "name": "Radek"}
print(type(json_text))  # <class 'str'>

dict_json = json.loads(json_text)
print(dict_json)  # {'age': 40, 'czy_pali': None, 'name': 'Radek'}
print(type(dict_json))  # <class 'dict'>
