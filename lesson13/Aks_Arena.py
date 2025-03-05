import random




from Aks_hero1 import Hero, Spec_Attac

class Arena(Hero,Spec_Attac):

    # конструктор - тут мы создаем свойства которые должны быть у каждого нового объекта
    # и присылаем сюда первоначальные их значения
    def __init__(self, warriors=[]) -> None:
        # свойства объектов
        self.warriors = warriors #все воины на арене

           
    # методы - это действия/команды которые могут выполнять объекты
    def _add_warrior(self, warrior):
        for warrior in self.warriors:
            if warrior in self.warriors:
                raise ValueError("Воин уже на арене")
            else:
                self.warriors.append(warrior)
                print(f"{warrior.name} участвует в битве")
        
    def choose_warrior(self):
        return random.choice(self.warriors)
    
    def battle(self):

        if len(self.warriors) <= 1:
            raise ValueError("Количество воинов на арене должно быть больше 1")        
        while len(self.warriors) > 1:
            a = self.choose_warrior()
            b = self.choose_warrior()
            if a == b:
                b = self.choose_warrior()
            print(f"Битва между {a.name} и {b.name}")
            Spec_Attac.do_attack(a,b)
            
            if b.health <= 0:
                self.warriors.remove(b)
                print(f"{b.name} пал в битве" )


        else:
            print(f"Победил воин: {self.warriors}")
            return  self.warriors

    def __str__(self):
        return f'{self.warriors}'
    

    def __repr__(self):
        return f'{self.warriors}'
    

           
                 



 







