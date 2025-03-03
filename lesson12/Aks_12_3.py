"""

Описать класс Counter, реализующий целочисленный счетчик.
который может увеличивать или уменьшать свое значение (атрибут value)
на единицу в заданном диапазоне.

Предусмотреть инициализацию счетчика значениями по умолчанию и произвольными значениями.

Определить атрибуты(свойства):
    - value - текущее значение счетчика
    ...

Определить методы:
    - инициализатор __init__, который устанавливает значение счетчика или 0 по умолчанию
    - increase(num=1), увеличивает счетчик на заданную величину или 1 по умолчанию
    - decrease(num=1), уменьшает счетчик на заданную величину или 1 по умолчанию
    - reset, сбрасывает значение счетчика на стартовое    
    - метод __iter__
    - метод __next__
    
    * - stat, возвращает среднее количество изменений счетчика в секунду

"""
class Counter:
    text_err = "Выход за пределы диапазона"

    def __init__(self, start=0, value=0, end=1):
        self.start = start
        self.value = value
        self.end = end

    def __increase__(self):
        if  self.start <= self.value < self.end:
            self.value += 1
            return self.value
        else:
            return self.text_err
        
        

    
    def __decrease__(self):
        if  self.start < self.value <= self.end:
            self.value -= 1
            return self.value
        else:
            return self.text_err

    def __reset__(self):
        return self.start
    
    def __iter__(self):
        return self

    def __next__(self):
        if  self.start <= self.value <= self.end:
            value = self.value
            self.value += 1
            return value
        else:
            return self.text_err

        

a = Counter(10,11,15)
print('(1)',a.__increase__())
print('(2)',a.__increase__())
print('(3)',a.__decrease__())
print(a.__reset__())

print('(4)', a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())

b = Counter()
print('(1)',b.__increase__())
print('(2)',b.__increase__())
print('(3)',b.__decrease__())
print(b.__reset__())
print('(4)', b.__next__())
print(b.__next__())
print(b.__next__())
