

import math
import csv
from random import randint
from typing import Callable


def create_csv_file():
    with open("outer_file.csv", mode="w", encoding='utf-8') as w_file:
        file_writer = csv.writer(w_file, delimiter = ";", lineterminator="\r")
        for i in range(10):
            a = randint(-50, 50)
            b = randint(-50, 50)
            c = randint(-50, 50)
            file_writer.writerow([a, b, c])


# Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
# -- читаем из файла
# -- решаем
# --- записываем в строку


def deco_csv(func: Callable):
    create_csv_file()

    res_list = []
    def wrapper(*args):
        res_dict = {}
        with open('outer_file.csv', newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
            for row in spamreader:
                res = func(int(row[0]),int(row[1]), int(row[2]))
                res_dict[str(row)] = res
                res_list.append(res_dict)
        return res_list

    return wrapper


@deco_csv
def root_squar_equat(*args):
    a, b, c = args
    disc = b ** 2 - 4 * a * c
    if disc > 0:
        x1 = (-b + math.sqrt(disc)) / (2 * a)
        x2 = (-b - math.sqrt(disc)) / (2 * a)
        return round(x1, 2), round(x2, 2)
    elif disc == 0:
        x = -b / (2 * a)
        return round(x, 2)




print(root_squar_equat())


