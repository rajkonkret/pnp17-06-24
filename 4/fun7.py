def connect(**opcje):  # ** - argumenty słownikowe, przekazywane po nazwie
    print(opcje)  # {'a': 1}
    conect_param = {
        'host': '127.0.0.1',
        'port': '8080'
    }
    conect_param['pwd'] = opcje
    print(conect_param)  # {'host': '127.0.0.1', 'port': '8080', 'pwd': {'a': 1}}


# a=1 - para klucz-wartosc
connect(a=1)
connect(a=1, b=4, c=9, name="Radek")
# {'host': '127.0.0.1', 'port': '8080', 'pwd': {'a': 1, 'b': 4, 'c': 9, 'name': 'Radek'}}
d1 = {'host': '127.0.0.1', 'port': '8080', 'pwd': {'a': 1, 'b': 4, 'c': 9, 'name': 'Radek'}}
print(d1['pwd'])  # {'a': 1, 'b': 4, 'c': 9, 'name': 'Radek'}
print(d1['pwd']['name'])  # Radek


# przyjęło się w pythonie argumnty pozycyjne z * oznaczac jako *args
# argumentu słownikowe (nazwane) jako **kwargs
def all_args(*args, **kwargs):
    print(args, kwargs)


all_args()  # () {}
all_args(1, 2, 3)  # (1, 2, 3) {}
all_args(a=8, b=0)  # () {'a': 8, 'b': 0}
all_args(1, 2, c=9)  # (1, 2) {'c': 9}
# all_args(a=8,1,2)  # SyntaxError: positional argument follows keyword argument
