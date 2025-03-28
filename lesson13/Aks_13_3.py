"""
в файле hero1 добавить следующий функционал
        - добавить несколько классов других героев унаследовав их от Hero.
        - Каждому герою добавить уникальное свойство-спец.очки (мана, ярость, и т.п. ) и 
                и свойство cо значением урона от спец.атаки.
        - Создать метод атаки special_attack которая возможна только если количество 
                спец.очков более 0.
        - Добавить метод attack который при атаке с вероятностью 25% будет использовать 
                спец.способность героя если у него остались спец.очки. 
                При спец атаке вычитать из очков 1. Если вероятность пришлась на
                остальные 75% - выполнить обычную атаку. Вывести сообщение в консоль 
                о типе и результате атаки.

добавить класс Arena:
        - атрибут warriors - все воины на арене (тип list)
        - магический метод __init__, который принимает необязательный аргумент warriors.
                Если был передан список warriors, та заполняет им атрибут. Если нет, то заполняет
                пустым списком.
        - метод add_warrior, который принимает аргумент warrior и добавляет его к warriors.
                Если данный воин уже есть в списке, то бросить исключение ValueError("Воин уже на арене").
                Если нет, то добавить воина к списку warriors и вывести сообщение на экран
                "{warrior.name} участвует в битве"
        - метод choose_warrior, который не принимает аргументов и возвращает случайного
                воина из warriors
        - метод battle, который не принимает аргументов и симулирует битву. Сперва 
                должна пройти проверка, что воинов на арене больше 1. Если меньше, то бросить
                исключение ValueError("Количество воинов на арене должно быть больше 1").
                Битва продолжается, пока на арене не останется только один воин. Сперва
                в случайном порядке выбираются атакующий и защищающийся. Атакующий ударяет
                защищающегося. Если у защищающегося осталось 0 health_points, то удалить его
                из списка воинов и вывести на экран сообщение "{defender.name} пал в битве".
                Когда останется только один воин, то вывести сообщение "Победил воин: {winner.name}".
                Вернуть данного воина из метода battle.
                
                
Создать несколько воинов используя разные классы, добавить их на арену и запустить битву. 
Выжить должен только один.

"""

from Aks_hero1 import Hero, Spec_Attac, Mag, Orc, Dwarf, Elf, Dragon
from Aks_Arena import Arena

   
hero1 = Mag('Gendalf', 5, 4, 10, 5, 0)
hero2 = Mag('Gendalf2', 5, 3, 10, 7, 0)    
hero3 = Orc('Ужасный', 5, 4, 10, 3, 0) 
hero4 = Dwarf('Мелкий', 5, 3, 10, 3, 0) 
hero5 = Elf('Цветочек', 5, 3, 10, 5, 0) 
hero6 = Dragon('Roarrr', 10, 4, 10, 10, 0) 

heroes = [hero1, hero2, hero3, hero4, hero5, hero6]

Arena_1 = Arena(heroes)
  

# Arena_1._add_warrior(hero6)


Arena_1.battle()


       