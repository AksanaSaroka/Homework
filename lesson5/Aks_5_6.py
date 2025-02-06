'''
Запросить 3 раза строку из нескольких чисел через пробел
    - вывести все уникальные числа по возрастанию
    - вывести числа которые есть в каждой строке
    -* вывести числа которые есть только в одной из трех строк
    
    выполнить без циклов и условий
    
    пример:
    >>> 1 2 11 22
    >>> 1 2 22 33
    >>> 1 2 33 44


    1) 1 2 11 22 33 44
    2) 1 2
    3) 11 44
    
'''
spisok1 = set(input('Введите числа через пробел: ').split())
spisok2 = set(input('Введите числа через пробел: ').split())
spisok3 = set(input('Введите числа через пробел: ').split())

a = spisok1 | spisok2 | spisok3
print(sorted(list(map(int,a))))

b = spisok1 & spisok2 & spisok3
print(sorted(list(map(int,b))))

d = (spisok1 - spisok2 - spisok3) | (spisok2 - spisok1 - spisok3) | (spisok3 - spisok1 - spisok2)
print(sorted(list(map(int,d))))