# *** кортеж из случайных чисел, мин и макс значение***

# import random
# arr = []
# i = 0
# while i < 10:
#     num = random.randrange(100)
#     arr.append(num)
#     i += 1
# tuple = tuple(arr)
# print(tuple)
# print(max(tuple))
# print(min(tuple))
# .......................
# import random
# tuple = tuple([random.randrange(100) for i in range(10)]) #генератор списка
# преобразовываем в кортеж
# # print(tuple)
# print(max(tuple))
# print(min(tuple))

# .......................

# import random
# tuple1 = tuple([random.randint(0, 5) for i in range(10)])
# tuple2 = tuple([random.randint(-5, 0) for i in range(10)])
# tuple3 = tuple1 + tuple2
# nul = tuple3.count(0)
# print(tuple3, nul)

# .......................

# tuple = (1, 's', 'd', 'f',)
# list = list(tuple)
# list = [str(i) for i in list]
# print(', '.join(list))

# .......................

# A = (13, 5, 43, 49, 67, 32, 12, 98, 6, 10, 34, 20, 55, 68, 14, 60, 14,)
# B = (53, 21, 4, 23, 76, 3, 43, 12, 54, 342, 21,)
# suma = 0
# sumb = 0
# for i in A:
#     suma += i
# for j in B:
#     sumb += j
# if suma > sumb:
#     print('Сумма больше в коортеже - A')
# else:
#     print('Сумма больше в коортеже - Б')
#
# print(A.index(min(A)) + 1)
# print(B.index(min(B)) + 1)

# .......................

# *** Dictionaries ***

# Position = {'Manager' : {'Director',
# 			 'Deputy Director'},
# 	    'Teacher' : {'Specialist',
# 			 'Methodist',
# 			 'Senior Lecturer'},
# 	    'Staff' : {'Cleaner',
# 		       'Porter',
# 		       'Watchman'}}
#
# count1 = len(Position)
# count2 = len(Position['Manager'])
# count3 = len(Position['Staff'])
#
# print(Position, 'len:', count1, '/n',
#       Position['Manager'], 'len:', count2, '/n',
#       Position['Staff'], 'len:', count3, '/n')

# .......................

# *** длина словаря ***

# Mounths = {1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr',
#            5: 'May', 6: 'Jun', 7: 'Jul', 8: 'Aug',
#            9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec', }
# count = len(Mounths)
# print(count)

# *** заполнение вручную словаря ***

# d = dict()
# count = int(input('Количество слов в стоваре:'))
# i = 0
# while i < count:
#     print('Ввод слов')
#     wrd = input('Слово: ')
#     value = int(input('Значение: '))
#     if wrd not in d:
#         d[wrd] = value
#     i += 1
# print(d)

# *** обьединение двух списков в словарь ***

# Num = dict(zip([1, 2, 3], ['One', 'Two', 'Tree']))
# print(Num)

# *** Обход словаря циклом for ***

# Mounths = {1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr',
#            5: 'May', 6: 'Jun', 7: 'Jul', 8: 'Aug',
#            9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec', }
#
# for mn in Mounths:
#     print(mn, ': ', Mounths[mn])

# *** вывести возраст из словаря ***

# person = {'name': 'Alex', 'age': 23, 'city': 'Minsk', }
# print(person['age'])

# .......................

# person = {'BMW': ["model1", 'model2', 'model3', ],
#           'Tesla': ['tmodel1', 'tmodel2', 'tmodel3']
#           }
# print(person['BMW'][0], person['BMW'][-1],
#       person['Tesla'][0], person['Tesla'][-1])

# .......................

# d1 = {'a': 100, 'b': 200, 'c': 300}
# d2 = {'a': 300, 'b': 200, 'd': 400}
# print(d1['b'] == d2['b'])

# .......................

# products = {'огурцы':[20, 6.99], 'помидоры': [30, 9.99],
#             'картошка': [5, 1.60],
# }
# for key, value in products.items():
#     print(key, value[0], value[1], sep=' - ')
# sold1 = input('Введите название товара: ')
# sold2 = int(input('Введите количество: '))
# for key, value in products.items():
#     if key == sold1 :
#         value[0] = value[0] - sold2
#         p_cost = sold2 * value[1]
#         print(sold1, 'будут стоить', p_cost, 'рублей за', sold2, 'шт.')
#         print('Оставшееся количество товара:', key, value[0], value, sep=' -')

# .......................

# *** Sets ***

# *** проверить, есть ли в последовательности чисел списка дубликаты***

# x = [1, 2, 3, 4, 5, 1 ,2]
# if x == set(x):
#     print('нет дубликатов')
# else:
#     print('есть дубликаты')


# *** пересечение и обьединения двух множеств ***

# set1 = {1, 2, 3}
# set2 = frozenset({1, 2, 3, 4, 5, 6})
# print(set1 | set2)
# print(set1 & set2)


# *** кости ***

# import random
# s1 = set()
# i = 0
# while i < 3:
#     num = random.randint(0, 6)
#     s1.add(num)
#     i += 1
# s2 = set()
# i = 0
# while i < 3:
#     num = random.randint(0, 6)
#     s2.add(num)
#     i += 1
# if sum(s1) > sum(s2):
#     print(sum(s1), sum(s2))
#     print('Вы проиграли')
# elif sum(s1) == sum(s2):
#     print('Ничья')
# else:
#     print(sum(s1), sum(s2))
#     print('Вы победили'

# *** вывод значений из множества по порядку ***

# n = int(input("Введите количество строк: "))
# list_numbs = [input() for i in range(n)]
# set_numbs = set(list_numbs)
# new_list = []
# for i in list_numbs:
#     if i in set_numbs and i not in new_list:
#         new_list.append(i)
# print('\n'.join(new_list))

# .......................

# a = int(input())
# b = int(input())
# c = a / b
# try:
#     b = 0       print(a / b)
# except ZeroDivisionError:
#     print("Деление на ноль!")
# finally:
#     print('Файнали')

# .......................

