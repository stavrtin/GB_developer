# ------------------------------------------------- 2---------------
# class User:
#     def __init__(self, name: str, equipm: list = None):
#         self.name = name
#         self.equipment = equipm if equipm is not None else []
#         self.life = 3
#
#         print(f'Создан юнит {self.name}, c оборудованием {self.equipment} и жизнями {self.life}')
#
#
# u1 = User("Вася", ['luk','strela'])
# u2 = User("Petiya", ['dubina','noj'])
# ------------------------------------------------- 2---------------
class User:
    def __init__(self, name: str):
        '''Это - документация'''
        self.name = name
        print(f'Создан юнит {self.name = }')

    def __new__(cls, *args, **kwargs):
        isinstance = super().__new__(cls)
        print(f'Создан class {cls}')
        return isinstance

# print('Первый раз')
# u1 = User('Вася')
# print('2q раз')
# u2 = User('Petyia')
# print('3q раз')
# u3 = User('Seva')
# -------------------------3----------------
class NamedInt(int):
    def __new__(cls, value, name):
        instance = super().__new__(cls, value)
        instance.name = name
        print(f'Создал класс {cls}')
        return instance

# a = NamedInt(2, 'типа что-то расширеено')
# b = NamedInt(3, 'расширеено')
# c = a + b
# print(f'{a} и {a.name = }')
# print(f'{b} и {b.name = }')
# print(f'{c} ')
# ------------------------------- документация -------------------
# u11 = User('Ivan')
# print(u11.__doc__)
# help(u11)
# --------------------------------- переопределение --------------
class Vector():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Vector ({self.x}, {self.y})'

    # def __str__(self):
    #     return f'vector ({self.x = } {self.y = })'

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x,y)


# a = Vector(-2,3)
# b = Vector(4,5)
# c = a + b
# print(f'{a = } + {b = } \t {c = }')

# -----------------------------сравнение ---------------
class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        return f'Треугольник со сторонами: {self.a}, {self.b}, {self.c}'

    def __eq__(self, other):
        first = sorted((self.a, self.b, self.c))
        second = sorted((other.a, other.b, other.c))
        return first == second

one = Triangle(3, 4, 5)
two = one
three = Triangle(3, 4, 5)
four = Triangle(4, 3, 5)
print(f'{one == two   = }')
print(f'{one == three = }')
print(f'{one == four  = }')
print(f'{one != one   = }')