# Логический тип данных, условные конструкции и операторы
# ( True, False, ==, !=, >=, <=, <>, and, or, not )
# bool - логический тип данных ( True, False )
# False - Ложь
# True - Правда
# == ровно ?
# != не ровно ?
# >= больше либо равен ?
# <= меньше либо равен ?
# or, and, not

# print('Hello World!')

# time = 'day'

# if time == 'morning':
#     print('good morning')
# elif time == 'day':
#     print('good day')
# elif time == 'evening':
#     print('good evening')
# else:
#     print('hello')

# print('5 > 8', 5 > 8)  # 5 больше 8 ? False - Ложь
# print('5 < 8', 5 < 8)  # 5 меньше 8 ? True - Правда

# print('type(5 < 8)', type(5 < 8))  # bool - логический тип данных

# print(2 == 3)  # == ровно ?
# print(2 != 3)  # != не ровно ?

# print(3 >= 2)  # 3 больше либо равен 2 ?

# print(2 > 1 and 2 < 7)  # True
# print(1 < 2 < 7)  # True
# print(not True)  # False

# Операторы назначения
# ( =, +=, -=, *=, /=, %=, **=, //= )

# a = 10
# a = a + 5

# a += 5
# a -= 5
# a *= 5
# a /= 5
# a **= 5
# a //= 5

# print(a)

# Условные операторы ( if, elif, else )

# name = 'Kutman'
# surname = 'Nurlanov'
# age = 20

# if age >= 25:
#     print(f'Hello {name} {surname}')
# elif age >= 18:
#     print(f'Hi {name}')
# else:
#     print('Your age is not suitable')

# time = 'утро'

# if time == 'morning' or time == 'утро':
#     print('good morning')
# elif time == 'day' or time == 'день':
#     print('good day')
# elif time == 'evening' or time == 'вечер':
#     print('good evening')
# else:
#     print('hello')

# len возвращяет количество элементов в массиве либо буквы в строке

# print(len('python'), len('javascript'))

# arr = [1, 21, 3, 123, 1, 23, 1, 12, 3]
#      0   1  2   3   4   5  6   7  8
# индексы

# print(len(arr))  # result - 9

# password_one = input('Введите пароль: ')
# password_two = input('Подтвердите пароль: ')

# if password_one == password_two:
#     print('Вы вошли в систему')
# else:
#     print('Введен не правильный пароль')

# word = 'python'

# [start:stop:step] - индексы ( срезы )

# print(word[2])
# print(word[0:3])
# print(word[::2])
# print(word[::-1])  # перевернули
# print(word[::-2])

# signal = input('Введите цвет светофора: ')

# if signal == 'green':
#     print('go')
# elif signal == 'yellow' or signal == 'red':
#     print('stop')
# else:
#     print('invalid olor (red, green, yellow)')
#     situation = input('write situation: ')
#     if situation == 'off':
#         print('check right and left side')
#     elif situation == 'police':
#         print('wait signal')

# current_time = int(input('Введите данное время в формате (0 или 24): '))

# if 6 <= current_time <= 11:
#     print('Доброе утро')
# elif 12 <= current_time <= 17:
#     print('Добрый день')
# elif 18 <= current_time <= 24:
#     print('Добрый вечер')
# elif 0 <= current_time <= 5:
#     print('Иди спать чел ты')
# else:
#     print('Вы ввели не корректное значение')

# password = input('Придумайте пароль: ')

# if len(password) >= 8 and not password.isalpha() and not password.isnumeric():
#     print('ok, password is great')
# else:
#     print('no')

# isalpha - Дополнительно проверяется, что пароль не состоит
# только из букв (метод isalpha())

# isnumeric - и не состоит только из цифр (метод isnumeric())

# Если оба этих условия выполнены (т.е., пароль
# содержит хотя бы один символ, который не является
# буквой или цифрой), выполняется следующий блок кода.

# Таким образом, программа проверяет, что пароль:
# Имеет длину не менее 8 символов.
# Не состоит только из букв или только из цифр.

# check_index = input('Введите текст: ')

# print(f'{check_index[0:2]}-{check_index[3:5]}')
