'''
Дан произвольный список из 5 элементов. 
     - Поменять местами 1ый и последний элемент
     - удалить и вывести на печать третий элемент
'''


a = [1, 5, 'hh', 6, 10]
a[0], a[-1] = a[-1], a[0]
print(a)

print(a.pop(2))
