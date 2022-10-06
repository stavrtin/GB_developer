import csv
import json

def destroy_txt(txt_str):
    '''разложу текстовый файл на списки имя-фамил-тел-описание'''

    name = txt_str.split('\n')[::4]
    last_name = txt_str.split('\n')[1::4]
    tel_name = txt_str.split('\n')[2::4]
    text_name = txt_str.split('\n')[3::4]
    # print(name, last_name, tel_name, text_name)
    txt_list = [name, last_name, tel_name, text_name]
    return txt_list


def create_dict_book(txt_list):
    '''делаю словарь из списка данных полученных из тхт'''

    dict_list_txt = []
    for item in range(len(txt_list[0]) - 1):
        dict_txt = dict(zip(["Имя", "Фамилия", "Тел", "Описание"], [txt_list[0][item], txt_list[1][item], txt_list[2][item], txt_list[3][item]]))
        dict_list_txt.append(dict_txt)
    return dict_list_txt


def create_csv_file(txt_list):
    '''соберем csv из списков '''

    with open("tel_book.csv", mode="w", encoding='utf-8') as w_file:
        file_writer = csv.writer(w_file, delimiter=";", lineterminator="\r")
        file_writer.writerow(["Имя", "Фамилия", "Тел", "Описание"])
        for item in range(len(txt_list[0]) - 1):
            print(txt_list[0][item],txt_list[1][item],txt_list[2][item],txt_list[3][item])
            file_writer.writerow([txt_list[0][item],txt_list[1][item],txt_list[2][item],txt_list[3][item]])

def create_json_file(txt_dict):
    '''соберем json из списков '''

    with open('tel_book.json', 'w', encoding='utf-8') as f_json:  # открываем файл на запись
        json.dump(txt_dict, f_json, ensure_ascii=False)

def open_book_txt():
    with open('tel_book.txt', 'r', encoding='utf8') as f:
        text = f.read()
    return text

def create_new_record(data):
    name = data[0]
    lastname = data[1]
    tel = data[2]
    prof = data[3]
    with open('tel_book.txt', 'a', encoding='utf8') as f:
        f.writelines(name)
        f.writelines('\n')
        f.writelines(lastname)
        f.writelines('\n')
        f.writelines(tel)
        f.writelines('\n')
        f.writelines(prof)
        f.writelines('\n')
    return

