'''
Запросить у пользователя число
    - если число менее 20 -  вывести на экран сколько чисел 
        в диапазоне от 0 до этого числа делится без остатка на 7. 
    - если более 20 - вывести на экран сколько чисел 
        в диапазоне от 0 до этого числа делится без остатка на 11.
'''

number = int(input('Введите число: '))

s = list(range(0,(number+1))) # список чисел в диапазоне [0,number+1]
# print(s)

n7 = 0
n7 = sum(map(lambda item: item % 7 == 0, s)) # сколько чисел делится без остатка на 7

n11 = 0
n11 = sum(map(lambda item: item % 11 == 0, s)) # сколько чисел делится без остатка на 11


if number <= 20:
    print('количество чисел,которые делятcя без остатка на 7: ',n7)
else:
    print('количество чисел,которые делятcя без остатка на 11: ',n11)