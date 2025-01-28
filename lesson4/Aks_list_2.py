'''
Запросить по очереди у пользователя 5 имен. Добавить все в список. 
Отсортировать. 
Вывести на экран.
Вывести True при наличии в списке имени 'Вася'
'''

users = []

user_name1 = input('Введите 1-ое имя - ')
user_name2 = input('Введите 2-ое имя - ')
user_name3 = input('Введите 3-ее имя - ')
user_name4 = input('Введите 4-ое имя - ')
user_name5 = input('Введите 5-ое имя - ')

users = [user_name1, user_name2, user_name3, user_name4, user_name5]
users.sort()

print(users)

ok = 'Вася' in users

print(ok)

