"""
Дан словарь наблюдения за температурой 
{"day1":18, "day2":22, "day3":7, "day4":11, "day5":14}. 
Отсортировать словарь по температуре в порядке возрастания и обратно.

"""
d = {"day1":18, "day2":22, "day3":7, "day4":11, "day5":14}

b = dict(sorted(d.items(), key = lambda x: x[1], reverse = False))
c = dict(sorted(d.items(), key = lambda x: x[1], reverse = True))
print(b)
print(c)