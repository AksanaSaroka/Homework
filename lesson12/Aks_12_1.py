"""
Создать класс Phone, у которого будут следующие атрибуты:

Определить атрибуты:

- brand - бренд
- model - модель
- issue_year - год выпуска

Определить методы:

- инициализатор __init__
- receive_call, который принимает имя звонящего и выводит на экран: 
        <Бренд-Модель> - Звонит {name}
- get_info, который будет возвращать кортеж (brand, model, issue_year)
- метод __str__, который выводит на экран информацию об устройстве:
Бренд: {}
Модель: {}
Год выпуска: {}
"""

class Phone:
        name = ' '
    
        def __init__(self, brand, model, issue_year):
                self.brand = brand
                self.model = model
                self.issue_year = issue_year


        def receive_call(self,name): 
                """ receive_call
                :param name:    name of the person calling 
                """
                print(f" <{self.brand}-{self.model}> - Звонит {name}") 

        def     get_info(self):
                """ get_info
                :return:   tuple (brand, model, issue_year)
                """
                return  f"{(self.brand, self.model, self.issue_year)}"
        
        def  __str__(self):
                """ __str__
                Метод, который выводит на экран информацию об устройстве.
                """
                print(f" Бренд: {self.brand} \n Модель: {self.model} \n Год выпуска: {self.issue_year}")



p = Phone('Nokia',3200,2000)
p.receive_call("Mr Smit")
print(p.get_info())
p.__str__()
        
        