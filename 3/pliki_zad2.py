import chardet

# pip install chardet


with open('test.log', 'rb') as f:  # rb - odczytuje bajtowo
    lines = f.read()

print(lines)
# b'Nadpisane\r\nDodane\r\nDodane\r\nDodane\r\nDodane\r\nDo\xc5\x9bdane\r\n'
result = chardet.detect(lines)
print(result)  # {'encoding': 'Windows-1254', 'confidence': 0.6586696861310511, 'language': 'Turkish'}
# po dodaniu większej liczby polskich znaków w pliku
# {'encoding': 'utf-8', 'confidence': 0.99, 'language': ''}
print(type(result))  # <class 'dict'>
encoding = result['encoding']
print(encoding)  # utf-8
print(lines.decode(encoding=encoding))
