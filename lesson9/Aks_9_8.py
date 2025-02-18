'''
Дан список содержащий в себе различные типы данных, отфильтровать таким
образом, чтобы 
 - остались только строки.
 - остался только логический тип.
 
'''
s = ['a', 'b', 4, True, 'Hello', False, 0.25]

print(list(filter(lambda x:isinstance(x,str), s)))
print(list(filter(lambda x:isinstance(x,bool), s)))