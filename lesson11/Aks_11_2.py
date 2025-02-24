"""
Написать функцию hello, которая принимает 2 аргумента name и surname и
выводит принтом "Привет, {name} {surname}"

Написать декоратор log_decorator, который перед выполнением
функции печатает на экран строку, вида
Выполняеся функция <имя> с аргусентами <аргументы> 
После выполнения функции напечатать строку "<имя функции> - завершена"
"""
def log_decorator(func):
    def wrapper(*args):
        print(f"Выполняеся функция <{func.__name__}> с аргументами <{args}>.")
        func(*args)
        print(f"Функция <{func.__name__}> завершена.")
    return wrapper

@log_decorator
def f_hello(name:str,surname:str):
    print(f"Привет, {name} {surname}!")


f_hello('Оксана', 'Сороко')