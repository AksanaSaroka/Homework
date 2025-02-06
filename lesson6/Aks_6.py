"""
Даны 4 переменные - a1, a2, a3, a4.
1 - вывести True если все они дробные числа
2 - вывести True если одна из них строка
3 - вывести True если  одна пара переменных является целочисленным типом. 
    Пары могут образовать только следующие переменные - a1-a3, a2-a4, a3-a4"
"""

# s = [a1, a2, a3, a4]
s = [1, 0.1, 3, 0.7]

print(all(type(x) is float for x in s))
print(any(type(x) is str for x in s))

pairs = [(s[0],s[2]), (s[1],s[3]), (s[2],s[3])]
print(pairs, any(type(x) is int and type(y) is int for x, y in pairs) )