'''Задание №1
📌 Создайте класс Моя Строка, где:
📌 будут доступны все возможности str
📌 дополнительно хранятся имя автора строки и время создания (time.time)'''
from time import time

class MyStr(str):
    '''Это - документация КЛАССА'''
    def __new__(cls, value: str, name: str,):
        '''Расширяем метод new параметрами value & name'''
        instance = super().__new__(cls, value)
        instance.name = name
        instance.created_at = time()
        return instance

    def __init__(self, value, dop = None):
        self.value = value

    def __str__(self):
        '''Это- документация метода'''
        return f'Это - экземпляр {self.value}'

# if __name__ == '__main__':
#     mystr = MyStr('Строка', "Что-то дополнительно")
#     print(mystr)
#     print(mystr.created_at)
#     print(mystr.name)

'''Задание №2
📌 Создайте класс Архив, который хранит пару свойств. Например, число и строку. 
📌 При нового экземпляра класса, старые данные из ранее созданных экземпляров сохраняются в пару списков-
архивов
📌 list-архивы также являются свойствами экземпляра '''


class Archive:

    numbers = []
    values  = []

    def __new__(cls, number: int, value: str):
        instance = super().__new__(cls)
        cls.numbers.append(number)
        cls.values.append(value)
        return instance

    def __init__(self, number: int, value: str):
        self.number = number
        self.value = value

    def __str__(self):
        '''Это- документация метода'''
        return f' Номер: {self.number = } Значен: {self.value} '

    def __repr__(self):
        '''Это- документация метода'''
        return f'Archiv({self.number}, {self.value})'


# if __name__ == '__main__':
#     my_arch1 = Archive(1, 'nhe-kz-kz')
#     my_arch2 = Archive(2, 'sadasd-asdadz-asdz')
#     my_arch3 = Archive(33, '33-333-333')
#     my_arch4 = Archive(444, '4444444444444')
#     print(f'{my_arch1.numbers} {my_arch1.values}')
#     # print(f'{my_arch2.numbers} {my_arch2.values}')
#     print(my_arch1)
#     print(my_arch1.__repr__())
#     print(my_arch4.__repr__())
#     print(f'{my_arch3 = }')


'''Задание №3
📌 Добавьте к задачам 1 и 2 строки документации для классов.'''

'''Задание №4
📌 Доработаем класс Архив из задачи 2. 
📌 Добавьте методы представления экземпляра для программиста и для пользователя.'''

'''Задание №5
📌 Дорабатываем класс прямоугольник из прошлого семинара.
📌 Добавьте возможность сложения и вычитания. 
📌 При этом должен создаваться новый экземпляр прямоугольника. 
📌 Складываем и вычитаем периметры, а не длинну и ширину.
📌 При вычитании не допускайте отрицательных значений.'''

class Rangler:

    def __init__(self, length: int, winght: int = None):
        self.length = length
        self.winght = length if winght is None else winght

    def perim(self) -> int:
        return 2 * (self.length + self.winght)

    def squer(self) -> int:
        return self.length * self.winght

    def __add__(self, other):
        new_perim = self.perim() + other.perim()
        new_a = self.length
        new_b = new_perim / 2 - new_a
        return Rangler(new_a, new_b)

    def __sub__(self, other):
        new_perim = abs(self.perim() - other.perim())
        new_a = min([self.length, other.length, self.winght, other.winght])
        new_b = new_perim / 2 - new_a
        return Rangler(new_a, new_b)

    def __str__(self):
        return f'{self.length}, {self.winght} , {self.perim()}'


# if __name__ == '__main__':
#     rang1 = Rangler(2,4)
#     rang2 = Rangler(1,3)
#     print(f'{rang1.perim() = }, {rang1.squer() = }')
#     print(f'{rang2.perim() = }, {rang2.squer() = }')
#     rang3 = rang2 - rang1
#     print(rang3)




'''Добавьте ко всем задачам с семинара строки документации и методы вывода информации на печать.
Создайте класс Матрица. Добавьте методы для:
вывода на печать,
сравнения,
сложения,
*умножения матриц'''

class Matrix:

    def __init__(self, a_matrix: list[list[int, float]]):
        self._rows = len(a_matrix)
        self._cols = len(a_matrix[0])
        self._a_matrix = a_matrix

    def __add__(self, other):
        new_matrix = [[0 for _ in range(self._cols)] for _ in range(self._rows)]
        for j in range(self._rows):
            for i in range(self._cols):
                new_matrix[j][i] = self._a_matrix[j][i] + other._a_matrix[j][i]
        return Matrix(new_matrix)


    def __eq__(self, other) :
        for j in range(self._rows):
            for i in range(self._cols):
                if self._a_matrix[j][i] != other._a_matrix[j][i]:
                    return False
        return True


    def __str__(self) -> str:
        return '\n'.join(['\t'.join(map(str, row)) for row in self._a_matrix]) + '\n'



if __name__ == '__main__':
    matr_a = Matrix([[5, 3], [1, 2], [6,  1]])
    # matr_b = Matrix([[3, 6], [4, 1], [5,  9]])
    matr_b = Matrix([[10, 6], [7, 5], [3, 1]])
    matr_c = Matrix([[10, 6], [7, 5], [3, 1]])

    print(matr_a)
    print(matr_b)
    print(matr_c)

    print(f'{matr_a == matr_b = }')
    print(f'{matr_a == matr_b = }')
    print(f'{matr_b == matr_c = }')
    print(matr_a + matr_b)
    print(matr_a + matr_c)

