"""
Создать класс Student.


Определить атрибуты:
    - surname - фамилия
    - name - имя
    - group - номер группы
    - grads - список оценок

Определить методы:
    - инициализатор __init__
    - Методы __eq__, __ne__, __lt__, __gt__, __le__, __ge__, которые будут сравнивать
    студентов по среднему баллу
    - метод add_grade - добавляет в список оценок одну или несколько оценок от 1 до 10
    - метод average_grade -считает и возвращает среднюю оценку ученика

Создать список из 5 студентов класса и вывести его отсортированным по возрастанию
и убыванию.

Вывести студентов, у которых средний балл больше 8
"""


from faker import Faker
f = Faker("ru-RU")



class Student:

    def __init__(self, surname, name, group, grades=[]):
        self.surname = surname
        self.name = name
        self.group = group
        self.grads = grades
    
    def __eq__(self,other_obj):
        return self.average_grade == other_obj.average_grade
    
    def __ne__(self,other_obj):
        return self.average_grade != other_obj.average_grade
    
    def __lt__(self,other_obj):
        return self.average_grade < other_obj.average_grade

    def __gt__(self,other_obj):
        return self.average_grade > other_obj.average_grade

    def __le__(self,other_obj):
        return self.average_grade <= other_obj.average_grade

    def __ge__(self,other_obj):
        return self.average_grade >= other_obj.average_grade

    def add_grade(self,*grades):
        return self.grads.extend(grades)
    
    def __iter__(self):
        return self
    
    def average_grade(self):
        return sum(self.grads)/len(self.grads)
    
    def __str__(self):
        return f"{self.surname} {self.name} ,{self.group} ,{self.grads}"
    
    def __repr__(self):
        return f"{self.surname} {self.name}, {self.group}, {self.grads}"



students = []  
for i in range(1,6):
    student = Student(f.last_name(), f.first_name(), f.random_int(110,115), [f.random_int(min=1, max=10) for k in range(10)])
    students.append(student)
print(students) 


students.sort(key=lambda x: x.average_grade(),reverse=False)
print('\nОтсортированнй список студентов повозрастанию среднего балла:')
for student in students:
    print(f"{student.surname} {student.name} - {student.average_grade()}")

students.sort(key=lambda x: x.average_grade(),reverse=True)
print('\nОтсортированнй список студентов убыванию среднего балла:')
for student in students:
    print(f"{student.surname} {student.name} - {student.average_grade()}")

print('\nCписок студентов со средним баллом выше 8:')
for student in filter(lambda x: x.average_grade()>= 8, students):
    print(f"{student.surname} {student.name} - {student.average_grade()}")
else:
    print('Студентов со средним баллом выше 8.0 пока нет')
