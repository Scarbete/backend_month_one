from typing import Union, List, Tuple


def even_or_odd(number: int) -> Union[bool, None]:
    """
    Функция берет целое число и возращает True если оно четное в противном случае False,
    иначе если передать в аргументы что-то кроме числа то функция возращает None
    :param number: Целое число которое мы проверяем на четное или не четное
    :return: (bool, None) если число четное то True иначе False если будет не число то None
    """
    return number % 2 == 0 if isinstance(number, int) else None


# print(even_or_odd(number=4))  # True
# print(even_or_odd(number=3))  # False
# print(even_or_odd(number='str'))  # None


def spelling(description: str) -> bool:
    """
    Функция берет параметр (description) и возращает True если в начале
    предложения буква начинается с Заглавной и в конце заканчивается с точкой
    :param description: описание (предложение которое мы проверяем на корректность)
    :return: bool: возращается True если преложение корректное иначе False
    """
    return description[0].isupper() and description.endswith('.')


# print(spelling(description='Корректное значение.'))  # True
# print(spelling(description='OK.'))  # True
# print(spelling(description='Не корретный текст без точки'))  # False
# print(spelling(description='не корретный текст без заглавной буквы в начале предложения.'))  # False


def calculator(
    num_one: Union[int, float],
    operator: str,
    num_two: Union[int, float]
) -> None:
    """
    Функция берет первое, второе число и оператор и возвращает результат операции
    в зависимости какой оператор в Python был выбран и если будет деление на 0 будет ошибка
    и также если ввести не корректный оператор также будет ошибка.
    Есть словарь operations в котором lambda функции которые нужны для операции,
    в переменной result мы берем из словаря функцию и вызываем его передав ему аргументы,
    таким образом в result будет храниться результат вычисления либо текст ошибки,
    дальше идет условие если result это целое или дробное число то показываем в консоли корректный текст,
    иначе отображаем текст самой ошибки
    :param num_one: первое число
    :param operator: оператор, именно по нему мы будем определятся какое значение нужно давать
    :param num_two: второе число
    :return: None
    """
    try:
        # try - Это механизм обработки с которым мы обрачиваем код который
        # нужно проверить, если там будет ошибка то сработает expect
        zero_error = 'Ошибка: деление на ноль'

        # lambda - это лямбда-функция. Лямбда-функции в Python — это небольшие анонимные
        # функции, которые определяются с помощью ключевого слова lambda.
        operations = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: a / b if b != 0 else zero_error,
            '**': lambda a, b: a ** b,
            '//': lambda a, b: a // b if b != 0 else zero_error,
            '%': lambda a, b: a // b if b != 0 else zero_error,
        }

        if operator in operations:
            result = operations[operator](num_one, num_two)

            if isinstance(result, (int, float)):
                print(f'{num_one} {operator} {num_two} = {result}')
            else:
                print(result)

        else:
            print('Ошибка: не корректный оператор!')
    except ZeroDivisionError:
        # ZeroDivisionError - Это встроенная штука в Python которое
        # возникает когда происходит попытка деления на 0
        print('Ошибка: деление на ноль!')


# Корректные значения
# calculator(num_one=5, operator='+', num_two=10)
# calculator(num_one=10, operator='-', num_two=5.5)
# calculator(num_one=20.5, operator='*', num_two=2)
# calculator(num_one=5, operator='/', num_two=10)
# calculator(num_one=5.25, operator='**', num_two=2)
# calculator(num_one=10, operator='//', num_two=3)
# calculator(num_one=5, operator='%', num_two=10)

# Не корректные значения
# calculator(num_one=20, operator='/', num_two=0)  # Ошибка: деление на ноль!
# calculator(num_one=20, operator='@', num_two=0)  # Ошибка: деление на ноль!
# calculator(num_one=20, operator='%', num_two=0)  # Ошибка: деление на ноль!
# calculator(num_one=20, operator='@', num_two=20)  # Ошибка: не корректный оператор!


def nearest_number(
    sequence: (
        Union[
            List[Union[int, float]],
            Tuple[Union[int, float], ...]
        ]
    ),
    target: Union[int, float] = 0
) -> Union[int, float]:
    """
    Функция первым позиционным параметром берет массив (список либо кортеж),
    который состоит из целых или дробных чисел и вторым параметром берет
    целое либо дробное число которое по умолчания имеет значение 0,
    затем возвращает самое близкое число исходя из массива (списка, кортеж) sequence
    :param sequence: список или кортеж из целых или дробных чисел
    :param target: целое или дробное число, по умолчанию 0
    :return: возвращает самое близкое число к target исходя из массива sequence
    """
    return min(sequence, key=lambda x: abs(x - target))
    #  - Как это работает

    # abs - как я понял это встроенная функция в Python которое возрващает
    #       какое-то абсолютное значение (это его расстояние от нуля на числовой оси)

    # (x - target) - вычисление разницы между элементом (x из массива sequence) c числом target
    #       [  abs(x - target)  ] - возвращает значение которое указывает на
    #       разницу между значением (x) и target

    #  - Использование key в min:

    # Когда мы вызываем min с параметром key, функция min находит
    # элемент с миниамльным значением, возвращаемым функцией key
    # а функция key в свою очередь применяется для каждого
    # элемента при итерации по массиву (списку, кортежу)

    # Пример
    # Допустим, у нас есть последовательность
    # [5, 20.18, 103, 4] и целевое число 27:
    #
    # Для элемента 5:
    #
    # Разница: 5 - 27 = -22
    # Абсолютное значение: abs(-22) = 22

    # Таким образом у нас будет массив из Абсолютных значений
    # и какой из них минимальный то показываем то самое число
    # на котором мы применяли key функцию.

    # Именно так вычисляется самое близкое число из массива sequence к target


# print(nearest_number([5, 20.18, 103, 4], 27))
# print(nearest_number((312, 996, 31, 1991), 1000))
# print(nearest_number((312, 996, 31, 1991)))
