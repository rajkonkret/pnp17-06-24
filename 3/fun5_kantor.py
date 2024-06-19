# stworzyc funkcję kantor
# ma posiadać dwie funkcje wewnętrzne usd, eur
# w zależności od parametru mamy otrzymawac właściwą funkcję
# możliwość przekazania dowolnej kwoty
def kantor(waluta):
    print("Otwieram kantor")

    def usd(kwota=0):
        print(f"Wymieniam {kwota} usd na {kwota * 4.02} pln")

    def eur(kwota=0):
        print(f"Wymieniam {kwota} eur na {kwota * 4.33} pln")

    if waluta == 'eur':
        return eur  # zwracam adres
    else:
        return usd


kantor_usd = kantor("usd")
kantor_usd(1000)

kantor_eur = kantor('eur')
kantor_eur(5000)
# Otwieram kantor
# Wymieniam 1000 usd na 4019.9999999999995 pln
# Otwieram kantor
# Wymieniam 5000 eur na 21650.0 pln
