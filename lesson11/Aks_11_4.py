'''
открыть и обработать файл students_grades.txt
собрать все данные в словарь ниже приведенного формата
записать в файл "excellent_students.txt" по 1 ученику из класса с наибольшим балом
{
    "9A":[
        {'fio':'fio', 
         'objects':{
            'mathematics':[4, 9, 7],
            'physics':[8, 9, 8, 6],
            ...:...
            }
        },
        ...        
    ],
    "9Б":[
        ...
    ]
}

'''
import os
import pickle
from pprint import pprint


file_dir = os.path.dirname(__file__)

# with open (f'{file_dir}\\students_grades.txt',"r",encoding='utf-8') as file:
#     lines = file.readlines()

with open(f'{file_dir}\\students_grades.txt',"rb") as file:
   lines = pickle.load(file)   
   
# # print(lines)
# # students = []
# # for line in lines:
# #     line.replace('\n',' ')
# #     students.append(line)
# students = [(line.replace('\n',' ')) for line in lines]
# print(students)
# # students = [list(line.split(',')) for line in lines]
# # print(students[0][1])
# # print(type(students))
# # b = sorted(students, key = lambda student :student[1],reverse=False)
# # print(students[1])

# dict_students = {}
# for student in students:
#     dict_students = {'student':[student]}
#         # dict_students = {'fio':student[0],'cl':student[1]}
#     #     #              ,'objects':{
#     #     # 'mathematics':int(student[2])}}
# print(dict_students)
    

# # with open (f'{file_dir}\\excellent_students.txt',"wb") as file:
# # print(students.index('9A'))            