'''
Дан список:
[1, 1, 2, 3, 21, 8, 13, 21, 34, 55, 89]
вывести на экран:
    - минимальное значение
    - максимальное значение
    - сумму всех элементов
    - список только элементов с нечетным индексом
'''

a = [1, 1, 2, 3, 21, 8, 13, 21, 34, 55, 89]

a_min = min(a)
a_max = max(a)
s = sum(a)
b = a[1::2]
print('Минимальное значение: ', a_min)
print('Максимальное значение: ', a_max)
print('Сумма всех элементов: ', s)
print('Список элементов с нечетными индексами: ', b)
