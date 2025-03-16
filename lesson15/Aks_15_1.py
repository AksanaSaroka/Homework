"""
Используя класс из пред.урока обеспечить хранение и сохранение любых изменений в базе 
данных. Для этого можно к примеру добавить в класс метод save который будет сохранять или 
создавать пользователя в базе данных и использовать его при любых изменениях.


* в базе данных создать таблицу предоставляемых услуг со след полями
	название
	тип (1 - платная 0 - бесплатная)
	стоимость 
	период в днях
** в класс пользователя добавить методы:
	добавить услугу (услуг у одного пользователя может быть несколько)
	продлить услугу (продлить можно если услуга еще не закончена, иначе добавить)
	удалить услугу
*** создать консольное или оконное приложение которое показывает меню и отрабатывает выбранный пункт.
	Меню:
		1 - показать пользователей
		2 - информация о пользователе (в т.ч. и подключенные услуги)
		3 - список услуг		
		4 - показать пользователей с определенной услугой
		5 - показать пользователей у которых за прошедший месяц окончился период хоть одной услуги 
 	 
"""

import re
from datetime import datetime as dt
from datetime import timedelta
import random
import string
import sqlite3

con = sqlite3.connect('lesson15\\test_Aks_1.db')
cur = con.cursor()


    
# Устанавливаем соединение с базой данных:
con = sqlite3.connect('lesson15\\test_Aks_1.db')
cur = con.cursor()


#создаем таблицу пердоставляемых услуг(services):
sql = """
CREATE TABLE IF NOT EXISTS services(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
	name TEXT,
 	type BOOLEAN,
	price REAL,
    period days INTEGER
);
"""
cur.execute(sql)

#создаем таблицу пользователей(users):
sql_u ="""
			CREATE TABLE IF NOT EXISTS users(
				id INTEGER PRIMARY KEY AUTOINCREMENT,
				name TEXT,
				login TEXT,
				password TEXT,
				is_blocked BOOLEAN,
                subscription_date INTEGER,
                subscription_mode INTEGER,
                service TEXT
			);
			""" 	
cur.execute(sql_u)

#cсохраняем изменение:
con.commit()



class User:
    
    def __init__(self, name:str, login:str, password:str = None) -> None:
        # свойства объектов
        global con, cur
        self.name = name
        self.login = login
        self.password = password if password else self.change_pass()
        self.is_blocked = False
        self.subscription_date = (dt.now().date() + timedelta(days=30)).strftime("%d/%m/%Y") # дата, до которой действует подписка
        self.subscription_mode = 'free' # вид подписки (free, paid)
		# self.save_user()
        
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if not re.search(r'[а-яА-Я]', value):
            raise ValueError('Некорректное имя(name). Необходимо использовать только буквы русского алфавита')
        self.__name = value 
     
    @property
    def login(self):
        return self.__login
    
    @login.setter
    def login(self,value):
        pattern = r'^[a-zA-Z0-9-_]{6,}$'
        if not re.search(pattern, value): 
            raise ValueError(f"""Некорректный login. Необходимо использовать только латинские буквы, 
                             цифры и черту подчеркивания.Длина не менее 6 символов""")
        self.__login = value
        
    @property
    def password(self):
        return self.__password
   
    @password.setter
    def password(self,value):
        if self.__check_pass(value): 
            self.__password = value
        else:
            raise ValueError(f""""Некорректный пароль. Необходимо использовать только латинские буквы, 
                             цифры. Длина пароля менее 6 символов, необходимы 
                             хотя бы одна строчная буква, одна заглавная буква и цифра.""")

    def __str__(self):
        return f"{self.name}, {self.login}, {self.password}"
    
    def __repr__(self):
        return f"{self.name}, {self.login}, {self.password}"
    
    def bloc(self, flag):
        if flag:
            return self.is_blocked == True	
    
    def check_subscr(self,check_date=None):
        if not check_date:
            check_date = (dt.now().date()).strftime("%d/%m/%Y")
        d1 = dt.strptime(check_date, "%d/%m/%Y")
        d2 = dt.strptime(self.subscription_date, "%d/%m/%Y")
        
        if d1 < d2:
            self.bloc(flag=False)
            print(f"""Ваша подписка действует {d2 - d1}.
            Вид подписки:{self.subscription_mode}""")
        else:
            self.bloc(flag=True)
            self.change_subscription() 
            print(f"""Срок действия подписки истек. Вы заблокированы.
                Вид подписки:{self.subscription_mode}.
                Необходимо оплатить подписку""")
       
    def __check_pass(self,password):
        pattern_pass = r'^(?=.*[0-9].*)(?=.*[a-z].*)(?=.*[A-Z].*)[0-9a-zA-Z]{,6}$'
        if re.search(pattern_pass, password): 
            return password 
 
    def generate_password(self,length=6):        
        pattern_gen = string.ascii_lowercase + string.ascii_uppercase + string.digits
        while True:
            new_password = ''

            for i in range(length):
                new_password += new_password.join(random.choice(pattern_gen))

            if (any(symbol in string.ascii_lowercase for symbol in new_password) and
                any(symbol in string.ascii_uppercase for symbol in new_password) and
                any(symbol in string.digits for symbol in new_password)):
                break
        return new_password
    
    def change_pass(self):
            password = self.generate_password()
            return password 
    
    def change_subscription(self):
        self.subscription_mode = 'paid' 
        return self.subscription_mode
    
    def get_info(self):
        if not self.is_blocked:
            return  f"Имя - {self.name}\n"\
                    f"Логин - {self.login}\n"\
                    f"Пароль - {self.password}\n"\
                    f"Вид подписки - {self.subscription_mode}\n"\
                    f"Подписка до - {self.subscription_date}\n"\
                    
        else:
            return f"Срок действия подписки истек. Вы заблокированы"

    def print_info(self):
        print(self.get_info() + '\n') 
       
	# def save_user(self):
    #     global con, cur
    #     sql1 = f"""
    #     	INSERT INTO user
    #           (name, login, password, is_blocked, subscription_date, subscription_mode, service) 
    #         VALUES ('{self.name}','{self.login}','{self.password}','{self.is_blocked}','{self.subscription_date}',\
    #             		'{self.subscription_mode}','{self.service}')
	# 	"""    
	# 	cur.execute(sql1)
    #     con.commit()   




   
user_1 = User('Коля','uuuew99988mm')
# user_1.check_subscr()
user_1.check_subscr('18/3/2025')
user_1.print_info()


con.close()

