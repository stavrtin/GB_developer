# -------------- Test 4.1 --------------------
print('-'*20, 'Test 4.1', '-'*20)
'''Напишите функцию для транспонирования матрицы.'''
def transporation(table):
    table2 = []

    for i in range(len(table[0])):
        table2.append(list())
        for j in range(len(table)):
            table2[i].append(table[j][i])
    return table2

matrix = [[1, 2, 3], [4, 5, 6]]
print(matrix)
matrix2 = transporation(matrix)
print(matrix2)

# -------------- Test 4.2 --------------------
print('-'*20, 'Test 4.2', '-'*20)
'''Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, где ключ 
- значение переданного аргумента, а значение - имя аргумента. Если ключ не хешируем,
 используйте его строковое представление.'''

def dictunary(a=2, b=3):
    dictun = {
        f'{a}': id(a),
        f'{b}': id(b)
    }

    return dictun
a = 2
b = 3
temp = dictunary(a, b)
print(temp)

