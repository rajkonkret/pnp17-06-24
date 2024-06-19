# funkcja wewnętrzna, zagnieżdzona
# dekortory wykorzystują zasadę funkcji wewnętrznej
def fun1():
    print("To jest fun1")

    def fun2():
        print("To jest fun2")

    return fun2  # zwraca adres funkcji fun2


print(fun1)  # <function fun1 at 0x000001F7A8068B80>
fun1()  # To jest fun1
xFun = fun1()
print(xFun)  # <function fun1.<locals>.fun2 at 0x0000023110D19E40>
xFun()  # To jest fun2
