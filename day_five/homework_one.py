
# Домашнее задание (5) первая часть

GeekTech = {
    'address': 'Toktogula 175',
    'courses': ['Fronted', 'Backend', 'IOS', 'Android', 'QA', 'UX/UI', 'PM'],
    'bag': {'fail', 'error', 'stack'}
}

# 1 ) Удалить баг
del GeekTech['bag']

# 2 ) Изменить адресс на нынешний
GeekTech['address'] = 'Имбраимова что-то'

# 3 ) Добавить номер телефона и инстаграмм аккаунт Гиктека
GeekTech['phone_number'] = '+996557820078'
GeekTech['account'] = '@geeks_edu'

# 4 ) Добавить/Расширить список актуальных курсами,
# которые вы знаете. Затем преобразовать этот список в set
new_courses = ['data syns', '1c', 'devops']
GeekTech['courses'].extend(new_courses)
GeekTech['courses'] = set(GeekTech.get('courses'))

# 5 ) Вывести словарь на экран с помощью цикла
# for с получением всех пар "ключ": значение
for key, value in GeekTech.items():
    print(f'{key}: {value}')
