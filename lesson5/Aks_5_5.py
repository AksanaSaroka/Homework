"""
Запросить фразу 
    - вывести на экран количество уникальных символов
    - вывести на экран количество уникальных слов
    -* вывести символ который встречался чаще всего

"""

from collections import Counter

fraza = input('Введите фразу: ')

c = Counter(fraza)
sorted(c.elements())


print('количество уникальных символов: ', len(set(fraza)))
print('количество уникальных слов: ', len(set(fraza.split())))
print('символ, который встречался чаще всего: ', c.most_common(1))

# print(c)