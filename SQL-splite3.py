# *** Some tasks for SQL requests ***

# SELECT ProductName, ProductionDate, ExpirationDate FROM Products

# .......................

# SELECT DISTINCT checks FROM Operation;

# .......................

# SELECT * FROM Players ORDER BY losses;

# .......................

# SELECT * FROM cakes ORDER BY calories LIMIT 3;

# .......................

# SELECT firstname FROM staff WHERE salary BETWEEN 1500 AND 1900;

# .......................

# SELECT name FROM films WHERE year >= 2010 AND production = 'Marvel Studios' ORDER BY name;

# .......................

# SELECT teamname, country from teams WHERE country IN ('Spain', 'England', 'Germany');

# .......................

# SELECT CONCAT (firstname, ' ', lastname) AS fullname, salary*12+experience*500 AS total FROM staff ORDER BY total;

# .......................

# SELECT AVG(score) FROM sam_grades WHERE semester != 2;

# .......................

# SELECT * FROM Foods WHERE fatpercentage < (SELECT AVG(fatpercentage) FROM Foods);

# .......................

# SELECT * FROM desserts WHERE name LIKE '%Chocolate%';

# .......................

# SELECT * FROM apartments WHERE price > (SELECT AVG(price) FROM apartments) AND status != '%Rented%' ORDER BY price;

# .......................

# SELECT students.id, students.firstname, students.lastname, teachers.lastname AS teacher FROM students, teachers WHERE  students.teacherid = teachers.id
# order by students.id;

# .......................

# SELECT p.productname, p.price, c.categoryname FROM products AS p, categories AS c WHERE p.categoryid = c.id;

# .......................

# SELECT * FROM Norwaychess UNION SELECT * FROM Tatasteel ORDER BY rating DESC;

# .......................

# INSERT INTO garage VALUES (6,    'Mercedes-Benz',   'G 63',   2020), (7,   'Porsche',    'Panamera',     2020);
# SELECT * FROM garage;

# .......................

# DELETE FROM products WHERE expiredate=0;
# SELECT * FROM products;

# .......................

# CREATE TABLE leaderboard (place INT,
# nickname VARCHAR, rating INT);
# INSERT iNTO leaderboard
# VALUES (1, 'Predator', 9500), (2, 'JohnWar', 9300), (3, 'NightWarrior', 8900);
# SELECT * FROM leaderboard;

# .......................

# ALTER TABLE cities ADD AttractivePlace varchar;
# UPDATE cities SET AttractivePlace ='Belem Tower'
# WHERE name='Lisbon';
# UPDATE cities SET AttractivePlace ='Plaza Mayor'
# WHERE name='Madrid';
# UPDATE cities SET AttractivePlace = 'Eiffel Tower'
# WHERE name='Paris';
#
# SELECT * FROM cities;

# .......................

# CREATE VIEW list AS SELECT acc_id, status FROM users;
# SELECT * FROM list;

# .......................

# INSERT INTO animals VALUES ('Slim', 'Giraffe', 1);
# CREATE VIEW list AS SELECT name, type, country FROM animals INNER JOIN Countries ON animals.country_id = countries.id ORDER bY country;
# SELECT * FROM list;

# .......................

# *** Some sqlite3 tasks ***


# import random
# import sqlite3
# from random import randint
# conn = sqlite3.connect('base.db')
# cursor = conn.cursor()
# cursor.execute('''CREATE TABLE iF NOT EXISTS tab_1(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1  INTEGER, col_2 INTEGER)''')
# a = 0
# while a <= 4:
#     cursor.execute("""INSERT INTO tab_1(col_1, col_2) VALUES (?,?)""",(random.randint(0, 9),random.randint(0, 9)))
#     conn.commit()
#     a += 1
# cursor.execute('''SELECT col_1, col_2 FROM tab_1''')
# k = cursor.fetchall()
# sum = 0
# for i in k:
#     sum += i[0] + i[1]
# if sum/(a+1) > (a+1):
#     cursor.execute('''DELETE FROM tab_1 WHERE  id = 4 ''')
#     conn.commit()
# else:
#     print('Количество записей равно среднему арифметическому')
# print(sum)

# .......................

# import random
# import sqlite3
# from random import randint
# conn = sqlite3.connect('base.db')
# cursor = conn.cursor()
# cursor.execute('''CREATE TABLE iF NOT EXISTS tab_1(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1  INTEGER, col_2 INTEGER)''')
# a = 0
# while a <= 4:
#     cursor.execute("""INSERT INTO tab_1(col_1, col_2) VALUES (?,?)""",(random.randint(0, 9),random.randint(0, 9)))
#     conn.commit()
#     a += 1
#
# cursor.execute('''SELECT*FROM tab_1''')
# k = cursor.fetchall()
# k2 = random.choice(k)
# print(*k2)
# if k2[1]%2 == 0 and k2[2]%2 == 0:
#     cursor.execute("""DELETE FROM tab_1 WHERE id=?""", (k2[0],))
#     conn.commit()
#     print(cursor.fetchall())
# else:
#     cursor.execute("""UPDATE tab_1 SET col_1 = 2, col_2 = 2 WHERE id=?""", (k2[0],))
#     conn.commit()
#     print(cursor.fetchall())

 # .......................

# import sqlite3
#
# conn = sqlite3.connect('base.db')
# cursor = conn.cursor()
# cursor.execute('''CREATE TABLE iF NOT EXISTS tab_1(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1  INTEGER)''')
# conn.commit()
#
# cursor.execute("SELECT * FROM tab_1")
# fetch_all = cursor.fetchall()
#
#
# def print_base():
#     for _ in fetch_all:
#         print(f"id: {_[0]}, col_1: {_[1]}")
#
#
# class Database:
#
#     def enter_arg(self, arg_1=None, arg_2=None, arg_3=None):
#         if arg_1 is not None and arg_2 is None and arg_3 is None:
#             print('Var 1')
#             cursor.execute('''INSERT INTO tab_1 (col_1) Values (3) ''')
#         elif arg_1 is not None and arg_2 is not None and arg_3 is None:
#             print('Var 2')
#             if type(arg_2) is int:
#                 cursor.execute("SELECT id FROM tab_1")
#                 first = cursor.fetchone()[0]
#                 cursor.execute('''DELETE FROM tab_1 WHERE id = ? ''', (first,))
#         elif arg_1 is not None and arg_2 is not None and type(arg_3) is int:
#             print("Var 3")
#             cursor.execute("UPDATE tab_1 SET col_1 = 77 WHERE id = 5")
#         conn.commit()
#
#
# database = Database()
# database.enter_arg(1)
# print_base()
# database.enter_arg(1, 2)
# print_base()
# database.enter_arg("1", "2", 3)
# print_base()

#.......................

# import sqlite3
# import os
# conn = sqlite3.connect('base.db')
# cursor = conn.cursor()
# cursor.execute('''CREATE TABLE iF NOT EXISTS tab_1(id INTEGER PRIMARY KEY AUTOINCREMENT, c1  TEXT, c2  TEXT)''')
# conn.commit()
# a = 0
# while a <= 3:
#     cursor.execute("""INSERT INTO tab_1(c1, c2) VALUES (?,?)""", ('first', 'second'))
#     conn.commit()
#     a += 1
# cursor.execute('''DELETE FROM tab_1 WHERE id = ? ''', (2, ))
# conn.commit()
# cursor.execute("UPDATE tab_1 SET c1 = 'hello', c2 = 'world' WHERE id = 3")
# conn.commit()
# with open('bd.txt', mode='w', encoding='utf-8') as f:
#     cursor.execute('''SELECT * FROM tab_1''')
#     k = cursor.fetchall()
#     for _ in k:
#         f.write(f"id: {_[0]}, c1: {_[1]}, c2: {_[2]} \n")