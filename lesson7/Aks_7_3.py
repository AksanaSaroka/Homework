'''
Запросить любое число. Заменить каждую цифру этого числа буквой, 
у которой номер в алфавите равен этой цифре. 
Например: 1352=aceb.
'''
alf = "abcdefghijklmnopqrstuvwxyz"

number = input('Введите число: ')

for s in number:
     number = number.replace(s, alf[int(s)-1])
         
             
print(number)




