
def show_main_menu():
    '''главное меню'''
    main_menu = {1: 'Открыть записную',
                 2: 'Добавить запись',
                 3: 'Удалить запись',
                 4: 'Редактировать запись',
                 5: 'Сохранить записную',
                 6: 'Найти запись',
                 7: 'Выход'
                  }
    for key, value in main_menu.items():
        print(f'{key} - {value}')
    while True:
        try:
            item_menu = int(input("Выберите пункт работы с записной >>   "))
            if item_menu not in main_menu:
                raise Exception
            return item_menu
        except Exception:
            print('Ошибка ввода. Введите правильное значение ')

    return item_menu

def sub_menu_save():
    '''подменю сохранения в выбранный формат'''

    main_menu = {1: 'Сохранить в .txt',
                 2: 'Сохранить в .csv',
                 3: 'Сохранить в .json',
                 4: 'Вернуться в предыдущее меню'
                  }
    for key, value in main_menu.items():
        print(f'{key} - {value}')
    while True:
        try:
            item_menu = int(input("Выберите формат сохранения записной >>   "))
            if item_menu not in main_menu:
                raise Exception
            return item_menu
        except Exception:
            print('Ошибка ввода. Введите правильное значение ')

    return item_menu


def sub_menu_open():
    '''подменю сохранения в выбранный формат'''

    main_menu = {1: 'Открыть из .txt',
                 2: 'Открыть из .csv',
                 3: 'Открыть из .json',
                 4: 'Вернуться в предыдущее меню'
                  }
    for key, value in main_menu.items():
        print(f'{key} - {value}')
    while True:
        try:
            item_menu = int(input("Выберите формат открытия записной >>   "))
            if item_menu not in main_menu:
                raise Exception
            return item_menu
        except Exception:
            print('Ошибка ввода. Введите правильное значение ')

    return item_menu


def show_book_txt():
    print('Выводим книгу в тхт - формате')
    with open('tel_book.txt', 'r', encoding='utf8') as f:
        text = f.read()
    print(text)


def show_book_csv():
    print('Выводим книгу в csv - формате')
    with open('tel_book.csv', 'r', encoding='utf8') as f:
        text = f.read()
    print(text)

def show_book_json():
    print('Выводим книгу в json - формате')
    with open('tel_book.json', 'r', encoding='utf8') as f:
        text = f.read()
    print(text)

def message_convert_to_json():
    print('Экспортируем книгу в json формат')

def message_convert_to_csv():
    print('Экспортируем книгу в csv формат')

def input_new_record():
    imput = (input('Выведите через пробел: фамилию - имя - тел - должность >>  '))
    new_record = [imput.split()[0], imput.split()[1], imput.split()[2], imput.split()[3]]
    return new_record

def input_new_record_completed():
    print('Запись добавлена')