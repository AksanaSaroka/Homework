'''
Запросить высоту елочки - число от 3 до 20. 
Напечатать на экране елочку где ее высота равна числу строк. 
Пример елочки из 4 строк:
   *
  ***
 *****
*******

'''

height = int(input('Введите высоту ёлочки(от 3 до 20): '))

s = ''

for i in range(1, height + 1):
      # print((' '*(height-i)) + ((2*i-1)*'*'))
      print((' '*(height-i)) + s.center((2*i-1),'*'))
