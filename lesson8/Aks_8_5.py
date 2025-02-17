'''
Написать функцию count_char, которая принимает строковое значение,
из которого создает и возвращает словарь, следующего вида:
{'буква': 'количество-вхождений-в-строку'}
Нельзя пользоваться collections.Counter!

'''
text = 'Магазин'

def count_char(text:str):
    d = {}
    for symbol in text:
        count = 0
        count += text.count(symbol)
        d.update({symbol: count})
    return(d)

print(count_char(text))