"""
Написать функцию (без регулярных выражений), которая принимает текстовую строку 
и возвращает словарь, который содержит информацию о количестве 
символов, слов, строк и предложений в тексте. 
Затем создайте вторую функцию, которая принимает этот словарь, 
и выводит его содержимое в удобном и красивом формате. 

"""
text_user = """Жила маленькая девочка. Мать любила ее без памяти, а бабушка еще больше.
Ко дню рождения внучки подарила ей бабушка красную шапочку. С тех пор девочка всюду в ней ходила."""
from pprint import pprint

def make_dict(text:str):
    d = {}
    number_of_symbols = len(text)
    number_of_words = len(text.split(' '))
    number_of_lines = len(text.split('\n'))
    number_of_sentences = len(text.split('.'))
    d = {'symbols':number_of_symbols,'words':number_of_words, 'lines': number_of_lines,'sentences':number_of_sentences}
    return(d)

def print_dict(text:str,param:dict={}):
    # param = make_dict(text)
    pprint(make_dict(text))


# print(make_dict(text_user))
print_dict(text_user)