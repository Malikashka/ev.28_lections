# """
# абстракция
# """
# #абстаркция (абстрактный класс) - принцип ООП в котором создается абстрактный класс (класс - пустышка)в котором задаются названия аттрибутов и методов для того чтобы в дочерних классах переопределить их нужным образом(у нас есть название но нет логики)

# from abc import ABC, abstractmethod, abstractproperty

# class AbstractAnimal(ABC):
#     @abstractmethod
#     def voice(self):
#         ...

#     @abstractproperty
#     def legs(self):
#         ...

# ob = AbstractAnimal()TypeError: Can't instantiate abstract class AbstractAnimal with abstract methods legs, voice

# class Dog(AbstractAnimal):
#     ...

# obj = Dog()TypeError: Can't instantiate abstract class AbstractAnimal with abstract methods legs, voice

# class Dog(AbstractAnimal):

#     def voice(self):
#         print('gav gav')
    
# obj = Dog() #TypeError: Can't instantiate abstract class AbstractAnimal with abstract methods legs

# class Dog(AbstractAnimal):
#     legs = 4

#     def voice(self):
#         print('gav gav')


# obj = Dog()
# obj.voice()
# print(obj.legs)



#@abstactmethod - декоратор который требует переопределение метода в наследуемом классе 

#@abstactproperty - декоратор который требует переопределение аттрибутов класса


# class Shape(ABC):
#     def __init__(self,name):
#         self.name = name

#     @abstractmethod
#     def area(self):
#         ...

# class Square(Shape):
#     def __init__(self, lenght):
#         super().__init__('Square')
#         self.lenght = lenght

#     def area(self):
#         return self.lenght ** 2
# obj = Square(12)
# print(obj.name)
# print(obj.area())

# class Dog(AbstractAnimal):
#     legs = 4
#     def voice(self):
#         print('gav gav')



# class Cat(AbstractAnimal):
#     legs = 4

#     def voice(self):
#         print('meow')

# dog = Dog()
# cat = Cat()
# arr = [dog, cat]
# for i in arr:
#     i.voice()
#     print(i.legs)




# 1)Создайте два класса A и B. В обоих классах есть метод count. В классе A он подсчитывает, сколько гласных букв в 
# слове, которое передается в качестве аргумента в методе count, а в классе B он подсчитывает количество согласных. 
# Создайте объекты от этих классов. 
# С помощью list comprehension создайте список из результатов работы метода count обоих объектов.

# !!!! 
# Обязательное условие: если в классе A или B не переопределить метод count должна выйти ошибка
# !!!!




