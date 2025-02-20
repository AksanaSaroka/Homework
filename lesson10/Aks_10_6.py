"""
Написать генератор triangular_numbers, который возвращает подряд 
треугольные числа

Формула:
Tn = 1 / 2 * n * (n + 1)

Например:
tn_gen = triangular_numbers()

next(tn_gen) -> 1
next(tn_gen) -> 3
next(tn_gen) -> 6
next(tn_gen) -> 10
next(tn_gen) -> 15
next(tn_gen) -> 21
"""

def triangular_numbers(n:int):
    for i in range(1,n+1):
        Tn = 1/2*i*(i+1)
        yield Tn

tn_gen = triangular_numbers(7)
for i in tn_gen:
    print(i)