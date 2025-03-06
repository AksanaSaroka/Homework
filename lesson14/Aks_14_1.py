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
import datetime

class User:
    def __init__(self, name, login, password='', is_blocked=False, subscription_date='', subscription_mode='free' ) -> None:
        # свойства объектов
        self.name = name
        self.login = login
        self.password = password
        self.is_blocked = is_blocked
        self.subscription_date = subscription_date
        self.subscription_mode = subscription_mode

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
        pattern_pass = r'^(?=.*[0-9].*)(?=.*[a-z].*)(?=.*[A-Z].*)[0-9a-zA-Z]{,6}$'
        if not re.search(pattern_pass, value): 
            raise ValueError(f""""Некорректный пароль. Необходимо использовать только латинские буквы, 
                             цифры. Длина пароля менее 6 символов, необходимы 
                             хотя бы одна строчная буква, одна заглавная буква и цифра.""")
        else:
            self.__login = value

    def __str__(self):
        return f"{self.name}, {self.login}, {self.password}"
    
    def __repr__(self):
        return f"{self.name}, {self.login}, {self.password}"
    
    def bloc(self):
        is_blocked = False
        if a:
            return is_blocked == True	
    
    def check_subscr(self,check_date=datetime.now().date()):

        if start_date <= check_date <= self.subscription_date:
            return f"""Ваша подписка действует {self.subscription_date - check_date} дней.
            Вид подписки:{self.subscription_mode}"""
    # def change_pass(self):
    #         pass
    
	# def get_info(self):
    #         pass   

user_1 = User('Коля','uuuew99988mm','aBcck9')
