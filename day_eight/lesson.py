# Работа с файлами
# "r" - чтение (read).
# "w" - запись (write).
# "a" - добавление (append).

from time import sleep as ukta

# "x" - создание файла 
# безопасный режим создание файла
# (чтобы не было конфликтов по названиям файла)

# encoding='UTF-8' - метод кодировки

# старый вариант
# w - write
# file = open('file.txt', 'w', encoding='UTF-8')
# file.write('Бишкек, Кыргызстан!')
# file.close()

# новый вариант
# a - append
# with open('file.txt', 'a') as file:
#     file.write('\n2222')

# with open('file.txt', 'x') as file:
#     file.write('123123123')

# r - read
# with open('file.txt', 'r') as file:
    # print(file.read())
    # print(file.readline())
    # print(file.readlines())  # ['\n', '2222\n', '2222\n']
    # print(file.readlines()[-2])  # last text in file

# with open('file.txt', 'r') as file:
#     for i in file.read():
    # for i in file.readline().split():
        # ukta(0.5)
        # print(i, end='')
    #     print(i, end='')
    # print(file.readlines())

# from random import randint, choice
# from datetime import datetime

# with open('results.txt', 'w') as file:
#     file.write('')

# students = [2, 3, 4, 6, 9, 10, 11, 13, 12, 7]

# while len(students) != 0:
#     first = randint(2, 10)
#     second = randint(11, 101)
#     student_id = choice(students)
#     name = input(f'name: {student_id}: ').title()
#     start = datetime.now()
#     user_answer = int(input(f'Сколько будет {first} * {second} = '))
#     end = datetime.now() - start
#     right_answer = first * second

#     if user_answer == right_answer:
#         print(True)
#         with open('results.txt', 'a') as file:
#             file.write(
#                 f'{name} {first} * {second} = {user_answer} {right_answer} '
#                 f'{end.seconds} правильно\n'
#             )
#     else:
#         print(False, right_answer)
#         with open('results.txt', 'a') as file:
#             file.write(
#                 f'{name} {first} * {second} = {user_answer} {right_answer} '
#                 f'{end.seconds} не_правильно\n'
#             )
#     students.remove(student_id)

# answers = []

# with open('results.txt', 'r') as file:
#     for line in file.readlines():
#         name = line.split()[0]
#         seconds = line.split()[-2]
#         status = line.split()[-1]
#         answers.append({
#             'name': name,
#             'seconds': seconds,
#             'status': status
#         })

# for i in answers:
#     if i['status'] == 'не_правильно':
#         print(i)
