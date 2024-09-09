# Домашнее задание ( 2 )

# Написать программу знаков зодиака.
# Программа должна запрашивать у пользователя
# день и месяц рождения, затем выводить на экран
# соответствующий знак зодиака.
# В случае неправильного ввода, вывести на экран подсказку.

# (0.04, 32.05, 0 апреля, 32 мая)
# считается неправильно введенной датой!


day = int(input('Введите день рождения: '))
month = int(input('Введите месяц рождения: '))


class Months:
    January = 1
    February = 2
    March = 3
    April = 4
    May = 5
    July = 6
    June = 7
    August = 8
    September = 9
    October = 10
    November = 11
    December = 12


class DaysCountInMonth:
    January = 31
    February = 29
    March = 31
    April = 30
    May = 31
    July = 31
    June = 30
    August = 31
    September = 30
    October = 31
    November = 30
    December = 31


class ZodiacNames:
    Aquarius = 'Водолей'
    Pisces = 'Рыбы'
    Aries = 'Овен'
    Taurus = 'Телец'
    Gemini = 'Близнецы'
    Cancer = 'Рак'
    Leo = 'Лев'
    Virgo = 'Дева'
    Libra = 'Весы'
    Scorpio = 'Скорпион'
    Sagittarius = 'Стрелец'
    Capricorn = 'Козерог'


class RangeOfDaysOfZodiacSigns:
    Aquarius = (  # Водолей
            month == Months.January
            and 20 <= day <= DaysCountInMonth.January
            or month == Months.February
            and day <= 18
    )
    Pisces = (  # Рыбы
            month == Months.February
            and 19 <= day <= DaysCountInMonth.February
            or month == Months.March
            and day <= 20
    )
    Aries = (  # Овен
            month == Months.March
            and 21 <= day <= DaysCountInMonth.March
            or month == Months.April
            and day <= 19
    )
    Taurus = (  # Телец
            month == Months.April
            and 20 <= day <= DaysCountInMonth.April
            or month == Months.May
            and day <= 20
    )
    Gemini = (  # Близнецы
            month == Months.May
            and 21 <= day <= DaysCountInMonth.May
            or month == Months.June
            and day <= 20
    )
    Cancer = (  # Рак
            month == Months.June
            and 21 <= day <= DaysCountInMonth.June
            or month == Months.July
            and day <= 22
    )
    Leo = (  # Лев
            month == Months.July
            and 23 <= day <= DaysCountInMonth.July
            or month == Months.August
            and day <= 22
    )
    Virgo = (  # Дева
            month == Months.August
            and 23 <= day <= DaysCountInMonth.August
            or month == Months.September
            and day <= 22
    )
    Libra = (  # Весы
            month == Months.September
            and 23 <= day <= DaysCountInMonth.September
            or month == Months.October
            and day <= 22
    )
    Scorpio = (  # Скорпион
            month == Months.October
            and 23 <= day <= DaysCountInMonth.October
            or month == Months.November
            and day <= 21
    )
    Sagittarius = (  # Стрелец
            month == Months.November
            and 22 <= day <= DaysCountInMonth.November
            or month == Months.December
            and day <= 21
    )
    Capricorn = (  # Козерог
            month == Months.December
            and 22 <= day <= DaysCountInMonth.December
            or month == Months.January
            and day <= 19
    )


if day > 0 and month > 0 and isinstance(day, int) and isinstance(month, int):
    if RangeOfDaysOfZodiacSigns.Aquarius:
        print(ZodiacNames.Aquarius)
    elif RangeOfDaysOfZodiacSigns.Pisces:
        print(ZodiacNames.Pisces)
    elif RangeOfDaysOfZodiacSigns.Aries:
        print(ZodiacNames.Aries)
    elif RangeOfDaysOfZodiacSigns.Taurus:
        print(ZodiacNames.Taurus)
    elif RangeOfDaysOfZodiacSigns.Gemini:
        print(ZodiacNames.Gemini)
    elif RangeOfDaysOfZodiacSigns.Cancer:
        print(ZodiacNames.Cancer)
    elif RangeOfDaysOfZodiacSigns.Leo:
        print(ZodiacNames.Leo)
    elif RangeOfDaysOfZodiacSigns.Virgo:
        print(ZodiacNames.Virgo)
    elif RangeOfDaysOfZodiacSigns.Libra:
        print(ZodiacNames.Libra)
    elif RangeOfDaysOfZodiacSigns.Scorpio:
        print(ZodiacNames.Scorpio)
    elif RangeOfDaysOfZodiacSigns.Sagittarius:
        print(ZodiacNames.Sagittarius)
    elif RangeOfDaysOfZodiacSigns.Capricorn:
        print(ZodiacNames.Capricorn)
    else:
        print('Вы ввели не корректную дату')
else:
    print('Не коректная дата')

