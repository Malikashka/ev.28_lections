# PostgresSQL - это система управления БД(СУБД/DBMS)
# СУБД - это ряд программ и инструментов позволяющих создавать БД, управлять ею и манипулировать данными внутри(CRUD)

# Postgres - это сама база данных, она реляционная, то есть данные хранятся в виде таблиц, и таблицы имеют связи между собой
# SQL (Structured Query Language) - декларативный язык структурированных запросов, он применяется для создания и получения данных при помощи запросов

# ----------------------------------------------
# Команда для входа в бд через юзера postgres:
# sudo -u postgres psql

# Команда для выхода
# exit

# Команда для входа в своего юзера
# # Команда для выхода
# \q

# создание юзера
# CREATE ROLE 'username' SUPERUSER LOGIN PASSWORD '1';

# изменения пароля
# alter user 'username' with password '1';

# создание бд
# create database 'name'

# \l - список бд

# \du - все юзеры

# \dt - все таблицы (нужно подключиться к бд заранее)

# \c 'name' - команда для подключения к бд
# psql -U <username> -d <dbname> - подключаемся под выбранным username к dbname


# class Password:
#     password = ''
#     def validate(self, password):
#         if len(password) not in range(9, 15):
#             return 'Password should be longer than 8, and less than 15'

#         if not any(ch.isdigit() for ch in password):
#             return 'Password should contain numbers too'

#         if not any(ch.isalpha() for ch in password):
#             return 'Password should contain letters as well'

#         symbols = ['@', '#', '&', '$', '%', '!', '~', '*']

#         if not any(ch in symbols for ch in password):
#             return 'Your password should have some symbols'

#         self.password = password

#         return 'Ваш пароль сохранен.'

#     def str(self):
#         return '*' * len(self.password)

# p = Password()
# print(p.validate('sdfd128@sjslk'))
# print(p)




# Типы полей в postgres

# Numeric Types (числовые типы)
    # a. smallint (2 bytes) -> -32767 to 32767
    # b. integer (4 bytes) -> -2.147 ... to 2.147...
    # c. bigint (8 bytes) -> ...
    # d. real (4 bytes) -> число с плавающей точкой, вещественные (6 знаков после запятой)
    # f. double precsion (8 bytes) -> real, но только с двойной точностью (12 знаков после запятой)
    # g.  serial (4 bytes) -> integer, auto-increment

# Character types (Символьные типы(строковые)):
    # a. varchar(количество символов)-> если мы укажем 50 символов, а заполним только 10, то остальные будут свободны
    # b. char (количество символов)-> если мы укажем 50 символов, а заполним только 10, то остальные будут заполнены пробелами
    # c. text() -> неограниченное количество символов

# Boolen Type
    # a. boolean (1 bytes) -> True/False

# date -> календарная дата (год, месяц, день)
# location  -> координатная точка (x, y) - (245, -12)

# enumerate types:
    # ('a', 'b', 'c')
    # CREATE TYPE <any name> AS ENUM('Happy', 'Sad', 'Mad')
    
    
# Команда для создания таблицы 
# CREATE TABLE <table name> (
#     <column> <type>,
# )

# films_db=# create table films(
# code char(5),
# title varchar(100),
# date date,
# genre varchar(50),
# budget integer,
# country varchar(50),
# id serial
# );

# DROP TABLE <name> - удаление таблицы


# Команда для добавления данных в таблицу
# INSERT INTO <tablename> [(columns)] values (data), (data);

# insert into films (code, title, date, genre, budget, country) VALUES
# ('het5', 'Lord of The Rings', '2001-06-12', 'Fantasy', 1200000, 'USA');

# Команда для получения данных:
# SELECT (columns) from <tablename>;

# Команда для обновления данных:
# UPDATE <table_name> SET <column> = <new_value> WHERE <column> = <value>;

# Команда для удаления данных:
# DELETE FROM <table> WHERE <column> = <value>;




# def longest_words(filename):
#     with open(filename, 'r') as file:
#         text = file.readlines()
#         text = [i.replace('\n', '') for i in text]

#     print(text)
    
# print(longest_words('article.txt'))

# ORDER BY: Позволяет нам соритровать выходящие данные по убыванию или возрастанию. ASC(по возрастанию) и DESC (по убыванию)

# Синтаксис: SELECT <row> from <tablename> order by <row> [asc/desc];

# Синтаксиc: SELECT <row> FROM <tablename> where <row> = 'чему либо'

# BETWEEN: условие между
# SELECT * FROM products WHERE id BETWEEN 3 and 8

# LIKE: Выводит результат который соответствует введенному шаблону для строк. (Он чувствителен к регистру)
# ILIKE: Выводит результат который соответствует введенному шаблону для строк. (Он  не чувствителен к регистру)
# Синтаксиc: SELECT <row> FROM <tablename> where <row> LIKE/ILIKE 'чему либо'

# AND оператор и, для множественных условий
# IN оператор в: <row> in (1,2,3,4,5);


# GROUP BY: Разделяет данные которые мы получаем в SELECT, при этом группируя их по определенному признаку

# HAVING: ставит условие при помощи которого данные отбираются в группировку

# Экспорт БД(damb):
# pg_dump -U <username> -d 'db_name' > 'file.sql'

# Импорт:
# psql -U username -d <dbname> -f <filename>


# LIMIT: ставит ограничение в количестве получаемых данных


# ----------------------------------------------------------
# Связи между талицами (relations):
    # 1. Один к одному (one to one) - человек и паспорт
        # В одну из талбиц добавляется поле fk и дается ограничения unique
    # 2. Один ко многим (one to many) - человек и банковские карты
        # В таблицу много (банковские карты добавляется поле fk)
    # 3. Многие ко многим (Many to many) - студенты и преподователи
        # Создается вспомогательная третья таблица со связями
         
# Ограничения
    # 1. NOT NULL - обязательна к заполнению
    # 2. UNIQUE - она обозначает, что будут хранться только уникальные данные
    # 3. CHECK - (check age > 0) ограничение проверки на условие
    # 4. PRYMARY KEY (для установки идентификатора данных в таблице)
    # 5. FOREIGN KEY - (для установки связей между таблицами)
    # 6. ON DELETE (для установки поведения удаление данных которые были связаны)
    

# Оператор Join()
# Данный оператор служит для выборки данных из двух таблиц

# LEFT JOIN: выборка будет содержать все строки из левой таблицы
# RIGHT JOIN: выборка будет содержать все строки из правой таблицы

# Синтаксиз:
# SELECT p1.title, p1.price, o1.quantity, p1.price * o1.quantity as total_sum from products as p1 JOIN orders as o1 ON p1.id = o1.product_id;


# Вытащить все произведения в котрых sourse = Moby и кол-во параграфов меньше 100
# SELECT source, totalparagraphs FROM work WHERE source = 'Moby' AND totalparagraphs < 100; 


# 2. Найти кол-во глав в каждом произведении
# select count(*), work.title from chapter join work on work.workid = chapter.workid group by work.title order by count(*) desc;

# 3. Найти сколько произведений относятся к каждому 
# select count(*), genretype from work group by genretype;

# 4. Найти кол-во параграфов в каждом произведении и вытащить названия произведений
# select count(*), work.title from paragraph join work on work.workid = paragraph.workid group by work.title;


# 5. Вытащить имена героев, чьи реплики состовляют больше 200 слов, также произведения в которых они встречаються, жанр, год выхода произдведения в порядке убывания
# select character.charname, work.title, work.genretype, work.year from character_work join character on character.charid = character_work.charid join work on work.workid = character_work.workid where character.speechcount > 200 order by work.year desc;


# 6. Вытащить героя, который чаще всех появляется в произведениях
# SELECT character.charname, COUNT(*) AS works_count FROM character_work JOIN character
# ON character.charid = character_work.charid JOIN work ON character_work.workid = work.workid
# GROUP BY character.charname ORDER BY works_count DESC LIMIT 1;





