# Set() - множество 
# Это изменяемые неупорядочный, итерируемый неиндексируемый тип данных

# Множества хранят в себе только не изменяемые типы данных

# a = 'febw'
# print(hash(a))

#1 -> set()
# a = set([1, 2, 3, 4])
# print(a)

# a = set({1:2, 3:4})
# print(a)

#2 -> {}
# set2 = {1, 2, 3}
# print(set2)

# set1 = {1, 2, 3 ,3}
# print(set1)

# Frozenset - неизменяемое множество

# set1 = {1,}
# print(type(set1))

# set1 = {1, 0, False, True}
# print(set1)

# a = 0
# print(bool(a))

# Методы set
# add -> для добавления 

set1 = {1, 2, 3}
# set1.add(4)
# print(set1)
# set1.add((1, 2 ,3 ,4, 5))
# print(set1)

#update - он может добавлять но не повторяя имеющееся и добавляет все итерируемые 

# set1.update({3: '1', 4: '5'})
# print(set1)
# #set1.update('string', {1, 2, 3, 4, 5, 6, 7})
# print(set1)

# # set1.update([1,23,2])
# # print(set1)

# Удаление в set 

# clear - очищает все множества
# remove(element) - удаляет элемент если его нету выдает ошибку
# dickard - если элемента  нету ничего не происходит
# pop() - удаляет из set(FIFO) first in first out

# set1.remove(2)
# print(set1)

# set1.clear()
# print(set1)
# set1.discard(3)
# print(set1)

# Difference - выводит отличия
set1 = {1, 2, 3, 4, 5}
set2 = {2, 3, 5, 7}
# print(set1.difference(set2))
# print(set1 - set2)
# set2.difference(set1)
# print(set2 - set1)

# a = set1.symmetric_difference(set2)
# print(a)
# print(set1^set2)

# set1.symmetric_difference_update(set2)
# print(set1)

# Intersection
# print(set1.intersection(set2))
# print(set1 | set2)

# print(set1.union(set2))
# print(set1 | set2)


# num = list(input())
# print(len(num) == len(set(num)))


# tuple - неизменяемый, индексируемый , итерируемый, упорядочный тип данных
#index(element) - возвращает индекс этого элементы в кортеж
# #литералы ()
# a = (True, 'a', 1)
# # print(a, type(a))
# b = tuple()
# #count() -  возвращает число вхождений этого элемента в кортеж
# # print(a.count(True))

# robert = {5, 7, 11, 10, 28} 
# kail = {1, 5, 14, 8, 22} 
# merri = {19, 20, 3, 11, 10}
# if (robert.intersection(kail)) or (robert.intersection(merri)): 
#     print(robert&kail, robert&merri,'kail merri') 
#     else:
#   print('no one')

num1 = 1
num2 = 2
num3 = 3
if num2 == num1:
    print('num2 == num1')
elif num3 == num1:
    print('num3 == num1')
elif num2 == num1 and num3 == num1:
    print('num3')
else:
    print(False)