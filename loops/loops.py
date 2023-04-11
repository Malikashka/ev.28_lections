# while <expression>:
    # <body>

# i = 0
# while i < 10:
#     i += 1 # i = i + 1
#     print(f'Цикл сработал {i} раз!')

# ls = list(range(1, 51))
# print(ls.reverse())
# while ls:
#     print(ls.pop())

# name1 = ''
# name2 = ''
# i = 0
# while name1.lower() != 'john' and name2.lower() != 'Raichel':
#     name1 = input('Vvedite imya1: ')
#     name2 = input('Vvedite imya2: ')
#     print()
#     i += 1
#     if i >= 5:
#         print('Цикл остановлен!')
#         break # принудительная остановка
# else: # тот оператор который сработает если в файл прилетит false
#     print('Ты угадал!')


# #---------------------
# user = {'username': 'JohnSnow', 'password': 'ilovepython123'}
# i = 3
# # password = None
# while password != user['password']:
#     # password = input(f'{user["username"]} vvedite parol\': ')
#     i -= 1
#     if i == 0:
#         print('Vy zablokirovany!!!')
#         break
#     i -= 1
# else:
#     print(f'{user["username"]} vy uspeshno zashli v sistemu!')

#--------------------

# for <variable> in <iterable object>:
#     <body>

# list_ = [0,1,2,3,4,5,6,7,8,9]
# i = iter(list_)
# print(i)
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i)) #stop iteration

# import random
# ls = []
# for x in range(1, 101):
#     ls.append(random.randint(1,50))
# print(len(ls))
# ls = set(ls)
# ls = list(ls)
# print(ls)
# print(len(ls))

# ls = ['Tirion', 'Bilal', 'John', 'Samsa', 'Jamie', 'Eddart']
# for x in ls:
#     if x == 'Bilal':
#         continue
#     print(f'Hello Mr\Mrs {x}!')
# i = 0
# while i<100:
#     i += 1
#     if i % 2 == 0:
#         continue
#     print(i)
    
#число 100
# 1,2,4,5,10,
# 20,25,50,100

# num = 1_000_000_000
# res = []

# for x in range(1,int(num ** 0.5) + 1):
#     if num % x == 0:
#         res.extend({x, num // x})
# res.sort()
# print(res)