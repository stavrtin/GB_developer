'''
Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
Функцию hex используйте для проверки своего результата.
'''
print('--------------------------TASK 2----------------------------------')

def print_hex(a_input):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Вы ввели {a_input}\n')  # Press Ctrl+F8 to toggle the breakpoint.
    dict_hex = {10: 'A',
                11: 'B',
                12: 'C',
                13: 'D',
                14: 'E',
                15: 'F'}
    a = a_input
    list_a = []
    while (a // 16) > 0:
        ostatok = a % 16
        if ostatok > 9:
            list_a.insert(0, dict_hex[ostatok])
        else:
            list_a.insert(0, str(ostatok))
        a = a // 16
    list_a.insert(0,str(a))
    print(f'Число {a_input} в шестнатиричной системе => {("".join(list_a))}')
    print(f'Проверка: {a_input} в шестнатиричной системе => {hex(a_input)}')



a = -1
while a < 0 or a > 1000000:
    try:
        a = int(input('Введите a от 1 до 1000000 => '))
    except:
        print('Введите число')
print_hex(a)


print('--------------------------TASK 3----------------------------------')

'''Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
Программа должна возвращать сумму и произведение* дробей.
Для проверки своего кода используйте модуль fractions.'''


a = (input('Введите 1ю дробь в виде: "1/2" => '))
b = (input('Введите 2ю дробь в виде: "1/2" => '))

def trnslate(data):
    data_chislit = int(data.split('/')[0])
    data_znamenat = int(data.split('/')[1])
    return data_chislit, data_znamenat

def data_sum(a, b):
    a_ch = trnslate(a)[0]
    a_zn = trnslate(a)[1]
    b_ch = trnslate(b)[0]
    b_zn = trnslate(b)[1]

    # print(f'{a_ch * b_zn + b_ch * a_zn}/{b_zn * a_zn}')
    ch = a_ch * b_zn + b_ch * a_zn
    zn = b_zn * a_zn
    res = output(ch, zn)
    return res

def data_mult(a, b):
    a_ch = trnslate(a)[0]
    a_zn = trnslate(a)[1]
    b_ch = trnslate(b)[0]
    b_zn = trnslate(b)[1]

    # print(f'{a_ch * b_ch}/{a_zn * b_zn}')
    res = output(a_ch * b_ch, a_zn * b_zn)
    return res

def output(ch1,zn1):
    dd = f'{ch1}/{zn1}'
    return dd


print(f'{a} * {b} = {data_mult(a, b)}')
print(f'{a} + {b} = {data_sum(a, b)}')
