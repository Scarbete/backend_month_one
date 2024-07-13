# Написать программу для вычисления расходов за неделю.

#  - Расход каждого дня недели должен вводиться пользователем
#    по запросу программы (input), на каждый отдельный день
#    должна быть отдельная переменная.

#  - Вывести общую сумму расходов.

#  - Вывести средний расход в день. (средний расход должен быть
#    в дробном числе, округленным с одной цифрой после точки.)

# import functools - В данный файл импортируется functools

print('Введите расходы для каждого дня недели: ')

monday = float(input('Понедельник: '))
tuesday = float(input('Вторник: '))
wednesday = float(input('Среда: '))
thursday = float(input('Четверг: '))
friday = float(input('Пятница: '))
saturday = float(input('Суббота: '))
sunday = float(input('Воскресенье: '))

all_days_in_week = [monday, tuesday, wednesday, thursday, friday, saturday, sunday]

# у functools вызываем готовый и облегченный метод reduce
# Она делает следующее: создает lambda функцию
# и с параметрами a, b возвращяет результат вычисления a+b
# каждый раз итерируясь по массиву all_days_in_week
# таким образом мы достигаем результата общей суммы расходов
# total_expenses = functools.reduce(lambda a, b: a+b, all_days_in_week)

# А это уже облегченный (прямолинейный) метод получения общей суммы
total_expenses = monday + tuesday + wednesday + thursday + friday + saturday + sunday

print('total_expenses', total_expenses)

days_in_week_count = 7

average_daily_expense = total_expenses / days_in_week_count

print(f'Общая сумма расходов за неделю: {total_expenses}')
# ( :.1f ) - гарантирует, что число будет
# отформатировано с одной цифрой после точки.
print(f'Средний расход в день: {average_daily_expense:.1f}')
