import random

class Hero:
    """     
    Класс дял создания героя 
    
     ...

    Attributes
    ----------
    name : str
        Имя героя
    health : int
        здоровье героя 
    age : int
        age of the person

    Methods
    -------
    print_info():
        Печатает в консоль информацию о герое
    
    kick():
        производит один удар - высчитывает и уменьшает броню и здоровье 
    
    """
    #  свойства класса - каждый созданный объект будет их иметь по умолчанию
    option1 = True
    points = 0
    level = 1

    # конструктор - тут мы создаем свойства которые должны быть у каждого нового объекта
    # и присылаем сюда первоначальные их значения
    def __init__(self, name, health, armor, strong) -> None:
        # свойства объектов
        self.name = name
        self.health = health
        self.armor = armor
        self.strong = strong
           
    # методы - это действия/команды которые могут выполнять объекты
    def _get_info(self):        
        return f"Имя {self.name}\n" \
               f"Здоровье - {self.health}\n" \
               f"Защита {self.armor}\n"\
               f"Сила {self.strong}"
        
    def print_info(self):
        print(self._get_info() + '\n')
    

    
class Spec_Attac:

    def __init__(self, unique_power, damage):
        self.unique_power = unique_power # уникальное свойство-спец.очки
        self.damage = damage # урон от спец.атаки

    def special_attack(self, other):
        """
        метод атаки special_attack, которая возможна только если количество 
                спец.очков более 0.
        """  
        if self.unique_power > 0:
            other.damage -= self.unique_power
            self.unique_power -= 1
            print (f"""
                   {self.name} применил специальную атаку против {other.name}.\n
                   Уникальная сила {self.name}: {self.unique_power} спец. очков. \n
                   Урон {other.name}:{other.damage} спец. очков.
                   """)
        else:
            print( f"Уникальное свойство истощено: нет спец.очков")


    def do_attack(self,other):
        """
        Метод attack, который при атаке с вероятностью 25% использует 
        спец.способность героя, если у него остались спец.очки. 
        При спец атаке вычитать из очков 1. Если вероятность пришлась на
        остальные 75% - выполняется обычную атаку. Выводит сообщение в консоль 
        о типе и результате атаки
        """
        if self.unique_power > 0  and random.randint(1,100) <= 25:
            self.special_attack(other)
        else:
            self.kick(other)

           
    def kick(self, other): 
               
        other.armor -= self.strong
        if other.armor < 0:
            other.health += other.armor
            other.armor = 0 

        print (f"""
                {self.name} применил обычную атаку против {other.name}.\n
                {self.name}: состояние защиты:{self.armor}, состояние здоровья: {self.health}. \n
                {other.name}: состояние защиты:{other.armor}, состояние здоровья: {other.health}. 
                """)  
    


    def __str__(self):
        return f'{self.name}'
    

    def __repr__(self):
        return f'{self.name}'

           
           
                 



class Mag(Hero, Spec_Attac):
    def __init__(self, name, health, armor, strong, unique_power, damage) -> None:
        # Hero.__init__(self, name, health, armor, strong)
        Hero.__init__(self,name, health, armor, strong)
        Spec_Attac.__init__(self, unique_power, damage)
        
   
    def print_info(self, sep="-"):
        info =  f"{__class__.__name__}\n"   \
                f"{Hero._get_info(self)}\n"  \
                f"{sep*20}\n" \
                f"Mana - {self.unique_power}\n"
        print(info)

       

# орки(ярость)
class Orc(Hero, Spec_Attac):   

    def __init__(self, name, health, armor, strong, unique_power, damage) -> None:
        # Hero.__init__(self, name, health, armor, strong)
        Hero.__init__(self, name, health, armor, strong)
        Spec_Attac.__init__(self, unique_power, damage)
       
   
    def print_info(self, sep="-"):
        info =  f"{__class__.__name__}\n"   \
                f"{Hero._get_info(self)}\n"  \
                f"{sep*20}\n" \
                f"Ярость - {self.unique_power}\n"
        print(info)
    

# гномы(выносливость)
class Dwarf(Hero, Spec_Attac): 

    def __init__(self, name, health, armor, strong,  unique_power, damage) -> None:
        # Hero.__init__(self, name, health, armor, strong)
        Hero.__init__(self, name, health, armor, strong)
        Spec_Attac.__init__(self, unique_power, damage)
       
   
    def print_info(self, sep="-"):
        info =  f"{__class__.__name__}\n"   \
                f"{Hero._get_info(self)}\n"  \
                f"{sep*20}\n" \
                f"Выносливость - {self.unique_power}\n"
        print(info)
 


# эльфы(ловкость)
class Elf(Hero, Spec_Attac):    

    def __init__(self, name, health, armor, strong,  unique_power, damage) -> None:
        # Hero.__init__(self, name, health, armor, strong)
        Hero.__init__(self, name, health, armor, strong)
        Spec_Attac.__init__(self, unique_power, damage)
    
   
    def print_info(self, sep="-"):
        info =  f"{__class__.__name__}\n"   \
                f"{Hero._get_info(self)}\n"  \
                f"{sep*20}\n" \
                f"Ловкость - {self.unique_power}\n"
        print(info)


# драконы(огонь)
class Dragon(Hero, Spec_Attac):  


    def __init__(self, name, health, armor, strong, unique_power, damage) -> None:
        # Hero.__init__(self, name, health, armor, strong)
        Hero.__init__(self, name, health, armor, strong)
        Spec_Attac.__init__(self, unique_power, damage)
        
   
    def print_info(self, sep="-"):
        info =  f"{__class__.__name__}\n"   \
                f"{Hero._get_info(self)}\n"  \
                f"{sep*20}\n" \
                f"Огонь - {self.unique_power}\n"
        print(info)




