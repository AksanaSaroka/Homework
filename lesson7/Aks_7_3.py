'''
Запросить любое число. Заменить каждую цифру этого числа буквой, 
у которой номер в алфавите равен этой цифре. 
Например: 1352=aceb.
'''
alf = "abcdefghijklmnopqrstuvwxyz"

number = input('Введите число: ')

for a in number:
     number = number.replace(a, alf[int(a)-1])
         
             
print(number)




