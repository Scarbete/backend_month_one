# Структуры данных: Списки, срезы, кортежи

# numbers = list(range(1, 6))

# numbers = [i*i for i in range(1, 6) if i < 4]

# print('numbers', numbers)

# words = ['Python', 20, 3.14, True, False, numbers]

# print('old words', words)

# Также рассмотрим CRUD:

# Create - (Создание) либо (Добавление)
# words.append('apple')
# words.insert(0, 'geektech')
# words.extend(numbers)

# print('words after (Create)', words)

# Read - Чтение (получение)

# Update - Обновление (редактирование)
# words[1] = False

# words[0], words[3] = words[3], words[0]

# words.insert(3, words.pop(0))

# print('words after (Update)', words)

# Delete - Удаление
# words.remove('geektech')
# words_last_element = words.pop(len(words) - 1)
# del words[4:]

# print('words after (Delete)', words)

# print('finally words', words)

# words.sort()

# words.sort(reverse=True)

# print('sorted words', words)

# words.reverse()

# print('reversed words', words)

# words = ['Python', 'apple', 'geektech', 'bishkek', 'Backend']
# new_copy = words.copy()
#
# new_copy[0] = 1337
#
# print(id(words), id(new_copy))
# print(new_copy is words)
#
# print(words)
# print(new_copy)

# Практика с срезами
# phone_humber = '+996557820078'
# country_code = phone_humber[:4]
# print('country_code', country_code)

# words.sort()

# words.sort(key=len)

# print('words', words)

# words = ['Python', 'apple', 'geektech', 'Яблоко', 'ананас']
# words_copy = words.copy()
#
# print('id', id(words), id(words_copy))
# print('\nwords is words_copy', words is words_copy)
#
# words_copy[0] = 100
#
# print(f'\n{words=}')
# print(f'{words_copy=}')

# Tuple - (кортеж)
# Тоже самое что и списки но он не меняется
# Они нужны для того чтобы хранить данные которые не будут менятся
# my_tuple = (100, True, 'python', 3.14)

# print(my_tuple)
# print(type(my_tuple))

# my_tuple[0] = 'apple'
# (tuple) object does not support item assignment

# конвертация кортежа в списка

# my_tuple = list(my_tuple)

# print(my_tuple)
# print(type(my_tuple))

# my_tuple = tuple(my_tuple)

# print(my_tuple)
# print(type(my_tuple))

# Можно итерироваться по кортежу
# for i in my_tuple:
#     print(i)

# my_new_tuple = (2)
# my_new_tuple = (2,)

# print(my_new_tuple)
# будет int - так как если в кортеже одно
# значение то оно становится его же типом
# print(type(my_new_tuple))

# my_tuple = (100, True, 'python', 3.14)

# (100, True, 'python', 3.14)
# print('my_tuple (old)', my_tuple)

# my_tuple += (56, '111', 34)

# (100, True, 'python', 3.14, 56, '111', 34)
# print('my_tuple (new)', my_tuple)

# words = [312, 3123, 13, 123]
# print('words old', words)  # [312, 3123, 13, 123]

# words += (3, 132, 2131)  # [312, 3123, 13, 123, 3, 132, 2131]
# print('words new', words)
