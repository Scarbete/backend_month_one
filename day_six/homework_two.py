
contacts = [
    {'name': 'Geektech', 'phone': '0507052018'},
    {'name': 'Служба спасения', 'phone': '911'},
    {'name': 'Пожарная служба', 'phone': '101'},
]


def display_contacts() -> None:
    """
    Функция предназначенная для отображении полной информации о контактах
    :return: None
    """
    print('\nСписок контактов:')

    for contact in contacts:
        name = contact['name']
        phone = contact['phone']
        print(f'Имя: {name}, Телефон: {phone}')


def create() -> None:
    """
    Функция для добавления (создание) нового контакта
    с помощью функции input() запрашивается новое имя и номер телефона
    дальше происходит поиск на существующего контакта если оно есть то обновляется номер телефона
    иначе если с такими значениями из input() не нашлось контакта то создается новый контакт
    и он добавляется в список контактов
    :return: None
    """
    new_name = input('Введите имя нового контакта: ')
    new_phone = input('Введите номер телефона: ')

    for contact in contacts:
        if contact['name'] == new_name:
            contact['name'] = new_phone
            print(f'Номер телефона ({new_name}) обновлен.')
            return

    contacts.append(dict(name=new_name, phone=new_phone))
    print(f'Контакт {new_name} добавлен.')


def update() -> None:
    """
    Функция для обновления данных контакта.
    С помощью input() запрашивается имя контакта которую нужно обновить, новое имя и номер телефона
    дальше происходит поиск по контактам по значению old_name, если контакт найден,
    то дальше идет поиск по контактам, с значениями из input() new_name, new_phone
    если такой контакт есть выводиться print() что данный контакт существует,
    иначе если по таким новым значениям ( new_name, new_phone ) все свободно,
    то обновляется контакт по ключу old_name в списке контактов (contacts)
    :return: None
    """
    old_name = input('Введите старое имя: ')
    new_name = input('Введите новое имя: ')
    new_phone = input('Введите номер телефона: ')

    for contact in contacts:
        if contact['name'] == old_name:
            for contact_for_new in contacts:
                if contact_for_new['name'] == new_name or contact_for_new['phone'] == new_phone:
                    print(f'С такими новыми данными уже есть контакт: {new_name}, {new_phone}')
                    return

            contact['name'] = new_name
            contact['phone'] = new_phone
            print(f'Контакт {old_name} обновлен на: name={new_name}, phone={new_phone}')
            return


def delete():
    """
    Функция берет глобальный объект contacts,
    затем запрашивает имя контакта для поиска и удаления.
    если такие данные есть в списке contacts оно удаляется,
    иначе если контакт не был найдет выводиться print(),
    то что контакт не был найден.
    :return: None
    """
    global contacts
    name = input('Введите имя: ')

    for contact in contacts:
        if contact['name'] == name:
            contacts.remove(contact)
            print(f'Контакт {name} удален')
            return

    print(f'Контакт {name} не был найден.')


def main() -> None:
    """
    Функция запускает бесконечный цикл, каждый раз выводиться информация о списке contacts,
    Дальше в print() указывается какие команды есть для выбора действий CRUD,
    с помощью input() запрашивается команда в консоли, есть словарь contacts_crud,
    в котором ключи это название команд из print('commands'),
    а значения это ссылки на функции CRUD для списка contacts,
    дальше идет условие если команда из input() есть в словаре contacts_crud,
    то мы берем фукнцию и вызываем его, иначе если командой будет (exit) то остановится цикл,
    иначе если команда введена не правильно то выводиться print() с указанием ошибки
    :return:
    """
    while True:
        display_contacts()
        print('\nКоманды: (create), (update), (delete), (exit)')
        command = input('Введите команду: ').strip().lower()

        contacts_crud = {
            'create': create,
            'update': update,
            'delete': delete,
        }

        if command in contacts_crud.keys():
            contacts_crud[command]()
        elif command == 'exit':
            print('Выход из программы.')
            break
        else:
            print('Не корректная команда!')


main()
