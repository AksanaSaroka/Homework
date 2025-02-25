"""
Написать декоратор который позволит не останавливать программу 
в случае если любая декорируемая функция выбрасывает ошибку, 
а выводить имя функции в которой произошла ошибка и информацию об ошибке в. 
Имя функции можно узнать использовав свойство __name__ ( print(func.__name__))

* сделать настраиваемы параметр который определяет печать в консоль или в файл
и если в файл передать название фала
"""

import os
file_dir = os.path.dirname(__file__)


def f_nonstop(filename, to_file = False):
    def f_nonstop_1(func):
        def wrapper(*args,**kwargs):
            try:
                return func(*args,*kwargs)
            except Exception as e:
                text_err = f"Произошла ошибка в {func.__name__}. Ошибка {str(e)}\n"
                if filename and to_file:
                    with open (f'{file_dir}\\{filename}',"a",encoding='utf8') as f:
                        f.write(text_err)
                        print(f"Произошла ошибка в {func.__name__}. Ошибка записана в файл {file_dir}\\{filename}")
                else:       
                    print(text_err)
        return wrapper
    return f_nonstop_1
   

@f_nonstop('')
def f1(a):
    a = 1/a
    return a

@f_nonstop('log1.txt',True)
def f11(a):
    a = 1/a
    return a
    
print(f1(5))
print(f1(0))
print('hahaha')
print(f1('ttt'))
print(123)
print(file_dir)

print(f11(5))
print(f11(0))
print('hahaha')
print(f11('ttt'))
print(123)
print(file_dir)


