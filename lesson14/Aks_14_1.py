"""
Создать класс User с атрибутами:

Свойства:
	- name - имя - содержит только буквы русского алфавита 
	- login - логин - может содержать  только латинские буквы цифры и черту подчеркивания быть не менее 6 символов
	- password - пароль - может содержать  только латинские буквы цифры. Обязательные условия: 
                содержит менее шести символов
                содержит строчную букву
                содержит заглавную букву
                содержит число
	- is_blocked - заблокирован
	- subscription_date - дата до какой действует подписка
	- subscription_mode - вид подписки (free, paid)


Методы:
	- bloc - принимает логическое значение и помечает пользователя заблокированным 
	- check_subscr - может принимать аргумент в виде даты. Проверяет действует ли подписка на определенную дату. 
						Если дата не передана значит на дату проверки. 
						Возвращает  действует ли подписка, ее вид и сколько осталось дней.
	- change_pass - смена пароля и присваивание его в качестве действующего. 
						Пароль должен пройти валидацию. 
						Если пароль не был передан сгенерировать по правилам и вывести в консоль.
	- get_info - выводит информацию о пользователе если заблокирован то сообщает об этом.



Создание объекта должно происходить  при передаче обязательных аргументов имя и логин и необязательного - пароль. Логин и пароль должны быть проверен на валидность.
Если пароль в конструктор не был передан он должен сгенерироваться на основании правил, и должен быть выведен на экран(консоль).
При создании пользователя ему предоставляется пробная подписка сроком на 30 дней.
При изменении даты подписки  вид подписки меняется на платный.
Валидацию данных сделать через регулярные выражения
"""
import re
from datetime import datetime as dt
from datetime import timedelta
import random
import string

class User:
    
    def __init__(self, name:str, login:str, password:str = None) -> None:
        # свойства объектов
        self.name = name
        self.login = login
        self.password = password if password else self.change_pass()
        self.is_blocked = False
        self.subscription_date = (dt.now().date() + timedelta(days=30)).strftime("%d/%m/%Y") # дата, до которой действует подписка
        self.subscription_mode = 'free' # вид подписки (free, paid)


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


   
user_1 = User('Коля','uuuew99988mm')
# user_1.check_subscr()
user_1.check_subscr('18/3/2025')
user_1.print_info()

