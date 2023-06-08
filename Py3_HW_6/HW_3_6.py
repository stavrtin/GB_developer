'''Урок 6. Модули

В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.

Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите код, решающий задачу о 8 ферзях.
Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга. Вам дана расстановка
8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга. Программа получает на вход восемь пар чисел,
 каждое число от 1 до 8 - координаты 8 ферзей. Если ферзи не бьют друг друга верните истину, а если бьют - ложь.

Напишите функцию в шахматный модуль. Используйте генератор случайных чисел для случайной расстановки ферзей
в задаче выше. Проверяйте различный случайные варианты и выведите 4 успешных расстановки.'''

from ask_chislo import ask_task
# ------------- урок 6  ------------- t1
from random import randint as rand
#
# d = rand(1, 5)
# print(d)

# ------------- урок 6  ------------- t2
'''Создайте модуль с функцией внутри.
� Функция принимает на вход три целых числа:
нижнюю и верхнюю границу и количество попыток.
� Внутри генерируется случайное число в указанных
границах и пользователь должен угадать его за
заданное число попыток.
� Функция выводит подсказки “больше” и “меньше”.
� Если число угадано, возвращается истина, а если
попытки исчерпаны - ложь.'''

# from ask_chislo import ask_task
#
# if __name__ == '__main__':
#     ask_task(1,5,2)
#

'''Задание №3
� Улучшаем задачу 2
� Добавьте возможность запуска функции “угадайки”
из модуля в командной строке терминала.
� Строка должна принимать от 1 до 3 аргументов:
параметры вызова функции.
� Для преобразования строковых аргументов
командной строки в числовые параметры
используйте генераторное выражение.'''

# from sys import argv
#
# if __name__ == '__main__':
#     ask_task(*(int(i) for i in argv[1:]))

'''Задание №4
� Создайте модуль с функцией внутри.
� Функция получает на вход загадку, список с
возможными вариантами отгадок и количество
попыток на угадывание.
� Программа возвращает номер попытки, с которой
была отгадана загадка или ноль, если попытки
исчерпаны.'''


'''Задание №7
Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
Для простоты договоримся, что год может быть в диапазоне [1, 9999]. 
Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь. 
Проверку года на високосность вынести в отдельную защищённую функцию.
'''


# -----------------------------HW - task 1 ------------------------------------------------
'''В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.'''

from data_module import check_data_view
from sys import argv


if __name__ == '__main__':
    # test = input('Введите год в виде DD.MM.YYYY ==> ')
    check_data_view(argv[1])

# -----------------------------HW - task 2 ------------------------------------------------
'''Добавьте в пакет, созданный на семинаре шахматный модуль. 
Внутри него напишите код, решающий задачу о 8 ферзях.
Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга. 
Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга. 
Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей. 
Если ферзи не бьют друг друга верните истину, а если бьют - ложь.

Напишите функцию в шахматный модуль. 
Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше. 
Проверяйте различный случайные  варианты и выведите 4 успешных расстановки.
'''

'''Добавьте в пакет, созданный на семинаре шахматный модуль.
Внутри него напишите код, решающий задачу о 8 ферзях.
Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.
Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
Если ферзи не бьют друг друга верните истину, а если бьют - ложь.'''

from random import randint
import random


def create_position():
    simbol = random.choice(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', ])
    digit = random.choice(['1', '2', '3', '4', '5', '6', '7', '8', ])
    position = simbol + digit
    # print(position)
    return position


def gen_positions():
    eigth_ferz_list = [create_position()]

    while len(eigth_ferz_list) < 9:
        new_position = create_position()
        if new_position not in eigth_ferz_list:
            eigth_ferz_list.append(new_position)
    return eigth_ferz_list


def gen_broken_field(position: str) -> list:
    simbol_ = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', ]
    digit_ = ['1', '2', '3', '4', '5', '6', '7', '8', ]
    horisont_, vertic_ = list(position)

    broken_field_h = [horisont_ + i for i in digit_ if i != vertic_]
    broken_field_v = [i + vertic_  for i in simbol_ if i != horisont_]

    result =   broken_field_h +  broken_field_v

    return result


def add(x, y):
    return list(map(lambda a, b: a + b, x, y))

def test_hor_vert(variant_position: list) -> bool:
    result = True

    return result


variant_position = gen_positions()

a, b = list(variant_position[1])

print(variant_position)
print(variant_position[1])
print(a, b)

print(gen_broken_field(variant_position[1]))





# step = simbol_.index(a) + 1

def levo_niz(position_ferz):
    simbol_ = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', ]
    digit_ = ['1', '2', '3', '4', '5', '6', '7', '8', ]
    digit_poz, simbol_poz = list(position_ferz)
    # --- срез внизлево---
    spisok_ostavsh_cifr_ = digit_[:int(simbol_poz) - 1]
    spisok_ostavsh_simb_ = simbol_[:simbol_.index(digit_poz)]
    # print(spisok_ostavsh_cifr_)
    # print(spisok_ostavsh_simb_)
    # print('---')

    if len(spisok_ostavsh_cifr_) < len(spisok_ostavsh_simb_):
    #     -----режем цифры иначе - буквы
        new_simb = (spisok_ostavsh_simb_[-len(spisok_ostavsh_cifr_):])
        new_cif = (spisok_ostavsh_cifr_)

    else:
        new_cif = (spisok_ostavsh_cifr_[-len(spisok_ostavsh_simb_):])
        new_simb = (spisok_ostavsh_simb_)

    if len(spisok_ostavsh_simb_) != 0 and len(spisok_ostavsh_cifr_) !=0:
    # --- склеить два списка----
        print(new_simb)
        print(new_cif)
        result_ln = add(new_simb, new_cif)

    else: result_ln = []

    return result_ln

def pravo_niz(position_ferz):
    simbol_ = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', ]
    digit_ = ['1', '2', '3', '4', '5', '6', '7', '8', ]
    digit_poz, simbol_poz = list(position_ferz)
    # --- срез внизлево---
    spisok_ostavsh_cifr_ = digit_[:int(simbol_poz) - 1]
    spisok_ostavsh_simb_ = simbol_[:simbol_.index(digit_poz)]
    # print(spisok_ostavsh_cifr_)
    # print(spisok_ostavsh_simb_)
    # print('---')

    if len(spisok_ostavsh_cifr_) < len(spisok_ostavsh_simb_):
    #     -----режем цифры иначе - буквы
        new_simb = (spisok_ostavsh_simb_[-len(spisok_ostavsh_cifr_):])
        new_cif = (spisok_ostavsh_cifr_)

    else:
        new_cif = (spisok_ostavsh_cifr_[-len(spisok_ostavsh_simb_):])
        new_simb = (spisok_ostavsh_simb_)

    if len(spisok_ostavsh_simb_) != 0 and len(spisok_ostavsh_cifr_) !=0:
    # --- склеить два списка----
        print(new_simb)
        print(new_cif)
        result_ln = add(new_simb, new_cif)

    else: result_ln = []

    return result_ln


print(levo_niz(variant_position[1]))
print('ssssssssssssssssss')

simbol_ = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', ]
digit_ = ['1', '2', '3', '4', '5', '6', '7', '8', ]
digit_poz, simbol_poz = list(variant_position[1])
# --- срез внизлево---
spisok_ostavsh_cifr_pr_niz = digit_[:int(simbol_poz) - 1]
spisok_ostavsh_simb_ = simbol_[:simbol_.index(digit_poz)]
# print(spisok_ostavsh_cifr_)
# print(spisok_ostavsh_simb_)
# print('---')

if len(spisok_ostavsh_cifr_) < len(spisok_ostavsh_simb_):
    #     -----режем цифры иначе - буквы
    new_simb = (spisok_ostavsh_simb_[-len(spisok_ostavsh_cifr_):])
    new_cif = (spisok_ostavsh_cifr_)

else:
    new_cif = (spisok_ostavsh_cifr_[-len(spisok_ostavsh_simb_):])
    new_simb = (spisok_ostavsh_simb_)

if len(spisok_ostavsh_simb_) != 0 and len(spisok_ostavsh_cifr_) != 0:
    # --- склеить два списка----
    print(new_simb)
    print(new_cif)
    result_ln = add(new_simb, new_cif)

else:
    result_ln = []