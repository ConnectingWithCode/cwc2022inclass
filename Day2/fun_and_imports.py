import math
import random

def imports():
    print("----- Imports -----")
    print(math.pi)
    print(math.sqrt(25))
    print(math.pow(7, 2))
    print(math.cos(math.pi * 0.5))

    print(random.randint(3, 9))
    print(random.randint(3, 9))
    print(random.randint(3, 9))
    print(random.randint(3, 9))
    print(random.randint(3, 9))

    print(random.random())
    print(random.random())
    print(random.random())
    print(random.random())


def fun(a, b, c):
    print("----- Functions -----")
    print(a, b, c)
    # return (a + b) * c
    return (a + a) * b + c


ans = fun(2, 3, 10)
print(ans)   # Guess --> 22

ans = fun(5, 2, 3)
print(ans)   # Guess --> 23

ans = fun(1, 99, 6)
print(ans)   # Guess --> 204

imports()
