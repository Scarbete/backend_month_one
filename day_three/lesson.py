# Циклы: ( for & while )

# Цикл for - используется для перебора элементов
# какой-то коллекции, например,
# списка, строки или диапазона чисел.

# Пример 1: Перебор элементов списка
# fruits = ['яблоко', 'банан', 'вишня']

# for fruit in fruits:
#     print('fruit:', fruit)

# Пример 2: Перебор символов строки
# word = 'Python'

# for letter in word:
#     print(letter)

# Пример 3: Использование функции range
# ( i - iterable || item )
# for i in range(5):
#     print(i)

# for i in range(5, 10):
#    print('end -', i)
#    print('end -', i, end='-')

# Функция range(5) создает последовательность
# чисел от 0 до 4 (5 не включается). Цикл for
# перебирает эти числа и выводит их.
# Эта последовательность выглядит следующим образом: 0, 1, 2, 3, 4.

# Цикл while - выполняет код до тех пор,
# пока условие истинно (True). ( indefinite )

# count = 0

# while count < 5:
#     print('while', count)
#     count += 1

# В этом примере цикл while продолжает выполняться,
# пока переменная count меньше 5. После каждого
# выполнения count увеличивается на 1.

# ( Операторы break и continue )
# Иногда нужно досрочно прервать выполнение цикла
# или пропустить оставшуюся часть текущей итерации.

# Оператор ( break ) прерывает выполнение цикла:

# for i in range(10):
#     if i == 5:
#         break
#     print('break ( if i == 5: )', i)

# Этот цикл остановится, когда i станет равно 5.
# и не выполнит код после break

# Оператор ( continue ) пропускает оставшуюся часть
# текущей итерации и переходит к следующей:

# for i in range(10):
#     if i % 2 == 0:
#         continue
#     print(f'Нечетное число: {i}')

# continue - как я понял это просто
# ( пропустить данную часть итерации к следующей )
# Этот цикл пропустит четные числа и выведет только нечетные.

# ( Вложенные циклы )
# Циклы можно вкладывать друг в друга, чтобы, например,
# перебрать элементы в многомерном списке.

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
#
# for row in matrix:
#     print()
#     for num in row:
#         print(f'{num} ')

# for i in range(1, 5):
#     for k in range(1, 4):
#         print(i, k)

# for i in range(5):
#     time = int(input('Введите время: '))
#
#     if 6 <= time <= 11:
#         print('good morning')
#     elif 12 <= time <= 17:
#         print('good day')
#     elif 18 <= time <= 24:
#         print('good evening')
#     elif 0 <= time <= 5:
#         print('sleep bro')
#     else:
#         print('unknow time')

# cash = 10_000
# percents = 0.12
# years = 5

# for i in range(years):
#     cash += cash * percents
#     print(round(cash, 2))

# import time
#
# count = 0
#
# while count < 100:
#     time.sleep(1)
#     print(f'count: {count}')
#     count += 1

# ghbdtn
# руддщ

# Индексы в списках и строках
# word = 'Python'
# print(word[0])  # 'P'
# print(word[1])  # 'y'
# print(word[-1])  # 'n'
# (отрицательный индекс -1 указывает на последний элемент)

# Список — это последовательность элементов
# (могут быть разные типы данных).
# Индексы также начинаются с 0.

# fruits = ['яблоко', 'банан', 'вишня']
# print(fruits[0])  # 'яблоко'
# print(fruits[1])  # 'банан'
# print(fruits[-1])  # 'вишня'

# Пример 2: Изменение элементов списка с помощью индексов
# numbers = [10, 20, 30, 40, 50]
# numbers[1] = 25
# print(numbers)  # [10, 25, 30, 40, 50]

# Индексы в многомерных списках
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# print(matrix[0][0])  # 1 (первый элемент первой строки)
# print(matrix[1][2])  # 6 (третий элемент второй строки)
# print(matrix[2][1])  # 8 (второй элемент третьей строки)

# Срезы (slices)
# Индексы также используются для создания срезов
# (подпоследовательностей) из списка или строки.
# Пример: Срезы строк
# word = 'Python'
# print(word[0:2])  # 'Py' (символы с индекса 0 до 2, не включая 2)
# print(word[2:])   # 'thon' (символы с индекса 2 до конца)
# print(word[:2])   # 'Py' (символы от начала до индекса 2, не включая 2)
# print(word[-2:])  # 'on' (последние два символа)

# Пример: Срезы списков
# numbers = [10, 20, 30, 40, 50]
# print(numbers[1:3])  # [20, 30] (элементы с индекса 1 до 3, не включая 3)
# print(numbers[:3])   # [10, 20, 30] (первые три элемента)
# print(numbers[3:])   # [40, 50] (элементы с индекса 3 до конца)
# print(numbers[-2:])  # [40, 50] (последние два элемента)

# word = 'Python'
#
# print(word.index('o'))

# rus = 'йцукенгшщзхъфывапролджэячсмитьбю'
# eng = 'qwertyuiop[]asdfghjkl;\'zxcvbnm,.'
#
# print(len(rus), len(eng))
#
# while True:
#     word = input('\nВведите слово: ')
#     for letter in word:
#         if letter in rus:
#             print(eng[rus.index(letter)], end='')
#         else:
#             print(rus[eng.index(letter)], end='')

# enter_text = 'ghbdtn'

# for letter in enter_text:
