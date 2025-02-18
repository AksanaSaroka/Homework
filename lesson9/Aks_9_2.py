'''
Написать рекурсивную функцию, которая вычисляет  
факториал переданного в нее числа.

'''



def factorial_rec(a:int):
    """
    factorial_rec - рекурсивная функция, которая вычисляет  
    факториал переданного в нее числа. 
    """
    # n! = (n – 1)! × n
    
    if a > 1:
        return (factorial_rec(a-1)*a)
    elif 0 <= a <= 1:
        return 1
    else:
        return 'err: факториал не может быть отрицательным числом '
      

print(factorial_rec(5))
print(factorial_rec(0))
print(factorial_rec(-1))

 