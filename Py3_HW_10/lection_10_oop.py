# data1 = [1,2,3]
# print(data1)
# print(f'{data1 = }, {type(data1) = },  {type(list) = }')
#
# import random
# import sup_mod
# result1 = random.randint(1, 10)
# result2 = sup_mod.randint(42)
# print(f'{result1 = }')
# print(f'{result2 = }')

class Person:
    __max_up = 3
    _max_level = 80

    def __init__(self, name, race = 'unknown', speed=100):
        self.name = name
        self.race = race
        self.level = 1
        self.health = 100
        self._speed = speed
        self.up = 3

    def _check_level(self):
        return self.level < self._max_level

    def level_up(self):
        if self._check_level():
            self.level += 1
        else:
            self.level = self._max_level

    def change_health(self, other, quentity):
        self.health += quentity
        other.health -= quentity


    def add_up(self):
        self.up += 1
        self.up = min(self.up, self.__max_up)

class Hero(Person):
    def __init__(self, power, *args, **kwargs):
        self.power = power
        super().__init__(*args, **kwargs) # --- для подключения конструктора РОДИТЕЛЯ

    def change_health(self, other, quentity):
        self.health += quentity * 2
        other.health -= quentity * 2

    def add_many_up(self):
        self.up += 1
        self.up = min(self.up, self._Person__max_up * 3)


# p1 = Person('Вася', 'Эльф', 120)
# print(f'{p1.up = }')
# p1.up = 1
# print(f'{p1.up = }')
# for _ in range(5):
#     p1.add_up()
#     print(f'{p1.up = }')

p1 = Hero('archery', 'Вася', '"Elph', 120)
p2 = Person('Маг', 'Troll')

print(f'{p1.health = }, {p2.health = }')
p1.change_health(p2, 10)
print(f'{p1.health = }, {p2.health = }')
p2.change_health(p1, 10)
print(f'{p1.health = }, {p2.health = }')

p1.add_many_up()
print(f'{p1.up = }')