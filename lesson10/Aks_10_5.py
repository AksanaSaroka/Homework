"""
Написать функцию счетчик которая с помощью замыкания (без глобальных переменных)
будет хранить в себе количество запусков и каждый раз возвращать число на 1 больше.
Функция должна принимать число с которого начинается отсчет.

Пример:
с1 = counter(1)
с10 = counter(10)

print(c1()) -> 2
print(c1()) -> 3
print(c1()) -> 4 

print(c10()) -> 11 
print(c10()) -> 12 
print(c10()) -> 13 

"""

def f_counter(n):
    count = n

    def wrapper(*args,**kwargs):
        nonlocal count
        count += 1
        return count
    
    return wrapper

c1 = f_counter(1)
print(c1())
print(c1())
print(c1())
print(c1())
print(c1())
print(c1())

c10 = f_counter(10)
print(c10())
print(c10())
print(c10())
