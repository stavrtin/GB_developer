'''Задание №1
📌 Создайте класс окружность.
📌 Класс должен принимать радиус окружности при создании экземпляра.
📌 У класса должно быть два метода, возвращающие длину окружности и её площадь.'''

# ----------------Task_1 --------------------------
from math import pi


class Circle:

    def __init__(self, radius):
        self.radius = radius

    def lenth_circl(self):
        return 2 * pi * self.radius

    def squer_circl(self):
        return pi * self.radius * self.radius


'''Задание №2
📌 Создайте класс прямоугольник. 
📌 Класс должен принимать длину и ширину при создании экземпляра. 
📌 У класса должно быть два метода, возвращающие периметр и площадь. 
📌 Если при создании экземпляра передаётся только одна сторона, считаем что у нас квадрат.'''


class Rangler:

    def __init__(self, length: int, winght: int = None):
        self.length = length
        self.winght = length if winght is None else winght

    def perim(self) -> int:
        return 2 * (self.length + self.winght)

    def squer(self) -> int:
        return self.length * self.winght


# if __name__ == '__main__':
#     rang = Rangler(4)
#     print(f'{rang.perim() = }, {rang.squer() = }')

'''Задание №3
📌 Напишите класс для хранения информации о человеке: ФИО, возраст и т.п. на ваш выбор. 
📌 У класса должны быть методы birthday для увеличения возраста на год, full_name для вывода полного ФИО и т.п. на 
ваш выбор. 
📌 Убедитесь, что свойство возраст недоступно для прямого изменения, но есть возможность получить текущий возраст.'''


class Human:

    def __init__(self, first_name: str, last_name: str, age: int, gender: str):
        self.first_name = first_name
        self.last_name = last_name
        self.__age = age
        self.gender = gender

    def get_age(self):
        return self.__age

    def birthday(self):
        self.__age += 1
        return self.__age

    def full_name(self):
        print(f'{self.first_name} {self.last_name} ')

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.get_age()} {self.gender} '


# if __name__ == '__main__':
#     fio1 = Human('Петя','Иванов', 21,'м')
#     fio2 = Human('Kate','Pet', 24,'fem')
#     fio3 = Human('Jak','Shirak', 56,'m')
#     print(fio1)
#     print(fio2)
#     print(fio3)
#     fio1.birthday()
#     fio2.birthday()
#     fio1.birthday()
#     print(fio1)
#     print(fio2)
#     print(fio3)

'''Задание №4
📌 Создайте класс Сотрудник. 
📌 Воспользуйтесь классом человека из прошлого задания. 
📌 У сотрудника должен быть:
○ шестизначный идентификационный номер
○ уровень доступа вычисляемый как остаток от деления суммы цифр id на семь '''

from random import  randint
import typing

class Sotrudnik(Human):

    def __init__(self, first_name: str, last_name: str, age: int, gender: str, prof: str):
        self.prof = prof
        self.id = self._get_id()
        self.level = self._secr_level()
        super().__init__(first_name, last_name, age, gender)

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.get_age()} {self.gender}  {self.prof} {self.id}  {self.level} '

    def _get_id(self)-> int:
        MIN_ID = 100000
        MAX_ID = 1000000
        return randint(MIN_ID, MAX_ID)

    def _secr_level(self)-> int:
        id = self._get_id()
        sum = 0
        for i in list(str(id)):
            sum += int(i)
        res_level = sum % 7
        return res_level


# if __name__ == '__main__':
#     fio_sotr1 = Sotrudnik('Петя','Иванов', 21,'м', 'povar')
#     fio_sotr2 = Sotrudnik('Kate','Pet', 24,'fem', 'strip')
#     fio_sotr3 = Sotrudnik('Jak','Shirak', 56,'m', 'teacher')
#     print(fio_sotr1)
#     print(fio_sotr2)
#     print(fio_sotr3)

'''Задание №5
📌 Создайте три (или более) отдельных классов животных. Например рыбы, птицы и т.п. 
📌 У каждого класса должны быть как общие свойства, например имя, так и специфичные для класса. 
📌 Для каждого класса создайте метод, выводящий информацию специфичную для данного класса.
📌 Вынесите общие свойства и методы классов в класс Животное. 
📌 Остальные классы наследуйте от него. 
📌 Убедитесь, что в созданные ранее классы внесены правки.'''


class Animal:

    def __init__(self, name: str, weigth: int, age: int):
        self.name = name
        self.weigth = weigth
        self.age = age

    def __str__(self):
        return f'{self.name = }, {self.weigth = }, {self.age = }'

    def move(self):
        pass

    def say(self):
        pass


class Bird(Animal):

    def __init__(self, name: str, weigth: int, age: int, vid_bird:str, sound: str):
        super().__init__(name, weigth, age)
        self.vid_bird = vid_bird
        self.sound = sound

    def __str__(self):
        return f'{super().__str__() }, {self.vid_bird = }, {self.move() = }, {self.say() = }'

    def move(self):
        return "fly"

    def say(self):
        return self.sound


class Dog(Animal):

    def __init__(self, name: str, weigth: int, age: int, vid_dog:str):
        super().__init__(name, weigth, age)
        self.vid_dog = vid_dog

    def move(self):
        return "run"

    def say(self):
        return 'gav-gav'

    def __str__(self):
        return f'{super().__str__() }, {self.vid_dog = }, {self.move() = }, {self.say() = }'


class Fish(Animal):

    def __init__(self, name: str, weigth: int, age: int, vid_fish:str):
        super().__init__(name, weigth, age)
        self.vid_fish = vid_fish

    def move(self):
        return "swim"

    def say(self):
        return 'bul-bul'

    def __str__(self):
        return f'{super().__str__() }, {self.vid_fish = }, {self.move() = }, {self.say() = }'

# if __name__ == '__main__':
#     bird_solov = Bird('Соловей', 3, 5, 'соловейки', 'тру-ля-ля')
#     dog_shpic = Dog('Терьер', 30, 15, 'Tax')
#     fish_fish = Fish('Гупи', 0, 2, 'Карп')
#
#     print(bird_solov)
#     print(dog_shpic)
#     print(fish_fish)

'''📌 Решить задачи, которые не успели решить на семинаре.
📌 Доработаем задачи 5-6. Создайте класс-фабрику. 
○ Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа. 
○ Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.
📌 Возьмите 1-3 любые задачи из прошлых семинаров (например сериализация данных), которые вы уже решали.
Превратите функции в методы класса, а параметры в свойства. Задачи должны решаться через вызов методов экземпляра. '''

class Fabric:

    def make_animal(self, animal_type: str, *args, **kwargs):
        new_animal = self._get_maker(animal_type)
        return new_animal(*args, **kwargs)

    def _get_maker(self, animal_type: str):
        types = {"dog": Dog, "bird": Bird, "fish": Fish}
        return types[animal_type.lower()]


if __name__ == '__main__':
    fabric = Fabric()
    animal_from_fabric = fabric.make_animal('Bird', 'Соловей', 3, 5, 'соловейки', 'тру-ля-ля')
    print(animal_from_fabric)


print('--------------------------TASK 3----------------------------------')

'''Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
Программа должна возвращать сумму и произведение* дробей.
Для проверки своего кода используйте модуль fractions.'''


class Sum:

    def __init__(self, drob1: str, drob2:str):
        self.drob1 = drob1
        self.drob2 = drob2

    def translate_str_to_digit(self, str_drob: str):
        data_chislit = int(str_drob.split('/')[0])
        data_znamenat = int(str_drob.split('/')[1])
        return data_chislit, data_znamenat

    def data_sum(self, data1, data2):
        a_ch = self.translate_str_to_digit(data1)[0]
        a_zn = self.translate_str_to_digit(data1)[1]
        b_ch = self.translate_str_to_digit(data2)[0]
        b_zn = self.translate_str_to_digit(data2)[1]
        ch = a_ch * b_zn + b_ch * a_zn
        zn = b_zn * a_zn
        res = (ch, zn)
        return res

    def __str__(self):
        return f'{self.drob1} + {self.drob2} =  {self.data_sum(self.drob1, self.drob2)[0]}/{self.data_sum(self.drob1, self.drob2)[1]}'

class Multy:

    def __init__(self, drob1: str, drob2:str):
        self.drob1 = drob1
        self.drob2 = drob2

    def translate_str_to_digit(self, str_drob: str):
        data_chislit = int(str_drob.split('/')[0])
        data_znamenat = int(str_drob.split('/')[1])
        return data_chislit, data_znamenat

    def data_mult(self, data1, data2):
        a_ch = self.translate_str_to_digit(data1)[0]
        a_zn = self.translate_str_to_digit(data1)[1]
        b_ch = self.translate_str_to_digit(data2)[0]
        b_zn = self.translate_str_to_digit(data2)[1]
        res = (a_ch * b_ch, a_zn * b_zn)
        return res

    def __str__(self):
        return f'{self.drob1} * {self.drob2} =  {self.data_mult(self.drob1, self.drob2)[0]}/{self.data_mult(self.drob1, self.drob2)[1]}'



a = '3/5'
b = '4/5'

sum1 = Sum(a, b)
mult1 = Multy(a,b)
print(sum1)
print(mult1)