#list() -> (списки, массив) - изменяемый, последовательный тип данных, который предаствляет из себя коллукцию каких либо объектов(значений).

# my_list = [1, 'string', False, None, [1,2,3,4,5]]
# print(my_list, type(my_list))








# my_list = list('Hello world')
# ls = ('hello world')
# print(ls)
# print(my_list)

# tuple_ = ('banana', 'apple', 'cherry')
# print(tuple_, type(tuple_))
# ls = list (tuple_)
# print(ls, type(ls))

#индексация в списках
# ls = [1, 2, 3, 4, 5, 'string', [True, False, None]]
# print(ls, len(ls))
# print(ls[1], ls[2])
# print(ls[4:]) # [5, 'string', [True, False, None]]


# ls = [1, 2, 3, 4, 5, 'string', [True, False, None], 4, 5, 6]
# print(ls[6][2])

# i = 0
# while i < 5:
#    print(i)
#    i += 1

# ls = list(range(1,11))
# print(ls)
# for num in ls:
#     print("Hello world")

# ls = ['John', 'Sansa', 'Tririon', 'Eddart', 'Serseya', 'Jamie']
# print(ls, len(ls))
# for x in ls:
#     print(f'Hello Mr\Mrs  {x}! Welcome to the club!')
#     print('1')

# print('2')

# #ls -> 1, 21 -> четных чисел - квадрат числа
#             -> нечетных  чисел - куб числа  
# ls = list(range(1,21))
# print(ls)
# for num in ls:
#     if num % 2 == 0:
#         print(f'Число четное {num} квадрат: {num**2}')
#     else:
#         print(f'Число нечетное {num} куб: {num**3}')

#------------------------
#методы списков
# print(dir([]))

#append(element) - Дбавляет элемент в конец списка

# ls = [1, 2, 3]
# print(ls)
# ls.append(4)
# ls.append(5)
# ls.append('Hello')
# ls.append([True, False])
# print(ls)

#extend(object) - расширяет список
#ls = [1, 2, 3]
# ls.append('Hello')
# print(ls)
# ls.append('Hello')
# ls.extend(str(56))
# ls.extend([1, 2, 3])
# print(ls)
# ls = [1,2,3]
# ls1 = [4,5,6]
# print(ls + ls1)

#sort() - сортирует список, если передать reserve=True, то список отсортируется в убывающем порядке

# from random import randint

# ls = []
# for x in range(0, 100):
#     num = randint(0, 1000)
#     ls.append(num)

# print(ls)
# ls.sort()
# print('After:')
# print(ls)

# ls = ['John', 'Deyneris', 'Tirion', 'Aizirek', 'azaliya']
# ls.sort(key=len, reserve=True)
# print(ls)

#insert(index, element) - добавляет элемент по указанному index
# ls = ['string', 2, 3, False]
# ls.insert(1,1)
# print(ls)

#remove(element) - удаляет элемент из списка, если такого нет, то выводится ошибка
#pop[index] - удаляет и возвращает из списка по index, но если index не передать, то он удалет последний элемент

# ls = [5, 1, 2, 4, 4, 5, 5, 5,]
# ls.remove(5)
# print(ls)
# print(9 in ls)


# ls = [5, 1, 2, 3, 4, 5, 5]
# #ls.pop(0)
# print(ls.remove(5)) #None
# deleted = ls.pop()
# print(ls)
# print(deleted)

# update -----------------
# ls = [1, 'h', 3]
# print(ls)
# ls[1] = 2
# print(ls)
# ls.reverse()
# print(ls)
# print(ls[::-1])

# pizza = ['first_item', 'second_item', 'third_item', 'fourth_item', 'fifth_item']
# spisok = []

# for x in pizza:
#     if not x.startwith('f'):
#       spisok.append(x)

# print(spisok)


