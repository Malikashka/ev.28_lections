# class methods, instans methods, static methods

# instance ,ethods - обычные методы которые принимают первым аргументом self(ссылка на объект). Нужны они чтобы внутри метода мы могли работать с аттрибутами объекта, получать их или изменять

# class Test:
#     def instance_method(self,a):
#         print('метод объекта')
#         print('первый аргумент:', self)

# obj = Test()
# obj1 = Test()
# obj.instance_method(5) #если вызвать у объекта то в self передается автоматически
# Test.instance_method(obj, 5) # если вызвать у класса то в self нужно передавать объект в ручную
# obj1.instance_method(5)

# class methods - методы которые принимают первым аргументом cls(ссылка на класс). Нужны они для создания или изменение аттрибутов класса и для манипуляции с классом внутри метода. Создается при помощи декоратора @classmethods

# class Test:
#     @classmethod
#     def class_methods(cls,a):
#         print('метод класса')
#         print('первый аргумент:', cls)

# obj = Test()
# print(Test, '!!!')
# print()
# obj.class_methods(5)
# print()
# Test.class_methods(5)

# class C:
#     counter = 0

#     def __init__(self) -> None:
#         self.a = 4

# obj_1 = C()
# obj_2 = C()
# obj_3 = C()

# print('obj_1',obj_1.counter)
# print('obj_2',obj_2.counter)
# print('obj_3',obj_3.counter)

# obj_1.counter += 1
# print()
# print('obj_1',obj_1.counter)
# print('obj_2',obj_2.counter)
# print('obj_3',obj_3.counter)

# C.counter += 5

# print('obj_1',obj_1.counter)
# print('obj_2',obj_2.counter)
# print('obj_3',obj_3.counter)


# class C:
#     counter = 0

#     def __init__(self) -> None:
#         self._inc_counter()
#         self.a = 4

#     @classmethod
#     def _inc_counter(cls):
#         cls.counter += 1

# obj1 = C() #1
# obj2 = C() #2
# obj3 = C() #3
# print(obj3.counter)
# obj4 = C() #4
# print(obj1.counter)
# print(obj2.counter)
# print(obj3.counter)
# print(obj4.counter)


# class Pizza:
#     def __init__(self,radius,*ingredients) -> None:
#         self.r = radius
#         self.ingredients = ingredients
    
#     def cook(self):
#         print(f'готовиться пицца размером {self.r*2} cm')

#     @classmethod
#     def four_cheese(cls, r):
#         pizza = cls(r,'моцарелла', 'голландский', 'дарблю', 'брынза')
#         return pizza

#     def __str__(self) -> str:
#         return f'{self.r} cm -> ' + ', '.join(self.ingredients)

# pizza1 = Pizza(20, 'пепперони','грибы', 'моцарелла')
# # pizza2 = Pizza(15, 'моцарелла', 'голландский', 'дарблю', 'брынза')
# # pizza3 = Pizza(20, 'моцарелла', 'голландский', 'дарблю', 'брынза')
# # pizza4 = Pizza(10, 'моцарелла', 'голландский', 'дарблю', 'брынза')
# pizza2 = Pizza.four_cheese(15)
# pizza3 = Pizza.four_cheese(20)
# pizza4 = Pizza.four_cheese(10)
# pizza5 = Pizza(20, 'пепперони','грибы', 'моцарелла', 'оливки')
# print(pizza1)
# print(pizza2)
# print(pizza3)
# print(pizza4)
# print(pizza5)


# class Person:
#     surname = 'Stark'

#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

#     def info(self):
#         print(f'{self.name} {self.surname} -> Age: {self.age}')

#     @classmethod
#     def from_birth_year(cls,name,birth_date):
#         from datetime import date
#         age = date.today().year - birth_date
#         return cls(name, age)
    

# obj = Person('John', 24)
# obj.info()
# obj2 = Person('Sansa', 19)
# obj2.info()
# obj3 = Person.from_birth_year('Rob', 1996)
# obj3.info()

# from datetime import datetime, date
# a = datetime.now()
# print(a.strftime('%H:%M:%S'), type(a))

#staticmethod - это те методы в классе которые не принимают в качестве аргументов ни класс ни объект так называемые методы которые не изменяют состояние

# class C:
#     @staticmethod
#     def static_method():
#         print('статический метод!')

# obj = C()
# obj.static_method(5)
# C.static_method(5)

# class Cylinder:
#     def __init__(self, radius, height) -> None:
#         self.area = self.get_area(radius, height)

#     @staticmethod
#     def get_area(r,h):
#         from math import pi
#         circle = pi * r ** 2
#         side = pi * h *(r * 2)
#         area = circle * 2 + side
#         return  round(area, 2)
    
# obj = Cylinder(10, 7)
# print(f'Area: {obj.area}')

# obj1 = Cylinder(3,12)
# print(f'Area: {obj1.area}')





