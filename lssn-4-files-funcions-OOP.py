# *** Files ***

# import os
# with open('test1.txt', mode='r') as f:
#     s = f.readlines()
#     print(s)
# for i in s:
#     i = i.replace('_', ' ')
#     la = i.split(' ')
# print(la)
# sum = 0
# for i in la:
#     if i.isdigit():
#         i = int(i)
#         sum += i
# print(sum)

# .......................

# import os
# with open('test3.txt', mode='w') as f:
#     s = input()
#     while s != '':
#         f.write(s + '\n')
#         s = input()

# .......................

# import os
# with open('test3.txt', mode='w') as f:
#     while True:
#         s = input()
#         if s == '':
#             break
#         f.write(s + '\n')

# *** Functions ***

# def f(x):
#     if x <= -2:
#         return 1-((x+2)**2)
#     elif -2 < x <= 2:
#         return -(x/2)
#     elif 2 < x:
#         return ((x-2)**2)+1

# .......................

# def modify_list(l):
#     for i in range(len(l) - 1, -1, -1):
#         if l[i] % 2 == 0:
#             l[i] = l[i]//2
#         elif l[i] % 2 != 0:
#             del l[i]

# .......................

# *** декоратор функции ***

# def first_f1():
# 	print('Test function 1')
#
#
# def second_f2():
# 	print('Test function 2')
#
# def simple_decor(fn):
# 	def wrapper():
# 		print('Start function')
# 		fn()
# 		print('Stop function')
# 	return wrapper
#
# first_f_wrapped = simple_decor(first_f1)
# second_f_wrapped = simple_decor(second_f2)
# first_f_wrapped()
# second_f_wrapped()

# .......................

# def simple_decor(fn):
#     def wrapper():
#         print('Start function')
#         fn()
#         print('Stop function')
#     return wrapper
#
# @simple_decor
# def first_f1():
#     print('Test function 1')
#
# first_f1()


# *** функция, которая считает гласные и согласные ***

# def letters(n=input()):
#     n = n.lower().replace(" ", '')
#     v = 0
#     c = 0
#     for i in n:
#         if i not in ('a', 'e', 'y', 'u', 'i', 'o',):
#             v += 1
#         else:
#             c += 1
#     print(c, v, n)
# letters()


# *** передача аргумента в функцию с помощью декоратора***

# def param_transfer(fn):
#     def wrapper(arg):
#         print('Start function: ' + str(fn.__name__) + '(), with param: ' + str(arg))
#         fn(arg)
#     return wrapper
#
#
# @param_transfer
# def print_sqrt(num):
#     print(num ** 0.5)
#
# print_sqrt(4)

# .......................

# *** Написать функцию для подсчета разрядов числа ***

# def count(num):
#     return len(str(num))
# print("Количество разрядов:", count(int(input('Введите число: '))))

# *** функция, заполняющая массив рандомными числами в заданном диапазоне ***

# import random
#
# def mass(num1, num2):
#     arr = [random.randrange(num1, num2) for i in range(10)]
#     print(arr)
# mass(int(input('Введите минимальное число массива: ')), int(input('Введите максимальное число массива: ')))


# *** OOP ***

# class Example():
#     first_stat = 12
#     second_stat = 13
#
#     def __init__(self, din1, din2):
#         self.din1 = din1
#         self.din2 = din2
#
#     def new(self):
#         self.new_var = 69
#         print(self.new_var)
#
#     def sum(self):
#         return self.first_stat + self.second_stat
#
#     def exp(self):
#         return self.din1 ** self.din2
#
# var_example = Example(3, 5)
# print(var_example.sum())
# print(var_example.exp())
# var_example.new()

# .......................

# *** Напишите программу по следующему описанию. Есть класс "Воин".
# От него создаются два экземпляра-юнита. Каждому устанавливается здоровье в 100 очков.
# В случайном порядке они бьют друг друга. Тот, кто бьет, здоровья не теряет. У того, кого
# бьют, оно уменьшается на 20 очков от одного удара. После каждого удара надо выводить сообщение,
# какой юнит атаковал, и сколько у противника осталось здоровья. Как только у кого-то
# заканчивается ресурс здоровья, программа завершается сообщением о том, кто одержал победу.***

# import random
# class Unit():
#     hp = 100
#     hit = 20
#     def fight(self):
#         self.hp = self.hp - self.hit
#         return self.hp
# unit1 = Unit()
# unit2 = Unit()
# while unit1.hp != 0 and unit2.hp != 0:
#     x = random.randint(1, 2)
#     if x == 2:
#         print('Unit2 attacks')
#         print('Unit1 has', unit1.fight(), 'hp left.')
#     else:
#         print('Unit1 attacks')
#         print('Unit2 has', unit2.fight(), 'hp left.')
# print('Победу одержал Unit' + str(x) + ' !!!')

# ***  Есть класс Person, конструктор которого принимает три параметра (не учитывая self) –
# имя, фамилию и квалификацию специалиста. Квалификация имеет значение заданное по умолчанию,
# равное единице.
#   У класса Person есть метод, который возвращает строку, включающую в себя всю информацию о
# сотруднике.
#   Класс Person содержит деструктор, который выводит на экран фразу "До свидания, мистер …"
# (вместо троеточия должны выводиться имя и фамилия объекта).
#   В основной ветке программы создайте три объекта класса Person. Посмотрите информацию о
# сотрудниках и увольте самое слабое звено.
#   В конце программы добавьте функцию input(), чтобы скрипт не завершился сам, пока не будет
# нажат Enter. Иначе вы сразу увидите как удаляются все объекты при завершении работы программы. ***

# class Person():
#
#     def __init__(self, name, sur, cval=1):
#         self.name = name
#         self.sur = sur
#         self.cval = cval
#
#     def info(self):
#         return print(self.name, self.sur, self.cval)
#
#     def __del__(self):
#         print('Goodbye Mr.' + self.name + ' ' + self.sur)
#
#
# spec1 = Person('Alex', 'Novik')
# spec1.info()
# del spec1
#
# def x():
#     x = input()
#
# x()

# ..............................................

# class Human():
#     default_name = 'default_name'
#     default_age = 'default_age'
#
#     def __init__(self, name=default_name, age=default_age):
#         self.name = name
#         self.age = age
#         self.__money = 0
#         self.__house = None
#
#     def info(self):
#         print('-------------')
#         print(self.name, self.age, self.__money, self.__house)
#
#     def ern_money(self, sum):
#         self.sum = sum
#         self.__money += self.sum
#
#
#     def __make_deal(self, model_house, price):
#         self.__house = model_house
#         self.__money -= price
#         print('-------------')
#         print(f'Money after bying a house: {self.__money}$')
#
#
#     def buy_house(self, model_house, discount):
#         price = model_house.final_price(discount)
#         if price <= self.__money:
#             print(f'Congrats, you bought a {model_house} house!')
#             self.__make_deal(model_house, price)
#         else:
#             print('Check your balance please.')
#
#     @staticmethod
#     def default_info():
#         print('-------------')
#         print(f'Дефолтное имя: {Human.default_name}.', f'Дефолтный возраст: {Human.default_age}.')
#
#
# class House():
#     default_area = 0
#     default_price = 0
#
#     def __init__(self, area=default_area, price=default_price):
#         self._area = area
#         self._price = price
#
#     def final_price(self, discount):
#         final_price = self._price - (self._price * (discount / 100))
#         print('-------------')
#         print(f'Total price including discount: {final_price}$')
#         return final_price
#
# class SmallHouse(House):
#     default_area = '40 m^2'
#     def __init__(self, price):
#         super().__init__(area=SmallHouse.default_area, price=price)
#
#
#     def info(self):
#         print('-------------')
#         print(f'Default house area: {self._area}')
#
# alex = Human('Alex', 23)
# alex.ern_money(500)
# alex.info()
# alex.default_info()
# small_house1 = SmallHouse(1000)
# small_house1.info()
# alex.buy_house(small_house1, 10)
# alex.ern_money(500)
# alex.buy_house(small_house1, 10)
# alex.info()