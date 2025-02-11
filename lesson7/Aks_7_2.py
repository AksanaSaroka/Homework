'''
Запросить фразу состоящую минимум из трех слов. 
Сформировать фразу из этих слов в которой каждая буква слова, 
продублирована то количество раз, которое соответствует номеру позиции 
данной буквы в слове этой буквы. 
Например: Привет как дела => Прриииввввееееетттттт кааккк деелллаааа

'''

fraza = input('Введите фразу: ')

words = fraza.split()

# решение через range():
# new_word = ''
# for word in words:
#   a = range(len(word))
#   for i in a:
#     new_word += word[i] * (i+1) 
#   new_word += ' '
# print(new_word)
 

# решение через enumerate():
new_fraza = []
for word in words:
  new_word = ''
  for i, symbol in enumerate(word,1):
    new_word += symbol * i 
  new_fraza.append(new_word)
print(new_fraza)

 

  

            
    

 





