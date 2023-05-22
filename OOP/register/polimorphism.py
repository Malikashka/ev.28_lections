# функция полиморфизм -> len(): __len__
# print(len('Makers'))
# print(len([1,2,3,5]))
# print(len({1:2,4:5}))

# + (__add__) - метод полиморфизм
# print(5 + 5)
# print('hello' + 'Hello')
# print([1,2,3] + [4,5,6])

# полиморфизм - это способность функции(метода) использлваться для разных типов(классов)
# широко распрастраненное определение: "один интерфейс - много реализаций"
# list.pop
# set.pop
# dict.pop


# class Cat:
#     def __init__(self,name,age) -> None:
#         self.name = name 
#         self.age = age

#     def info(self):
#         print(f'It\'s a cat. Cats name is {self.name}, age: {self.age}')

#     def make_sound(self):
#         print('Meow, meow!')

# class Dog:
#     def __init__(self,name,age) -> None:
#         self.name = name 
#         self.age = age

#     def info(self):
#         print(f'It\'s a cat. Cats name is {self.name}, age: {self.age}')

#     def make_sound(self):
#         print('Bark, bark!')

# cat = Cat('Garfild',5)
# dog = Dog('Pluto', 6)

# for obj in (cat, dog):
#     obj.info()
#     obj.make_sound()
        

# from math import pi

# class Shape:
#     def __init__(self, name):
#         self.name = name

#     def fact(self):
#         return f'Я фигура в двумерной плоскости:{self.name}!'
    
# class Square(Shape):
#     def __init__(self, length) -> None:
#         super().__init__('Квадрат')
#         self.length = length

#     def area(self):
#         return self.length ** 2
    
#     def fact(self):
#         return super().fact() + '\ny квадрата все стороны равны и углы равны 90 градусам!'
    

# class Circle(Shape):
#     def __init__(self, radius) -> None:
#         super().__init__('Окружность')
#         self.radius = radius

#     def area(self):
#         return pi * self.radius ** 2
    
# a = Square(8)
# b =  Circle(4)

# print(a.fact())
# print(a.area())

# print(b.fact())
# print(b.area())


