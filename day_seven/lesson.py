# lambda, и работа с исключениями
# lambda arguments: expression
# map, filter

# lambda_function = lambda a, b: a + b


# def up_letter(word):
#     return word.title()


# def last_up(word):
#     return word[:-1] + word[-1].title()


# def show_words(function, sequence):
#
#     for i in sequence:
#         print(function(i))


# words = ('oop', 'python', 'django')
# show_words(lambda word: word[:-1] + word[-1].title(), words)
# show_words(lambda word: word.title(), ('oop', 'django', 'python'))
# show_words(lambda )


# print(type(lambda_function))
# print(type(up_letter))


# show_words(up_letter, 'python')
# show_words(len, ['geektech', 'kgz', 'bishkek'])

# lambda_function = lambda a, b: a + b


# def def_function(a, b):
#     return a + b


# print(lambda_function(2, 3))
# print(def_function(2, 3))

# numbers = list(range(1, 11))
# new_tuple = tuple(filter(lambda x: x < 5, numbers))
# new_set = set(filter(lambda x: x < 5, numbers))
# new_list = list(map(lambda num: num * 3, numbers))
# new_list = [i * 3 for i in numbers]
# new1 = sorted(numbers, key=lambda x: x % 2 == 0)
# new2 = sorted(numbers, key=lambda x: x % 2 != 0)
# new3 = sorted(numbers, key=lambda x: x % 2 != 0, reverse=True)
# print(new1)
# print(new2)
# print(new3)
# print(numbers, new_list, sep='\n')
# print(new_tuple)
# print(new_set)

# print('python'[99])  # IndexError
# print(10 / 0)  # ZeroDivisionError: division by zero
# print(a)  # NameError

# try:
#     print(int('23'))
# except:
#     # message, define smth
#     print('Неверный тип данных')
# finally:
#     # mesage
#     print('finally')
# number = int(input('Enter number: '))


# def test_try():
#     try:
#         number = int(input('Enter number: '))
#         print(number)
#     except ValueError:
#         print('error')
#
#     print('after try')
#
#
# test_try()

word = 'python'

while True:
    try:
        user_index = int(input('index: '))
        print(word[user_index])
    except ValueError:
        print('ValueError')
    except IndexError:
        print('IndexError')
