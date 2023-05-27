'''Решить задачи, которые не успели решить на семинаре.
Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
В результирующем списке не должно быть дубликатов.'''
import collections
from collections import Counter
print('-'*20, 'Test 2', '-'*20)
list_test = [1,1,2,3,3,4,5,6,6,3,7,8,8,9]
list_dup_1 = set([x for x in list_test if list_test.count(x) > 1])
list_dup_2 = [x for x,k in Counter(list_test).items() if k > 1]
print(list_test)
print(list(list_dup_1))
print(list_dup_2)

# -------------- Test 3 --------------------
print('-'*20, 'Test 3', '-'*20)
'''В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых. 
Не учитывать знаки препинания и регистр символов. За основу возьмите любую статью из википедии 
или из документации к языку.'''

text = 'В большой текстовой, строке подсчитать Ц;количество встречаемых% слов и: вернуть 10 самых частых. ' \
       'Не учитывать знаки препинания и регистр символов. За основу" возьмите , ,? любую статью из википедии ' \
       'или из документации к языку.'
text_low = text.lower()
# print(text_low)
import string

text_clear = text_low.translate(str.maketrans('', '', string.punctuation))
# print(text_clear)
text_list = text_clear.split(' ',)

text_list_dict = (Counter(text_list).items())

top_10_worlds = sorted(text_list_dict, key=lambda x: x[1], reverse=True)[:5]
# print(top_10_worlds)
out = [x for x,y in top_10_worlds ]
print(out)

# -------------- Test 4 --------------------
print('-'*20, 'Test 4', '-'*20)
''' Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения. 
Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
 Достаточно вернуть один допустимый вариант. 
 *Верните все возможные варианты комплектации рюкзака.'''

dict_thing = {'вещь_1':1, 'вещь_2':3,'вещь_3':4,'вещь_4':0.5,'вещь_5':2,'вещь_6':6,'вещь_7':2,'вещь_8':2,'вещь_9':1}
max_weight = 12

sorted_dict = sorted(dict_thing.items(), key=lambda x: x[1])
complect = []
# print(sorted_dict)
# print(len(sorted_dict))
weight_compl = 0
step = 0

while (weight_compl + sorted_dict[step][1] <= max_weight) and (step <= (len(sorted_dict) - 1)):
    # print(sorted_dict[step])
    step += 1
    weight_compl += sorted_dict[step][1]
    # print(weight_compl)
    complect.append(sorted_dict[step][0])
print(f'Масса вещей = {weight_compl}')
print(f'В рюкзаке будет: {", ".join(complect)} ')

