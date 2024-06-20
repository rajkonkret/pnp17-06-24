def allparams(a, b, /, c=42, d=256):
    print("a, b", a, b)
    print("c, d", c, d)


allparams(1, 2)  # pozycyjne 1,2
# / oddziela argumenty pozycyjne od nazwanych
# te z lewej strony muszą być wtedy przekazywane tylko po pozycji
# allparams(b=9, a=8)  # TypeError: allparams() got some positional-only arguments passed as keyword arguments: 'a, b'
allparams(1, 2, c=8)  # c, d 8 256
allparams(1, 2, 3, 4)


# a, b 1 2
# c, d 3 4


def allparams_2(a, b, /, c=42, *args, d=256, **kwargs):
    print("a, b", a, b)
    print("c, d", c, d)
    print('args', args)
    print('kwargs', kwargs)


# ile minimum?
allparams_2(1, 2)
# jak przekazac cokolwiek do c?
allparams_2(1, 2, c=9)
allparams_2(1, 2, 3)  # c, d 3 256
# gdzie trafi czwarty argument po pozycji?
allparams_2(1, 2, 3, 4)  # args (4,)
# a kolejnr? kiedy zakonczy argsy?
allparams_2(1, 2, 3, 4, 5, 6, 7, 8, 9, 0)  # args (4, 5, 6, 7, 8, 9, 0)
# jak przekazac d? d musi byc po nazwie d=9
allparams_2(1, 2, d=9)
allparams_2(1, 2, 3, 4, 5, 6, d=9)  # c, d 3 9
# jak przekazac do kwargsów
allparams_2(1, 2, 3, 4, 5, 6, d=9, e=9, name="Radek")
# kwargs {'e': 9, 'name': 'Radek'}
# gdzie trafi a=7
allparams_2(1, 2, 3, 4, d=9, e=9, name="radek", a=7)
# do kwargsow kwargs {'e': 9, 'name': 'radek', 'a': 7}
