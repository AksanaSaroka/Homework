'''
Запросить количество секунд. 
Вывести на экран время в формате ЧЧ:ММ:СС равное эти секундам.
Пример: 35457 -> 09:50:57
Сделать 2 варианта с форматной строкой и без.
'''


number_of_seconds = int(input('Введите количество секунд: '))

hh = str("{:02}".format(number_of_seconds//3600))
mm = str("{:02}".format((number_of_seconds % 3600)//60))
ss = str("{:02}".format(number_of_seconds%60))

print(hh, mm, ss, sep=':')
print(f"{hh}:{mm}:{ss}")