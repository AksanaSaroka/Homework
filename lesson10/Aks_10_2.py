
"""
Написать генератор factorial, который возвращает подряд значения факториала

Например:

factorial_gen = factorial()

next(factorial_gen) -> 1
next(factorial_gen) -> 2
next(factorial_gen) -> 6
next(factorial_gen) -> 24
"""

def factorial(a):
    if a > 1:
        return (factorial(a-1)*a)
    elif 0 <= a <= 1:
        return 1
    else:
        return 'err: факториал не может быть отрицательным числом '

def factorial_gen(n):
    for i in range(1,n+1):
       yield factorial(i)

b = factorial_gen(5)
for i in b:
    print(i)

print(type(b))




# def factorial_gen(a:int):
    
#     f = 1
#     for i in range(1, a+1):
#         f *= i
#         yield f


# b = factorial_gen(6)
# for i in b:
#     print(i, end='\n')

# print(type(b))