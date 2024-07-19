# Структуры данных: словари, множества.
# { key: value } - { ключ: значение }
# dict - dictionary (словарь)
# set - множество

# defuault dict
# student = {
#     'name': 'Kutman',
#     'age': 20,
#     'hobby': ['программирование', 'киберспорт', 'музыка', 'аниме'],
#     'married': False
#     (Ключами могут быть неизменяемые типы)
#     20: 2004,
#     True: False,
#     False: True
# }

# print('student', student)
# print('type(student)', type(student))

# dict()
# new_dict = dict(name='Aesthetic', age=20)
# print('new_dict', new_dict)
# entries_dict = dict([['name', 'Kutman'], ['age', '20'], ['married', False]])
# print('entries_dict', entries_dict)

# CRUD
# student = {
#     'name': 'Kutman',
#     'age': 20,
#     'hobby': ['программирование', 'киберспорт', 'музыка', 'аниме'],
#     'married': False
# }

# print('student (old)', student)

# (Create)
# print('\nCreate')
# student['height'] = 1.83
# student['hobby'].append('Backend')
# student.update(new_dict)
# print('student (new) [ Create ]:', student)

# (Read)
# print('\nRead')
# print(student['hobby'])
# print(student['hobby'][0])
# print(student['hobby'][-1])
# print(student['hobby'][0:3])
# print(student.get('nam', 'такого ключа нет!'))
# print(student.get('name', 'такого ключа нет!'))
# print('values', student.values())
# print('keys', student.keys())
# print('items', student.items()) # Типа Object.entries как в JS
# for key in student:
#     print(f'{key}: {student[key]}')
# print()
# for key, value in student.items():
#     print(f'{key}: {value}')

# (Update)
# student['age'] += 2
# student['married'] = True
# student['hobby'][-1] = 'Anime'
# print('student (new) [ Update ]:', student)

# (Delete)
# del student['hobby'][-1]
# del student['married']
# deleted = student.pop('hobby')
# print('student (new) [ Delete ]:', student)

# numbers = [i for i in range(1, 6)]
# print('numbers', numbers)  # [1, 2, 3, 4, 5]

# test_obj = {i: i*i for i in range(1, 6)}
# print('test_obj', test_obj)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# new_obj = dict(enumerate('python'))
# print('new_obj', new_obj)  # {0: 'p', 1: 'y', 2: 't', 3: 'h', 4: 'o', 5: 'n'}

# regions = ['chuy', 'osh', 'talas', 'batken', 'y-k', 'jalal-abad', 'naryn']
# data = {i: int(input(f'Сколько градусов в {i}: ')) for i in regions}
# print(f'Средняя температура по КР {round(sum(data.values()) / len(regions), 2)}')

# numbers = {1, 2, 3, 3, 1, 2, 4}
# number2 = [1, 2, 3, 3, 1, 2, 4]

# print(numbers)  # {1, 2, 3, 4}
# print(number2)  # [1, 2, 3, 3, 1, 2, 4]

# print(type(numbers))  # <class 'set'>
# print(type(number2))  # <class 'list'>

# plov = {'рис', 'морковь', 'мясо'}
# manty = {'тесто', 'мясо', 'лук'}

# print('plov', plov)
# print('manty', manty)

# difference - различие
# print('difference', plov.difference(manty))  # {'морковь', 'рис'}
# print('difference', plov - manty)  # {'морковь', 'рис'}

# intersection - пересечение (сходства)
# print('intersection', plov.intersection(manty))  # {'мясо'}
# print('intersection', plov & manty)  # {'мясо'}

# union - смешка
# print('union', plov.union(manty))
# print('union', plov | manty)

# symmetric_difference - все кроме того что их объяденяет
# print('symmetric_difference', plov.symmetric_difference(manty))
# print('symmetric_difference', plov ^ manty)

# CRUD

# ( Create )
# print('add plov old:', plov)
# plov.add('Чеснок')
# print('add plov new:', plov)

# ( Update )
# print('update plov old:', plov)
# plov.update(['лук', 'перец'])
# print('update plov new:', plov)

# ( Delete )
# print('remove plov old:', plov)
# plov.remove('рис')
# print('remove plov new:', plov)

# word = 'инвентаризация'
# word = set(word)
# print(word)

# from random import choice
# from time import sleep

# students = [2, 3, 5, 14, 7, 8, 9, 10, 11, 13, 19]
# answers = {}

# while len(students) != 0:
#     print(students)
#     students_id = choice(students)
#     name = input(f'Имя студента под номером {students_id}: ').title()
#     timer = 20
#
#     while timer != 0:
#         sleep(1)
#         print(timer)
#         timer -= 1
#
#     rate = int(input(f'Оценка для {name}: '))
#     answers[name] = rate
#     students.remove(students_id)

# for name, rate in answers.items():
#     print(f'{name}: {rate}')

# print(sum(answers.values()) / len(answers))

# new_number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# print('new_number', new_number)
# new_number.sort(reverse=True)
# print('new_number', new_number)
# new_number.sort()
# print('new_number', new_number)

# zip Пример:
# arr1 = ["O!", "Megacom"]
# arr2 = ["0705", "0550"]
# zip(arr1, arr2) ->  [("O!", "0705"), ("Megacom", "0550")]

import time

# Данные для теста
data = range(1000000)

# Измерение времени для спискового включения
start_time = time.time()
squares_list_comprehension = [x**2 for x in data]
end_time = time.time()
list_comprehension_time = end_time - start_time

# Измерение времени для обычного цикла for
start_time = time.time()
squares_loop = []
for x in data:
    squares_loop.append(x**2)
end_time = time.time()
loop_time = end_time - start_time

print(f"List comprehension time: {list_comprehension_time}")
print(f"Loop time: {loop_time}")

print(loop_time - list_comprehension_time)
