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


text = input('Введите товар: ')
print(f"{float(products[text])*1.15:.2f}")


s_of_products = sum(map(float, products.values()))
print('Сумма', f"{s_of_products:.2f}")

