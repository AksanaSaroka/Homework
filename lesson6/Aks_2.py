'''
запросить у пользователя логин пароль и возраст
вывести доступ разрешен:
    логин:admin   пароль:123456    возраст: любой    
    логин:vasya   пароль: vas123   возраст: менее 60
    логин:guest   пароль: любой    возраст:более 18
    
в остальных случаях - "доступ запрещен".

'''
login = input('Введите Ваш логин: ')
password = input('Введите Ваш пароль: ')
age = int(input('Введите Ваш возраст: '))

if login == 'admin' and password == '123456' and age:
    print('Доступ разрешен')
elif  login == 'vasya' and password == 'vas123' and age <= 60:
    print('Доступ разрешен')  
elif  login == 'guest' and password and age >= 18:
    print('Доступ разрешен') 
else:
    print('Доступ запрещен')    