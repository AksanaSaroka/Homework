'''
Написать функцию count_char, которая принимает строковое значение,
из которого создает и возвращает словарь, следующего вида:
{'буква': 'количество-вхождений-в-строку'}
Нельзя пользоваться collections.Counter!

'''
text = 'Магазин игрушек на Немиге'

def count_char(text:str):

    d = {}
    count = 0
    for symbol in text:
        if symbol:
            count += 1
            d.update({symbol: count})
    return(d)

print(count_char(text))