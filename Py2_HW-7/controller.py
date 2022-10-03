import view
import model
import logging
# logging.basicConfig(level=logging.DEBUG, filename='log.txt', filemode='a', format='%(asctime)s')
logging.basicConfig(level=logging.DEBUG, filename='log.txt', filemode='a', format='%(asctime)s - %(process)d-%(levelname)s-%(message)s')



def main_process():
    print('Поехали')

    user_select = view.show_main_menu()
    # print(user_select)
    if user_select == 1:
        # print(f'Выбран пункт =Открыть записную= ')
        logging.info(f"Выбран пункт {user_select}")
        open_file_select = view.sub_menu_open()
        if open_file_select == 1:
            # print(f'Открываем .txt')
            view.show_book_txt()
        elif open_file_select == 2:
            # print(f'Открываем .csv')
            view.show_book_csv()
        elif open_file_select == 3:
            # print(f'Открываем .json')
            view.show_book_json()
    elif user_select == 2:
        # print(f'Выбран пункт =Добавить запись= ')
        logging.info(f"Выбран пункт {user_select}")
    elif user_select == 3:
        print(f'Выбран пункт =Удалить запись= ')
    elif user_select == 4:
        print(f'Выбран пункт =Редактировать запись= ')
    elif user_select == 5:
        print(f'Выбран пункт =Сохранить записную= ')
        save_menu_select = view.sub_menu_save()
        if save_menu_select == 1:
            print(f'Сохраняем в .txt')

        elif save_menu_select == 2:
            # print(f'Сохраняем в .csv')
            view.message_convert_to_csv()
        #     --- в модель за преобразованием из текста в цсв
        #   открыть книгу тхт
            text = model.open_book_txt()
        #   конвертировать в нужный формат
            txt_list = model.destroy_txt(text)
            model.create_csv_file(txt_list)
        #     откроем экспортированный файл
            view.show_book_csv()

        elif save_menu_select == 3:
            # print(f'Сохраняем в .json')
            view.message_convert_to_json()
        #     --- в модель за преобразованием из текста в json
            text = model.open_book_txt()
            #   конвертировать в нужный формат
            txt_list = model.destroy_txt(text)
            txt_dict = model.create_dict_book(txt_list)
            model.create_json_file(txt_dict)
            #     откроем экспортированный файл
            view.show_book_json()
    elif user_select == 6:
        print(f'Выбран пункт =Найти запись= ')
    elif user_select == 7:
        exit()


