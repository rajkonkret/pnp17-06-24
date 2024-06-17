tekst = "Witaj świecie"
print(tekst)  # Witaj świecie
print(type(tekst))  # <class 'str'>

# teksty są niemutowalne
tekst2 = tekst.upper()
print(tekst)  # Witaj świecie
print(tekst2)
print(tekst.upper())
# WITAJ ŚWIECIE
# WITAJ ŚWIECIE
print(tekst2)  # WITAJ ŚWIECIE

print(tekst.lower())  # witaj świecie

print(tekst)  # Witaj świecie

print(tekst.removesuffix('świecie'))  # "Witaj "
print(tekst.removeprefix('Witaj'))  # " świecie"
print(tekst)  # Witaj świecie 0123456789

print(tekst.count("i"))  # 3
print(tekst.count("j", 0, 4))  # 0 -> 0123 zbiór z prawej strony otwarty
print(tekst.count("i", 0, 4))  # 1 -> 0123
# Witaj
# 01234
print(tekst[3])  # "a" - czwarty element - indeks 3

encoded_s = tekst.encode('utf-8')
print(encoded_s)  # b'Witaj \xc5\x9bwiecie'
print(type(encoded_s))  # <class 'bytes'>
# \xc5 zapis szesnastkowy, dziesietnie 197
print(encoded_s.decode('utf-8'))  # Witaj świecie

imie = "Radek"
tekst_format = f"Mam na imię {imie} i lubię Pythona"
print(tekst_format)  # Mam na imię Radek i lubię Pythona
# f - f-string, tekst sformatowany

tekst_format_2 = f"\tMam na imię {imie}\n i lubię Pythona.\b"
print(tekst_format_2)
# "	Mam na imię Radek
#  i lubię Pythona"
# \t - tabulator
# \n - nowa linia
# \b - backspace

starszy = "Witaj %s!"
print(starszy % imie)  # Witaj Radek!

print("""   Teskt
wielolinijkowy""")
# "   Teskt
# wielolinijkowy"
