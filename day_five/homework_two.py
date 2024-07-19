
# Домашнее задание (5) вторая часть

# Дан кортеж состоящий из номеров и кодов:
# data = (
#     "O!", "Megacom", "0705", "Beeline", "0550",
#     "0770", "Katel", "0510", "Fonex", "0543"
# )
# 1 ) Создать два пустых списка designations и codes
# 2 ) Пройтись циклом for по кортежу data, добавить наименования
#     компаний в designations и коды в codes
# 3 ) Создать словарь operators на основе списков designations
#     и codes c помощью цикла while или встроенных функций
#     dict() и zip() , где ключами будут названия компаний
#     а значениями коды содержащиеся в множестве.
# 4 ) Удалить нефункционирующие операторы
#     из словаря operators. (Katel, Fonex)
# 5 ) Добавить/Обновить к уже существующим номерам
#     (Ошке, Меге и Билайну) пару кодов на своё усмотрение.
# 6 ) В итоге вывести на экран наименования операторов и
#     соответствующие номера в таком виде (в паре ключ-значение):

# (() => {
#     O! - {'0705', '0700', '0500'}
#     MegaCom - {'0550', '0999', '0555'}
#     Beeline - {'0770', '0222', '0777'}
# })

data = (
    "O!", "Megacom", "0705", "Beeline", "0550",
    "0770", "Katel", "0510", "Fonex", "0543"
)

designations = []
codes = []

[codes.append(i) if i.isdigit() else designations.append(i) for i in data]

operators = {key: {value} for key, value in zip(designations, codes)}

del operators['Katel']
del operators['Fonex']

operators['Megacom'].add('0700')
operators['Megacom'].add('0500')
operators['O!'].add('0999')
operators['O!'].add('0555')
operators['Beeline'].add('0222')
operators['Beeline'].add('0777')

for key, value in operators.items():
    print(f'{key}: {value}')
