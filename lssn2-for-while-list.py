# *** Напишите программу, на вход которой даются четыре числа a, b, c и d, каждое в своей строке. Программа должна
# вывести фрагмент таблицы умножения для всех чисел отрезка [a; b] на все числа отрезка[c;d].
# Числа a, b, c и d являются натуральными и не превосходят 10, a≤b,c≤d. ***

# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
#
# for x in range(c,d+1):
#     print('\t',x, end="")
# print()
# for z in range(a,b+1):
#     print(z, end='     ')
#     for y in range(c, d+1):
#         print(z*y, end='    ')
#     print()

# *** Напишите программу, которая считывает с клавиатуры два числа a и b, считает и выводит на консоль среднее арифметическое
# всех чисел из отрезка [a;b], которые кратны числу 3. ***

# a = int(input())
# b = int(input())
# s=0
# y=0
# for i in range(a,b+1):
#     if i%3==0:
#         s+=i
#         y+=1
# print(s/y)


# *** Some  more tasks For loops ***

# s = input()
# sim = input()
# t = ''
# for i in s:
#     if i != sim:
#         t += i
# print(t)

# .......................

# start = input()
# end = input()
# step = input()
# a = range(int(start), int(end), int(step))
# for i in a:
#     print(i)

# .......................

# dishes = ['Курица', 'Мясо', 'Рыба']
# a = input()
# for i in dishes:
#     if a != i:
#         continue
#     else:
#         print('Я не ем ', i)

# .......................

# x = 1
# for i in range(1, 101):
#     if i % 2 != 0:
#         x *= i
# print(x)

# .......................


# s = []
# for i in range(1, 501):
#     if i % 5 == 0:
#         s.append(i)
#     else:
#         continue
# print(s)

# .......................

# s = []
# for i in range(1, 498):
#     if i % 2 == 0:
#         s.append(i)
#     else:
#         continue
# print(*s)

# .......................

# s = ['1', '1', '2', '3', '3']
# x = []
# for i in s:
#     if s.count(i) >= 2:
#         if i in x:
#             continue
#         x.append(i)
# print(x)

# *** Напишите программу, которая считывает со стандартного ввода целые числа, по одному числу в строке, и после первого
# введенного нуля выводит сумму полученных на вход чисел. ***

# i = 0
# s=int(input())
# while  s != 0:
#     i+=s
#     s = int(input())
# print(i)

# *** В Институте биоинформатики между информатиками и биологами устраивается соревнование. Победителям соревнования достанется
# большой и вкусный пирог. В команде биологов aa человек, а в команде информатиков — b человек. Нужно заранее разрезать пирог
# таким образом, чтобы можно было раздать кусочки пирога любой команде, выигравшей соревнование, при этом каждому участнику
# этой команды должно достаться одинаковое число кусочков пирога. И так как не хочется резать пирог на слишком мелкие кусочки,
# нужно найти минимальное подходящее число. Напишите программу, которая помогает найти это число. ***

# d = 1
# a=int(input())
# b=int(input())
# while d%a!=0 or d%b!=0:
#     d+=1
# print(d)


# *** Some  more tasks While loops ***

# *** сумма чисел от 1 до 50 ***

# i = 1
# result = 0
# while i <= 50:
#     reesult += i
#     i += 1
# print(result)

# .......................

# *** вывести квадраты всех целых чисел от 1 до 10 ***

# i = 1
# result = 0
# while i <= 10:
#     result = i * i
#     i += 1
#     print(result)

# .......................

# *** перемножить все четные значения в диопазоне от 0 до 125 ***

# i = 1
# result = 1
# while i <= 125:
#     if i % 2 == 0:
#         result *= i
#     i += 1
# print(result)

# .......................

# *** Вывести числа от 1 до 15 в порядке убывания ***

# i = 15
# s = ""
# while i >= 1:
#     s += str(i) + ' '
#     i -= 1
# print(s)

# .......................

# i = 1
# s = []
# while i <= 15:
#     s.append(i)
#     i += 1
# s.reverse()
# print(*s)

# .......................

# i = 7
# s = []
# while a <= 100:
#     s.append(i)
#     i += 7
# print(*s)
# print(len(s))

# .......................

# a = int(input())
# b = int(input())
# arr = []
# while a < 0:
#     arr.append(a)
#     a += 1
# print(arr)

# .......................

#  *** Casino ***
# import random
#
# i = 1
# while i <= 5:
#     print('Попытка #', i)
#     x = input('Введите число и цвет: ')
#     number = random.randrange(1, 10)
#     color = random.randrange(1, 3)
#     if color == 1:
#         c = str(number) + " red"
#     else:
#         c = str(number) + " black"
#     if x == c:
#         print('Вы угадали')
#         print(c)
#         break
#     elif x != c:
#         print('Вы не угадали')
#         print(c)
#     i += 1


# *** Напишите программу, на вход которой подается одна строка с целыми числами. Программа должна вывести сумму этих чисел.
# Используйте метод split строки. ***

# a = [int(num) for num in input().split()]
# print(sum(a))

# *** Напишите программу, на вход которой подаётся список чисел одной строкой. Программа должна для каждого элемента этого списка
# вывести сумму двух его соседей. Для элементов списка, являющихся крайними, одним из соседей считается элемент,
# находящий на противоположном конце этого списка.
# Например, если на вход подаётся список "1 3 5 6 10", то на выход ожидается список "13 6 9 15 7" (без кавычек).
# Если на вход пришло только одно число, надо вывести его же.
# Вывод должен содержать одну строку с числами нового списка, разделёнными пробелом. ***

# a = [int(i) for i in input().split()]
# n = len(a)
# if n == 1:
#      print(*a)
# elif n == 2:
#     print(a[1]*2, a[0]*2)
# else:
#     for i in range(n-1):
#         print(a[i-1]+a[i+1])
#     print(a[-2]+a[0])

# *** Напишите программу, которая принимает на вход список чисел в одной строке и выводит на экран в одну строку значения,
# которые встречаются в нём более одного раза.
# Для решения задачи может пригодиться метод sort списка.
# Выводимые числа не должны повторяться, порядок их вывода может быть произвольным. ***

# a = [int(i) for i in input().split()]
# a.sort()
# n = len(a)
# b = []
# for i in range(n-1):
#     if a[i] == a[i+1] and not a[i] in b:
#         b.append(a[i])
# print(*b)

# *** Some  more tasks Lists ***

# *** Список в обратном порядке ***

# a = [1, 2, 3, 4]
# print(id(a), a[::-1])
# .......................
# a = [1, 2, 3, 4]
# print(a.reverse())

# .......................

# *** найти в списке первое вхождение числа 20 и заменить его на 200 ***

# a = [1, 20, 3, 20]
# ind = a.index(20)
# a[ind] = 200
# print(a)

# .......................


# *** случайно заменил все 20 на 200 ***

# a = [1, 20, 3, 20]
# for i in a:
#     if i == 20:
#         ind = a.index(20)
#         del a[ind]
#         a.insert(ind, 200)
# print(a)

# .......................

# arr = [15, 48, 'hello', 6, 19, 'world', 98, 3, ]
# x = []
# su = 0
# consonant = 0
# vowels = 0
# for i in arr:
#     i = str(i)
#     if i.isdigit():
#         if int(i) % 2 != 0:
#             x.append(1)
#         elif int(i) % 2 == 0:
#             while int(i) > 0:
#                 num = int(i) % 10
#                 su += num
#                 i = int(i) // 10
#             x.append(su)
#             su = 0
#     elif i.isalpha():
#         for letter in i:
#             if letter in 'aioeyu':
#                 vowels += 1
#             else:
#                 consonant += 1
# print('Всего гласных: ', vowels)
# print('Всего согласных: ', consonant)
# print(x)

# *** Напишите программу, которая считывает с консоли числа (по одному в строке) до тех пор, пока сумма введённых чисел
# не будет равна 0 и сразу после этого выводит сумму квадратов всех считанных чисел.
# Гарантируется, что в какой-то момент сумма введённых чисел окажется равной 0, после этого считывание продолжать не нужно.***

# a1 = int(input())
# s = a1
# s2 = a1**2
# while s != 0:
#     a1 = int(input())
#     s = s + a1
#     s2 = s2+(a1**2)
#     if s == 0:
#         break
# print(s2)


# *** Напишите программу, которая выводит часть последовательности 1 2 2 3 3 3 4 4 4 4 5 5 5 5 5 ... (число повторяется столько
# раз, чему равно). На вход программе передаётся неотрицательное целое число n — столько элементов последовательности должна
# отобразить программа. На выходе ожидается последовательность чисел, записанных через пробел в одну строку.
# Например, если n = 7, то программа должна вывести 1 2 2 3 3 3 4.***

# n = int(input())
# t = []
# if n > 1:
#     for i in range(1, n):
#         if n > 1:
#             t += [str(i)]*i
#     print(*t[0:n])
# elif n == 0 or n == 1:
#     print(n)

# *** Напишите программу, которая считывает список чисел lst из первой строки и число x из второй строки, которая выводит все
# позиции, на которых встречается число x в переданном списке lst. Позиции нумеруются с нуля, если число xx не встречается
# в списке, вывести строку "Отсутствует" (без кавычек, с большой буквы). Позиции должны быть выведены в одну строку,
# по возрастанию абсолютного значения. ***

# a = [int(i) for i in input().split()]
# num = int(input())
# b = []
# for i in range(len(a)):
#     if num == a[i]:
#         b.append(i)
#     elif num != a[i]:
#         continue
# if len(b) > 0:
#     print(*b)
# else:
#     print("Отсутствует")

# .......................

# n = ''
# m = []
# while True:
#     n = str(input()) # ввод строк
#     if n == 'end':
#         break
#     m.append([int(s) for s in n.split()])
# li, lj = len(m), len(m[0])
# new = [[sum([m[i-1][j], m[(i+1)%li][j], m[i][j-1], m[i][(j+1)%lj]]) for j in range(lj)] for i in range(li)]
#
# for i in range (li):
#     for j in range (lj):
#         print(new[i][j], end =' ')
#     print()

# *** Выведите таблицу размером n×n, заполненную числами от 11 до n^2 по спирали, выходящей из левого верхнего угла и
# закрученной по часовой стрелке, как показано в примере (здесь n=5): ***

# mas=int(input())
# arr=[[0 for j in range(mas)] for i in range(mas)]
# rem,i,k=0,0,1
# for m in range (mas,0,-1):
#     for j in range (rem,m):
#         arr[i][j]=k;k+=1
#     for i in range (rem+1,m):
#         arr[i][j]=k;k+=1
#     for j in range (m-2,rem-1,-1):
#         arr[i][j]=k;k+=1
#     for i in range (m-2,rem,-1):
#         arr[i][j]=k;k+=1
#     rem+=1
# for row in arr:
#     for elem in row:
#         print(elem, end=' ')
#     print()

