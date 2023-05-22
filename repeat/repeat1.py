# num1 = 1

# while num1 >= 0:
#     num1 = input('Vvedite chislo: ') #int('54') #54t
#     if num1[0] == '-' and num1[1:].isdigit():# -51
#         num1 = int(num1)
# else:
#     num1 = 1

# print('Встретилось отрицательное число!')

#---------------------------------------------------------------------

# from random import randint

# ls = []
# for x in range(0,100):
#     ls.append(randint(0,100))

# res = []
# for x in ls: 
#     if x not in res:
#       res.append(x)

# print(res, len(res))

#----------------------------------------------------------------------

# x1 = int(input('Vvedite 1 coordinatu gde stoit ladya:'))
# y1 = int(input('Vvedite 2 coordinatu gde stoit ladya:'))
# ladya = [x1, y1] # 2, 5


# x2 = int(input('Vvedite 1 coordinatu kuda idet ladya:'))
# y2 = int(input('Vvedite 2 coordinatu kuda idet ladya:'))
# target = [x2, y2] # 4, 6

# if x1 == x2 or y1 == y2:
#     print(True)
# else:
#     print(False)

#-----------------------------------------------------------------------

# import random
# ls = ['Plov', 'Besh', 'Kuurdak', 'Oromo', 'Lagman']
# p = 0
# b = 0
# k = 0
# o = 0
# l = 0

# for x in range(0, 1_000_000):
#     meal = random.choice(ls)
#     # print(meal)
#     if meal.lower() == 'plov':
#         p += 1
#     elif meal.lower() == 'besh':
#         b += 1
#     elif meal.lower() == 'kuurdak':
#         k += 1
#     elif meal.lower() == 'oromo':
#         o += 1
#     elif meal.lower() == 'lagman':
#         l += 1
#     else:
#         l += 1

# print('Результаты голодных игр:')
# # print(f'Plov: {p}\nBesh: {b}\nKuurdak: {k}\nOromo: {o}\nLagman: {l}')
# dict_ = {'Plov': p,'Besh': b,'Kuurdak': k,'Oromo': o, 'Lagman': l}
# print(dict)
# res = sorted(dict_.items(), key=lambda x: x[1], reverse=True)[0]
# print(f'Победило блюдо {res[0]} и оно набрало: {res[1]} очков')

#------------------------------------------------------------------------------

# Givven an array integers nums and an integers target, return undices of the two makers such that they add up to target.

# 1) nums = [2, 7, 11, 15]
# target = 9
# 0, 1 ------------------ 2 + 7 = 9

# 2) nums = [4, 11, 2, 5, 1, 6]
# target = 8
# 2, 5 ------------------ 2 + 6 = 8
                        # 8 - 4 = 4
                        # 8 - 11 = -3
                        # 8 - 2 = 6

# import numbers


# nums = [4, 11, 2, 5, 1, 6]
# target = 8

# for i in range(0, len(nums)):
#     num = target - nums[i]
#     if num in nums:
#         if num != nums[i]:
#          print(f'Otvet: {i}, {nums.index(num)}')
#          break



    


