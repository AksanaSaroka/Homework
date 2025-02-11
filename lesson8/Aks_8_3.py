'''
Написать функцию, которая вычисляет  факториал переданного в нее числа без рекурсии.

'''
a = 5

def factorial(a:int):
    i = 1
    f = 1
    for i in range(1, a+1):
        f *= i
        i += 1
    return f

print(factorial(a))