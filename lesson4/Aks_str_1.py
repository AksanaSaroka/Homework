'''
Программа должна запросить любую фразу и вывести на экран :
     - количество символов в данной фразе.
     - количество слов  в данной фразе. 
            Словом может считаться любой набор символов разделенный от 
            других пробелом и количеством символов больше или равных 1.
     -* количество гласных в данной фразе. Нельзя использовать if и for.

'''


fraza = input('Введите фразу: ')
glasn = 'aeiouyаеёиоуыэюя'


words = fraza.split()
num_words = len(words)

fraza_lower = fraza.lower()
num_glasn = sum(map(fraza_lower.count, glasn))

print('Количиство символов:', len(fraza))
print('Количиство слов:', num_words)
print('Количиство гласных:', num_glasn)

