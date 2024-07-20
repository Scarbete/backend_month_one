# Функции, аргумента (параметры): *args, **kwargs.

# width = 6
# length = 8
# square_2 = width * length
# print(square_2)

# width = 8.5
# length = 20
# square_hall = width * length
# print(square_hall)

# def - definition (определение функции)

# def greet(name, surname='Surname'):  # name - объязательный позиционный параметр
#     print(f'name: {name}, surname: {surname}')


# 'Kutman' - объязательный позиционный аргумент
# greet('Kutman', 'Nurlanov')
# greet('Aesthetic', 'CODM')
# greet('Yardix')
# greet('Surname', 'Name')
# greet('Surname', 'Name')

# Именованные аргументы (keyword args)
# greet(surname='Surname', name='Name')

# greet with input
# greet(name=input('Укажите имя: '), surname=input('Фамилия: '))

# print(len('123') + 5)  # len('123') Уже является числом


# def my_len(iterable):
#     count = 0
#
#     for _ in iterable:
#         count += 1
#
#     return count


# print(my_len('python') + 5)
# print(my_len([1, 2, 3, 4, 5, 6]) + 5)


# def get_area(width: int or float, length: int or float) -> int or float:
#     """
#     Принимает ширину и длину, возравщает площадь.
#     :param width:
#     :param length:
#     :return int:
#     """
#     return width * length


# print(get_area.__doc__)
# print(help(get_area))
# print(help(str))
# print(help(int))
# square_one = get_area(width=6, length=8)
# square_two = get_area(width=8.6, length=20)
# print(square_one, square_two, sep='\n')


# def my_min(seq):
#     return sorted(seq)[0]
#
#
# def my_max(seq):
#     return sorted(seq)[-1]
#
#
# print(my_min([1, 4, 5, 7, 0.5, 20]))  # list
# print(my_min((1, 4, 5, 7, 0.5, 20)))  # tuple
# print(my_max([1, 4, 5, 7, 0.5, 20]))  # list
# print(my_max((1, 4, 5, 7, 0.5, 20)))  # tuple


# def plus(*args , a, b=1):  # Bad
# def plus(a, *args, b=1):  # Bad
# def plus(a, b=1, *args):
#     print('a', a)
#     print('b', b)
#     print('args', args)
#     print('args[0]', args[0])
#     print('args[-1]', args[-1])
#     print('sorted sorted args', sorted(args))
#     print('sorted reverse args', sorted(args, reverse=True))
#     return sum(args) / a


# print(plus(10, 5, 5, 5, 5, 5, 5, 5, 5, 20, 35))
# print(plus(_, _, _))

# def menu(a, **kwargs):  # Good
# def menu(a, b, **kwargs):  # Good
# def menu(**kwargs, a, b):  # Bad

# def menu(**kwargs):
#     return kwargs  # return dict


# def sum_with_kwargs(**kwargs):
#     return sum(kwargs.values())


# print(menu(name='Kutman', age=20, hobby=['programming', 'sport']))
# print(sum_with_kwargs(a=5, b=10, c=20, d=15))

# def test_args_kwargs(*args, **kwargs):

student_rates = {
    'Aesthetic': 2,
    'Yardix': 3,
    'Quasar': 4,
    'LevivUp': 5
}

print('student_rates', student_rates)
# CRUD


# CREATE


def find_student(name: str) -> bool:
    """
    :param name:
    :return bool:
    """
    return name in student_rates.keys()


def is_correct_rate(rate: int) -> bool:
    """
    :param rate:
    :return bool:
    """
    return 5 >= rate >= 1


def add(name: str, rate: int) -> None:
    """
    :param name:
    :param rate:
    :return:
    """
    if not find_student(name):
        if is_correct_rate(rate):
            student_rates[name] = rate
        else:
            print(f'{name} rate\'s: {rate} is uncorrect! (1-5)')
    else:
        print(f'Name {name} is in student rates!')


# DELETE
def delete(name: str) -> None:
    """
    :param name:
    :return:
    """
    if find_student(name):
        del student_rates[name]
    else:
        print(f'{name} is not in student_rates')


add(name='Kutman', rate=10)  # error
add(name='Kutman2', rate=-1)  # error
add(name='Kutman3', rate=11)  # error
add(name='Kutman4', rate=5)  # good
add(name='LevivUp', rate=10)  # error
print('student_rates', student_rates)

delete('Kutman1')  # error
delete('Kutman2')  # error
delete('Kutman4')  # good
delete('LevivUp')  # good
delete('Quasar')  # good
print('student_rates', student_rates)


# UPDATE
def update(name: str, new_name) -> None:
    """
    :param name:
    :param new_name:
    :return:
    """
    if name in student_rates.keys():
        student_rates[new_name] = student_rates.pop(name)
        # student_rates[new_name] = student_rates[name]
        # del student_rates[name]
    else:
        print(f'{name} is not in student_rates')


update('Aesthetic', 'New_Aesthetic')
print('student_rates', student_rates)


def sycle_crud_with_students():
    while True:
        print(student_rates)

        command = input(
            f'1 ) add\n'
            f'2 ) edit\n'
            f'3 ) delete\n'
            f'4 ) mid sum\nEnter: '
        )

        if command == '1':
            add(name=input('Введите имя: '), rate=int(input('Введите оценку: ')))
        elif command == '2':
            update(name=input('Введите имя: '), new_name=input('Введите новое имя: '))
        elif command == '3':
            delete(name=input('Введите имя: '))
        elif command == '4':
            result = sum(student_rates.values()) / len(student_rates.keys())
            print(f'Средняя сумма: {round(result, 2)}')
        elif command == 'stop':
            break
        else:
            print('Выбирайте из списка!')


sycle_crud_with_students()

# DRY - don't repeat yourself
