'''
Дан список:
['hello', 'python', 'интерпретатор', 'pep8', "123"]
Вернуть список где вместо элементов данного списка прописаны количество символов каждого элемента.

'''
s = ['hello', 'python', 'интерпретатор', 'pep8', "123"]

b = list(map(len, s))
print(b)
