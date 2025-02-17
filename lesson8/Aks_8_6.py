"""
Напишите функцию yes_or_no, которая принимает список из целых чисел,
а возвращает список из Yes или No для каждого элемента, 
Yes - если число уже встречалось и No, если нет
[1,2,3,1,4] => [no, no, no, yes, no]

если в списке не все целые числа вернуть False.

"""
sp = [1,2,3,1,4]

def  fun_yes_or_no(lst):
    """
    Функция yes_or_no принимает список из целых чисел,
    а возвращает список из Yes или No для каждого элемента, 
    Yes - если число уже встречалось и No, если нет
    """
    
    results = ['yes' if a in lst[:i] else 'no' for i, a in enumerate(lst)]
    # print(results)
    if not all(isinstance(x,int) for x in lst):
        return('False')
    else:
        return(results)



print(fun_yes_or_no(sp))