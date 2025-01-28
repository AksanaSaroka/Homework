'''
Пользователь вводит 3 числа, 
найти среднее арифметическое с точность 3 знака после запятой

'''

number1 = float(input('Введите 1-ое число - '))
number2 = float(input('Введите 2-ое число - '))
number3 = float(input('Введите 3-ее число - '))

sr_arifm = round(((number1+number2+number3)/3),3)

print(sr_arifm)