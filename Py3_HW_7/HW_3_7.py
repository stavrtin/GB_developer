'''find all files'''
'''
    принимать параметр желаемое конечное имя файлов. При переименовании в конце
     имени добавляется порядковый номер.
    принимать параметр количество цифр в порядковом номере.
    принимать параметр расширение исходного файла. Переименование должно работать 
    только для этих файлов внутри каталога.
    принимать параметр расширение конечного файла.
    принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] 
    берутся буквы с 3 по 6 из исходного имени файла. 
    К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.
'''
import os


# ---- получаем сведения о папке (2й параметр - список файлов)
def create_file_name(path, new_name, max_digit, old_extention, new_extention, part_of_old_file_name):
    '''преобразовываем файлы в новый вид'''

    path = path
    new_part = new_name
    number_of_digits = max_digit
    find_extention = old_extention
    new_file_extension = new_extention
    range_of_old_name = part_of_old_file_name

    max_len_zero = '0000000000'

    extention_list = [i for i in path][0][2]

    # ----------------------список только нужных файлов по расширению ----------------
    find_files = [i for i in extention_list if i.split('.')[1] == find_extention]
    # print(find_files)

    # ----------------------------------- выковырнем часть имени -----
    start_split_old_name = range_of_old_name[0]
    end_split_old_name = range_of_old_name[1]
    part_name_old_files = [i.split('.')[0][start_split_old_name:end_split_old_name] for i in find_files]
    # print(part_name_old_files)

    # -----------------присоединяем новый кусок имени ------------

    new_name_files = [i + '_' + new_part + '.' + new_file_extension for i in part_name_old_files]
    # print(new_name_files)

    # --------------- присоединим цифровую часть -----------

    new_digit_part = max_len_zero[:number_of_digits]
    new_name_files_list = []

    for i in enumerate(new_name_files):
        new_name_files_list.append(
            i[1].split('.')[0] + '_' + str(new_digit_part[:-len(str(i[0]))]) + str(i[0]) + '.' + i[1].split('.')[1])

    # print(new_name_files_list)
    return find_files, new_name_files_list

path_file = 'c:\\Users\\stavr\\Virt_envar\\Virt_envar\\Scripts\\12_Programms\\pythonProject_GB_3\\HW_3_7'
path_name = os.walk(path_file)
new_part = 'nor'
number_of_digits = 5
find_extention = 'psi'
new_file_extension = 'txt'
range_of_old_name = [1, 7]

list_names = create_file_name(path_name, new_part, number_of_digits, find_extention, new_file_extension, range_of_old_name)

# print(list_names)

# os.rename(list_names[0], list_names[2])
for i in range(len(list_names[0])):
    os.rename(path_file + '\\' +  list_names[0][i], path_file + '\\' + list_names[1][i])