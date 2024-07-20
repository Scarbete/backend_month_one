
contacts = [
    {'name': 'Geektech', 'phone': '0507052018'},
    {'name': 'Служба спасения', 'phone': '911'},
    {'name': 'Пожарная служба', 'phone': '101'},
]


def display_contacts():
    print('\nСписок контактов:')

    for contact in contacts:
        name = contact['name']
        phone = contact['phone']
        print(f'Имя: {name}, Телефон: {phone}')


def create() -> None:
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
    global contacts
    name = input('Введите имя: ')

    for contact in contacts:
        if contact['name'] == name:
            contacts.remove(contact)
            print(f'Контакт {name} удален')
            return

    print(f'Контакт {name} не был найден.')


def main():
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
