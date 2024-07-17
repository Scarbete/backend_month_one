# Домашнее задание (4)
# Дан кортеж состоящий из разных типов данных:
# data_tuple = ('h', 6.13, 'C', 'e', 'T', True, 'k', 'e', 3, 'e', 1, 'g')

# 1 ) Создать два пустых списка letters и numbers

# 2 ) Пройтись циклом for по кортежу data_tuple, добавить
#     все строки в список letters, а всё остальное в numbers.

# 3 ) Из списка numbers удалить число 6.13 и переместить True
#     в конец списка letters, затем вставить число 2 между 3 и 1

# 4 ) Отсортировать numbers, реверсировать
#     letters и изменить пару букв в letters.

# 5 ) Измените список numbers в список квадратов своих же чисел

# 6 ) Преобразовать списки numbers и letters в кортежи

# (В итоге):
# кортеж letters должен выглядеть так:
# (True, 'G', 'e', 'e', 'k', 'T', 'e', 'c', 'h')

# кортеж numbers должен выглядеть так:
# (1, 4, 9)

data_tuple = ('h', 6.13, 'C', 'e', 'T', True, 'k', 'e', 3, 'e', 1, 'g')

letters = []
numbers = []

for item in data_tuple:
    if isinstance(item, str):
        letters.append(item)
    elif isinstance(item, (int, float)):
        numbers.append(item)
    else:
        print(f'{item} (не корректный тип данных)')

numbers.remove(6.13)
letters.append(numbers.pop(numbers.index(True)))
numbers.insert(1, 2)

numbers.sort()
letters.reverse()

letters[letters.index('g')] = 'G'
letters[letters.index('C')] = 'c'

numbers = [num ** 2 for num in numbers]

letters_tuple = tuple(letters)
numbers_tuple = tuple(numbers)

# (Result)
print(letters_tuple)
print(numbers_tuple)
