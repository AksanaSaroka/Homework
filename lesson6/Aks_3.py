'''
Запросить 3 числа. Вывести наибольшее  из них. Решить используя if.
'''

spisok = input('Введите три числа через пробел').split()
s = list(map(float, spisok))

if s[0] > s[1] and s[0] > s[2]:
    print(s[0])
elif s[1] > s[0] and s[1] > s[2]:
    print(s[1])
else:
    print(s[2])