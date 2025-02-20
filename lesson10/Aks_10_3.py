"""
Написать функцию которая принимает строку в которой есть 
круглые скобки и возвращает True или False анализируя все ли скобки 
являются закрытыми и расставлены в правильном порядке.
Примеры:
    (()()) -> True
    (()()() -> False
    (hello(2)ver()(33)python) -> True
    (hello(2()ver(33)python)) -> True
    (hello(2()ver(33)python) -> False

# """


def find_brackets(text):
    a = []
    for symbol in text:
        if symbol == '(' or symbol == ')':
            a.append(symbol)
    
    ok = True if text.count('(') == text.count(')') and a[0] == '(' and a[-1] ==')' else False
    # print(text.count('('))
    # print(text.count(')'))
    return ok


# s = '(hello(2)ver()(33)python)'
print(find_brackets('(()())'))
print(find_brackets('(()()()'))
print(find_brackets('(hello(2)ver()(33)python)'))
print(find_brackets('(hello(2()ver(33)python))'))
print(find_brackets('(hello(2()ver(33)python)'))



