"""
Запросить у пользователя год рождения и в соответствии с его возрастом 
охарактеризовать пользователя - 
ребенок, подросток, юноша, в расцвете сил, пожилой, старик.
"""

from datetime import datetime

god_rozhd = int(input('Введите Ваш год рождения: '))
d = datetime.now()
age = d.year - god_rozhd


if age <= 10:
    print('Вы ребёнок')
elif 10 < age <=  17:
    print('Вы подросток')
elif 17 < age  <=  21:
    print('Вы юноша')
elif 21 < age  <=  60:
    print('Вы Карлсон')
elif 60 < age  <=  75:
    print('Вы как коньяк')
else:
    print('Вы аксакал')