# Введение в Python: Встроенные функции, переменные, коментарии.
# Базовые типы данных: строки, целые и дробные числа.

# str - строка
name = 'Kutman'
# str - строка
surname = 'Nurlanov'
# int - число
age = 20

print('Hello World!')

print(name)
print(surname)
print(age)

print(type(name))
print(type(surname))
print(type(age))

lower_text = 'apple'

print('Hello', name, surname)

# str - метода
print(lower_text.title())
surname.upper()

print('Hello', name, surname)

# lower() - Преобразует все символы строки в нижний регистр
print(name.lower())

# upper() - Преобразует все символы строки в верхний регистр
print(name.upper())

# capitalize() - Делает первый символ строки заглавным,
# а все остальные символы - строчными.
test_text = 'O\'neil'
print(test_text.capitalize())

# title() - Делает заглавным первый символ каждого слова в строке
print('title', name.title())

# strip([chars]) - Удаляет пробелы (или указанные символы) в начале и конце строки
strip_test_text = '  123  Hello World!  123  '
# '123  Hello World!  123'
print('strip', strip_test_text.strip())

# lstrip([chars]) - Удаляет пробелы (или указанные символы) в начале строки.
lstrip_test_text = '   123 Hello world!   '
# '123 Hello world!   '
print('lstrip', lstrip_test_text.lstrip())

# rstrip([chars]) - Удаляет пробелы (или указанные символы) в конце строки.
rstrip_test_text = '  123  Hello World!  123  '
# '  123  Hello World!  123'
print('rstrip', rstrip_test_text.rstrip())

# split(sep=None, maxsplit=-1) - Разбивает строку на части
# по заданному разделителю. Возвращает список строк.
split_test_text = 'Hello World'
# ['Hello', 'World']
print('split', split_test_text.split())

# join(iterable) - Объединяет элементы итерируемого объекта
# в одну строку, используя текущую строку как разделитель
join_test_text = ['Hello', 'World']
# 'Hello World'
print('join', ' '.join(join_test_text))

# replace(old, new[, count]) - Заменяет все вхождения подстроки
# old на подстроку new. Можно указать количество замен.
replace_test_text = 'Hello, World!'
# "Hello, Python!"
# Находит слово World и заменяет его на Python
print('replace', replace_test_text.replace('World', 'Python'))

replace_test_name = 'Quasar'
print('replace_test_name (old)', replace_test_name)
new_replace_test_name = replace_test_name.replace('Quasar', 'Aesthetic')
print('replace_test_name (new)', replace_test_name)  # ('Quasar') Не изменяемый тип данных
print('new_replace_test_name', new_replace_test_name)

# find(sub[, start[, end]]) - Возвращает наименьший индекс, по которому
# подстрока sub найдена в строке. Возвращает -1, если подстрока не найдена.
find_test_text = 'Hello, World!'
print('find', find_test_text.find('World!'))  # 7

# count() - Возвращает количество неперекрывающихся
# вхождений подстроки sub в строке
print('31', name.count('a'))

# startswith(prefix[, start[, end]]) - Возвращает True,
# если строка начинается с подстроки prefix.
startswith_test_text = 'Hello, World!'
print('startswith', startswith_test_text.startswith('Hello'))  # True

# endswith(suffix[, start[, end]]) - Возвращает True, если
# строка заканчивается на подстроку suffix.
endswith_test_text = 'Hello, World!'
print('endswith', endswith_test_text.endswith('World!'))  # True

# работа с апостолами - Экранирование

# хорошо
test_name_1 = 'o\'neil'
test_name_2 = "o'neil"

print(test_name_1)
print(test_name_2)

# плохо
# test_name_3 = 'o'neil'

# Конкатенация строк
print(f'{name} {surname} {age}')

print('Hello,', name.title(), surname.title())

print('Hello, ' + name.title() + ' ' + surname.title())

print('2' + '3')

print(2 + 3)

print('Hello! {} {}'.format(name, surname))

# format - форматирование строки
print('My name is {}, i am {} years old'.format(name, age))

surname = 'O\'neil'

# f - format - форматирование строки
print(f'Hello! My name is {name.title()} {surname.capitalize()}, i am {age} years old!')

# Операции над тем что мы уже знаем
number1 = 10
numebr2 = 2
print('+', number1 + numebr2)
print('-', number1 - numebr2)
print('*', number1 * numebr2)
print('/', number1 / numebr2)  # result: 5.0
print('//', number1 // numebr2)  # result: 5 когда мы хотим число без дробей
print('**', number1 ** numebr2)  # Возведение в степень
print('%', number1 % numebr2)  # result: % 0
print(20 % 7)  # Остаток от деления
print(2 + 3 * 4)
print((2 + 3) * 4)  # () - Это приоритет (выражение)

test_num = 10
drob_num = 2.0  # float

print('type(test_num)', type(test_num))  # int
print('type(drob_num)', type(drob_num))  # float

print(test_num // drob_num)  # result: 5 потому что мы работаем с дробным числом

print(20 // 8)  # result: 2
print(20 / 8)  # result: 2.5

print('round', round(20 / 3, 1))  # Округление

# input - Строка в терминале в которую можно что либо ввести,
# он возвращяет нам строку
# my_name = input('Введите свое имя: ')
# my_surname = input('Введите свою фамилию: ')
# my_age = int(input('Введите свой возраст: '))  # int() - Явное преобразование типа
# current_year = 2024
#
# print(f'Hello {my_name.title()} {my_surname.title()} вы {current_year - my_age} года рождения!')

number_str1 = str(20)
number_str2 = str(20.0)
print(number_str1)
print(type(number_str1))

print(number_str1 + number_str2)

# Среднее арифметическое число
sum_ages = 20 + 18 + 16 + 14 + 13 + 32 + 23 \
           + 23 + 14 + 13 + 32 + 23 + 23 + 32

amunt_peoples = 14

average_age = sum_ages / amunt_peoples

print('Среднее арифметическое число', round(average_age, 2))
print('Среднее арифметическое число', int(average_age))


# по наитии поверхостно пробую другие темы в Python

# функции - также по code style нужно делать промежуток по 2 строки
def summing(num_one, num_two):
    print(f'Результат: {num_one + num_two}')


summing(2, 5)


# class
class Animal:

    def __init__(self, new_name, new_color):
        self.new_name = new_name
        self.new_color = new_color
        # self.__name = name  # Приватный атрибут

    def make_sound(self, sound):
        print(f'{self.new_name} make sound: {sound}')

    def get_name(self):
        return self.new_name

    def set_name(self, the_new_name):
        self.new_name = the_new_name


cat = Animal('Kami', 'Gray')
dog = Animal('Bobik', 'White')

cat.make_sound('meow')
cat.make_sound('bark')


class Cat(Animal):
    def make_sound(self, sound='meow'):
        return sound


new_cat = Cat('Kurama', 'Red')
print(new_cat.make_sound())


# калькулятор на class
class SumClass:

    def __init__(self):
        print('SumClass - инициализирован (создан)')

    # В Python, декоратор @staticmethod используется для
    # создания статических методов в классах.
    # Статический метод не зависит от состояния
    # объекта класса (экземпляра) и не имеет доступа
    # к атрибутам экземпляра (self) или класса (cls).
    # Он действует как обычная функция, но принадлежит
    # пространству имен класса, что позволяет организовать
    # код более логичным образом.

    @staticmethod
    def plus_two_nums(num_one, num_two):
        print('plus_two_nums', num_one + num_two)

    @staticmethod
    def sum_with_operation(num_one, num_two, operation):
        sum_result = 0

        if operation == '+':
            sum_result = num_one + num_two
        elif operation == '-':
            sum_result = num_one - num_two
        elif operation == '*':
            sum_result = num_one * num_two
        elif operation == '/':
            sum_result = num_one / num_two
        else:
            print('Вы не корректно ввели оперцию (+,-,*,/)')

        print(f'SumClass: {num_one} {operation} {num_two} = {sum_result}')


# Но также я могу использовать Static методы без создания самого экземпляра
SumClass.plus_two_nums(2, 3)
SumClass.sum_with_operation(40, 2, '/')

# Здесь мы сначала создаем наш экземпляр
sum_class = SumClass()
sum_class.plus_two_nums(20, 10)
sum_class.sum_with_operation(5, 5, '+')
sum_class.sum_with_operation(5, 5, '-')
sum_class.sum_with_operation(5, 5, '*')
sum_class.sum_with_operation(5, 5, '/')
sum_class.sum_with_operation(5, 5, '///')
