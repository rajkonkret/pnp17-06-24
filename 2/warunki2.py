# od Pythona 3.10
# match case

lista = []
lang = input('Podaj znany Ci język programowania')

match lang.lower().replace(" ", ""):
    case "python":
        lista.append("Python")
    case "java":
        lista.append("Java")
    case _:  # wartośc domyslna, else
        print("Nie znam takiego języka programowania")

print(lista)
