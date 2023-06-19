phone_book = {}
path: str = 'phones.txt'


def open_file():
    phone_book.clear()
    file = open(path, 'r', encoding='UTF-8')
    data = file.readlines()
    file.close()
    for contact in data:
        nc = contact.strip().split(':')
        phone_book[int(nc[0])] = {'name': nc[1], 'phone': nc[2], 'comment': nc[3]}
    sorted(phone_book.items())
    print('\nТелефонный справочник успешно загружен!')
    print('=' * 200 + '\n')


def save_file():
    data = []
    for i, contact in phone_book.items():
        new = ':'.join([str(i), contact.get('name'), contact.get('phone'), contact.get('comment')])
        data.append(new)
    data = '\n'.join(data)
    with open(path, 'w', encoding='UTF-8') as file:
        file.write(data)
    print('\nТелефонная книга успешно сохранена!')
    print('=' * 200 + '\n')


def show_contacts(book: dict[int, dict]):
    print('\n' + '=' * 200)
    for i, cnt in book.items():
        print(f"{i:>3}: {cnt.get('name'):<20}{cnt.get('phone'):<20}{cnt.get('comment'):<20}")
    print('=' * 200 + '\n')


def menu() -> int:
    main_menu = '''Главное меню:
    1. Открыть файл
    2. Сохранить файл
    3. Показать все контакты
    4. Создать контакт
    5. Найти контакт
    6. Изменить контакт
    7. Удалить контакт
    8. Выход'''
    print(main_menu)
    while True:
        select = input('Выберите пункт меню: ')
        if select.isdigit() and 0 < int(select) < 9:
            return int(select)
        print('Введите число в контексте меню')
        print('=' * 200 + '\n')


def add_contact():
    uid = max(list(phone_book.keys())) + 1
    name = input('Введите имя контакта: ')
    phone = input('Введите телефон контакта: ')
    comment = input('Введите комментарий к контакту: ')
    phone_book[uid] = {'name': name, 'phone': phone, 'comment': comment}
    print(f'\nКонтакт {name} успешно добавлен в книгу!')
    print('=' * 200 + '/n')


def search():
    result = {}
    word = input('Введите слово по которому будет осуществляться поиск: ')
    for i, cnt in phone_book.items():
        if word.lower() in ''.join(list(cnt.values())).lower():
            result[i] = cnt
    return result


print('=' * 200 + '\n')


def change_contact():  # добавил 6 пункт (изменение контакта в телефонной книги)
    show_contacts(phone_book)
    usr_id = int(input('Введите id контакта, который необходимо изменить: '))
    if usr_id in phone_book:
        phone_book[usr_id]['name'] = input('Введите имя: ')
        phone_book[usr_id]['phone'] = input('Введите номер телефона: ')
        phone_book[usr_id]['comment'] = input('Введите комментарий: ')
    else:
        print('Контакт с указанным id не найден.')
    print('\nКонтакт успешно изменён!')


print('=' * 200 + '\n')


def delete_contact():  # добавил 7 пункт (удаление из телефонной книги)
    show_contacts(phone_book)
    usr_id = int(input('Введите id контакта, который необходимо удалить: '))
    if usr_id in phone_book:
        phone_book.pop(usr_id)
        print('\nКонтакт успешно удален!')
    else:
        print('Такого id нет в справочнике')


print('=' * 200 + '\n')


def menu() -> int:
    main_menu = '''Главное меню:
    1. Открыть файл
    2. Сохранить файл
    3. Показать все контакты
    4. Создать контакт
    5. Найти контакт
    6. Изменить контакт
    7. Удалить контакт
    8. Выход'''
    print(main_menu)
    while True:
        select = input('Выберите пункт меню: ')
        if select.isdigit() and 0 < int(select) < 9:
            return int(select)
        print('Введите число в контексте меню')


open_file()
while True:
    select = menu()
    match select:
        case 1:
            open_file()
        case 2:
            save_file()
        case 3:
            show_contacts(phone_book)
        case 4:
            add_contact()
        case 5:
            result = search()
            show_contacts(result)
        case 6:
            change_contact()
        case 7:
            delete_contact()
        case 8:
            print('До свидания! До новых встреч!')
            break
print('*' * 200 + ' \n ')
