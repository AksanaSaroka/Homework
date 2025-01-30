"""
Запросить трижды ввод наименования товаров и их цену через пробел. 
"пример: 
>>>яблоко 10"
>>>груша 15
>>>малина 20
    
    - создать из введенных данных словарь где ключ это наименование, а цена значение
    - запросить имя товара, найти его в словаре, и вывести его цену, увеличенную на 15%. 
    - вывести сумму всех товаров

"""


product1 = input('Введите 1-ый товар и его цену -')
product2 = input('Введите 2-ой товар и его цену -')
product3 = input('Введите 3-ий товар и его цену -')


product11 = product1.split()
product22 = product2.split()
product33 = product3.split()

products = dict([product11, product22, product33])
print(products)

a = list(products.items())[1][1]
print(int(a)*1.15)

b =list(products.values())
c = list(map(int, b))
s_of_products = sum(c)

print('Сумма', s_of_products)

