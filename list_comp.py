# list comprehensions - генераторы списков
# list comprehensions - упрощенный подход к созданию списков, который задействует в себе цикл for, 
# а также конструкцию if для определения того, что в итоге попадает в наш список.

# list -> 0 - 200 -> num % 2 = 0

# ls = []
# for x in range(0, 201):
#     if x % 2 == 0:
        # ls.append(x)
# ls = [x for x in range(0,201) if x % 2 != 0]
# print(ls)

# list: 0 - 300 -> num % 2 == 0, num % 3 == 0
# ls = []
# for x in range(0,301):
#     if x % 2 == 0 and x % 3 == 0:
#         ls.append(x)
# print(ls)

# ls = [i for i in range(0,301) if i % 2 == 0 and i % 3 == 0]
# print(ls)

# list: 0 - 100 -> x % 2 == 0 : x ** 2, x % 3 == 0: x ** 3 

# ls = []
# for x in range(0,101):
#     if x % 2 == 0:
#         ls.append(x ** 2)
#     elif x % 3 == 0:
#         ls.append(x ** 3)
# print(ls)
# print(5 if input() == 'yes' else 7)

# ls = [x ** 2 if x % 2 == 0 else x ** 3 for x in range(0,101) if x % 2 == 0 or x % 3 == 0]
# print(ls)

#----------------------------

# newlist = [expression for item in iterable <if condition == True>]

# ls = [str(i * 2) for i in range(0,11)]
# print(ls)

# ls = [[1,2,3], [4,5,6], [7,8,9]]
# result = [1,2,3,4,5,6,7,8,9]

# res = []
# for x in ls:
#     for item in x:
#         res.append(item)

# print(res)

# ls = [[1,2,3], [4,5,6], [7,8,9]]
# res = [item for x in ls for item in x]
# print(res)

#---------------------

# from datetime import datetime

# start = datetime.now() #19.55
# ls = [x for x in range(0,100_000_000)]
# # ls = []
# # for x in range(0,100_000_000):
# #     ls.append(x)
# finish = datetime.now() # 19.55.46
# print(finish - start)

#-----------------------
#set comprehensions
# set_ = {x for x in range(1,100)}
# print(set_, type(set_))
# set1 = {1,2,3,4 'a' ,True}
# print(set1)

#-------------------
#dict comprehensios
# dict = {
#     key: value,
#     key: value
# }
# dict_ = {x: x ** 2 for x in range(0,16)}
# print(dict_)

# names = ['John', 'Tirion', 'Eygan', 'Sansa', 'Ramsi']
# dict_ = {x:len(x) for x in names}
# print(dict_)

#-----------------------
# dict1 = {
#     'Soke': {'history': 99, 'fizik': 95, 'math': 94},
#     'Omoke':{'history': 84, 'fizik': 75, 'math': 86},
#     'John': {'history': 100, 'fizik': 87, 'math': 90},
# }

# res ={}
# for key, value in dict1.items():
#     for inner_key, inner_value in value.items():
#         if max(value.values()) == inner_value:
#             res[key] = inner_value
# print(dict1)
# print(res)
# res = {key: inner_key for key, value in dict1.items() 
# for inner_key, inner_value in value.items() if inner_value == max(value,values())}
# print(res)
# try:
#     n = int(input('Vvedite chislo: '))
# except ValueError:
#     print('Invalid number!')
# else:
#     dict_ = {x: x ** 2 for x in range(1,501) if x % n == 0}
#     print(dict_)