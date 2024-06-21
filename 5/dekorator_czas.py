import time
import numpy as np


def measure(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"CZas wykonania funkcji {func.__name__}: {execution_time}")
        return result

    return wrapper


@measure
def my_wait():
    time.sleep(2)


my_wait()


@measure
def my_for_sum():
    suma = 0
    for i in range(15_000_000):
        suma += i
    print("Sum is:", suma)


@measure
def my_sum_without_for():
    total = sum(range(15_000_000))
    print("Sum is:", total)


my_for_sum()
my_sum_without_for()


@measure
def my_sum_np():
    total = np.sum(np.arange(15_000_000), dtype=np.int64)
    print("Sum is:", total)


my_sum_np()
# CZas wykonania funkcji my_wait: 2.0007569789886475
# Sum is: 112499992500000
# CZas wykonania funkcji my_for_sum: 0.6840755939483643
# Sum is: 112499992500000
# CZas wykonania funkcji my_sum_without_for: 0.6248624324798584
# Sum is: 112499992500000
# CZas wykonania funkcji my_sum_np: 0.059992074966430664
# GraalVM
