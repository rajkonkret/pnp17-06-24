import random

# generowanie liczb pseudolosowych

print(random.randint(1, 100))  # int 1..100
print(random.randrange(1, 100))  # int 1..99
print(random.randrange(7))  # 0..6
print(random.random())  # float 0.6572961984462559 0 do 0.999999
print(random.random() * 10)  # 4.23472746698944 od 0 do 9.999999

lista = [6, 12, 34, 56, 67, 89, 120]
print(random.choice(lista))
print(random.choice(lista))
print(random.choice(lista))
print(random.choice(lista))
print(random.choice(lista))
print(random.choice(lista))

lista_kule = list(range(1, 50))  # range() od 1 do 49
# print(lista_kule)
print("-------")
# wyn = random.choice(lista_kule)
# lista_kule.remove(wyn)
# print(wyn)
# wyn = random.choice(lista_kule)
# lista_kule.remove(wyn)
# print(wyn)
# wyn = random.choice(lista_kule)
# lista_kule.remove(wyn)
# print(wyn)
# wyn = random.choice(lista_kule)
# lista_kule.remove(wyn)
# print(wyn)
# wyn = random.choice(lista_kule)
# lista_kule.remove(wyn)
# print(wyn)
# wyn = random.choice(lista_kule)
# lista_kule.remove(wyn)
# print(wyn)
print(random.choices(lista_kule, k=6))  # [30, 34, 19, 34, 6, 34] z powtórzeniami
print(random.sample(lista_kule, 6))
print(random.sample(lista_kule, k=6))
# [16, 14, 1, 45, 43, 6]
# [32, 23, 44, 28, 8, 40]
