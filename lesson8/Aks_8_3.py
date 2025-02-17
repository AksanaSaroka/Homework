'''
Написать функцию, которая вычисляет  факториал переданного в нее числа без рекурсии.

'''
a = 5

def factorial(a:int):
    
    f = 1
    for i in range(1, a+1):
        f *= i
        return f

print(factorial(a))