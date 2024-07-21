from typing import Union, List, Tuple


def nearest_number(
    sequence: (Union[List[Union[int, float]], Tuple[Union[int, float], ...]]),
    target: Union[int, float] = 0
) -> Tuple[Union[int, float], List[Union[int, float]]]:
    """_summary_
    The function takes a list/tuple and an integer or fractional 
    number and returns a tuple where the first element is the 
    target number and then a list sorted by an algorithm that 
    will first give numbers that are closer in absolute value to target

    Args:
        sequence ( List[int, float], Tuple[int, float], ... ): _description_
        target ( [int, float], optional): _description_. Defaults to 0.

    Returns:
        Tuple[ int, float, List[int, float] ]: _description_
    """
    nearest_arr = sorted(sequence, key=lambda x: abs(x - target))
    return target, nearest_arr


print(nearest_number(sequence=[312, 996, 31, 1991], target=1000))
# result: (1000, [996, 312, 31, 1991])

print(nearest_number(sequence=[5, 20.18, 103, 4], target=27))
# result: (27, [20.18, 5, 4, 103])


def retrieve_element(iterable: Union[List, Tuple, str]):
    """_summary_
    The function takes an iterable object as the first parameter, 
    and executes an endless loop where it will request the index 
    of the element and will output it to the console; if there are errors, 
    the loop will not stop, but will show the cause of the error and will continue to work, 
    it is also possible to exit the loop by entering the text exit in input()
    
    Args:
        iterable (Union[List, Tuple, str]): _description_
    """
    while True:
        command = input('Введите индекс элемента: ')
        if command.lower() == 'exit':
            print('Выход из программы')
            break
        try:
            index = int(command)
            print('Результат:', iterable[index])
        except IndexError:
            last_index = len(iterable) - 1
            print(f'Результат: Неверный индекс. Укажите индекс от 0 до {last_index}.')
        except ValueError:
            print('Не корректное значение!')


# my_list = [10, 20, 30, 40, 50]
# retrieve_element(my_list)

my_list = [10, 20, 30, 40, 50, 20, 30, 25, 15, 10, 5]

# Пример использования map для возведения чисел в квадрат
numbers_square = list(map(lambda num: num * num, my_list))
print('numbers_square:', numbers_square)

# Пример использования filter для получения четных чисел
even_nums = list(filter(lambda num: num % 2 == 0, my_list))
print('even_nums:', even_nums)

# Пример использования filter для получения нечетных чисел
odd_nums = list(filter(lambda num: num % 2 != 0, my_list))
print('odd_nums:', odd_nums)
