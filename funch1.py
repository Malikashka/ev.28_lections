# найти квадрат, куб, результат деления на 100
# num1 = 5
# -> {'num': 5, '2': 25,'3':125,'100':0.05}

# num1 = 5
# print({'num': num1, '2': num1 ** 2,'3':num1 ** 3 ,'100':num1 / 100})
# num2 = 16
# print({'num': num2, '2': num2 ** 2,'3':num2 ** 3 ,'100':num2 / 100})
# num3 = 28
# print({'num': num3, '2': num3 ** 2,'3':num3 ** 3 ,'100':num3 / 100})
# num4 = 1154
# print({'num': num4, '2': num4 ** 2,'3':num4 ** 3 ,'100':num4 / 100})
# num5 = 31
# print({'num': num5, '2': num5 ** 2,'3':num5 ** 3 ,'100':num5 / 100})

# # # Dry - Dont repeat yourself
# num1 = 5
# num2 = 16
# num3 = 28
# num4 = 1154
# num5 = 31
# def operations(num):
#     print({'num':num, '2': num ** 2, '3': num ** 3,'100':num / 100})

# operations(num1)
# operations(num2)
# operations(num3)
# operations(num4)
# operations(num5)

#-------------------------------
# функция - это именованная часть программы которая содержит 
# в себе определенный набор инструкций и может вызываться в других частях столько раз сколько угодно 

# def name_of_func(<a, b>#параметры):
#    <body> # код какая то логика которая будет давать конечный результат
#    <return> # оператор который помогает вернуть результат

# name_of_func(5,6 # оргументы)
             
# параметры функций - это перемеменные которые будут принимать
# данные от мпользователя и хранить в себе эти данные

# аргументы функции - данные которые мы передаем в функцию в моменте вызова

# print(len('str'))

# ls = [1,2,3,4,5]
# str1 = 'hello world s vami Kani i John Snow!'

# def our_len(obj):
#     i = 0
#     print(obj)
#     for x in obj:
#         i += 1
#     print(f'result:{i}')

# our_len(ls) # [1,2,3,4,5]
# our_len(str1)


# def isEven(obj):
#     if obj % 2 == 0:
#         return True
#     else:
#         return False
    
# result = isEven(6)
# print(result)
# print(isEven(5))

#----------------------------

# words = ['John', 'Ono', 'kazak', 'peter', 'dovod', 'radar', 'apa', 'piko']
# def get_polindrom(words):
#     result = []
#     for word in words:
#         if word.lower() == word[::-1].lower():
#             result.append(word)
#     return result

# palindrom_words = get_polindrom(words)
# print(polindrom_words)


# def get_percenage(money, period):
#     if money < 30000:
#         raise ValueError ('вложить можно более 30000')
#     if period < 3:
#         raise ValueError ('период должен юыть не менее 3 лет ')
#     year = 0
#     while year < period:
#         money += money * 0.1
#         year += 1
#     return money

#  try:
#     money = float(input('Введите сумму вложения:'))
#     period = int(input('Введите период: '))
#     print(get_percenage(money, period))
# except ValueError:
#     print('неправильный ввод!!!')

# def range(first, last, step=1):
#     pass



# def isEven(num:int)->bool:
#     """Our function returns True or False while checking number for even number"""
#     return True
# print(isEven(5))
# print(isEven([1,2,3]))

