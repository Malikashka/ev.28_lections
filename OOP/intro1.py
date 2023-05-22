# # OOП - объектно-ориентирование програмирование 

# # Класс - описание того как должен выглядеть объект то есть в классе мы описываем какими свойствами(данными) и поведением(функции) должен обладать объект

# # Объект - сущность которую мы создаем от класса у объекта есть собственные состояния свойств(данные) 

# # Целью создания было создать данные с функциями которую управляли этими данными

# # Свойствами(аттрибутами) - называют обычные переменные внутри класса  в которых  хранятся данные объекта 

# # Методы - обычные функции внутри класса методы описывают поведение объекта

# # ----------------------------

# class Human:
#     age = 0
#     def __init__(self,first_name, last_name, job, citizenship):
#         self.name = first_name + ' ' + last_name
#         self.job = job
#         self.citizen = citizenship

#     def show_info(self):
#         return f'Name: {self.name}, Age: {self.age}, Job: {self.job}, Citizen: {self.citizen}'
    
# john = Human('John', 'Snow', 'King of North', 'Northerner')
# bilal = Human('Bilal', 'Lanister', 'Programmist', 'KR')

# # print(john, type(john))
# # print(dir(john))

# print(john.show_info())
# john.age = 24
# print(john.show_info())
# john.job = 'King of Westeros'
# print(john.show_info())
# print()
# print(bilal.show_info())

# ---------------------------
# class Dog:
#     age = 0
#     ushi = True

#     def __init__(self,name,color) -> None:
#         "Инициализатор, именно здесь создаются атрибуты объекта"
#         # self - ссылка на объект который только что создался 
#         self.name = name
#         self.color = color

#     def bark(self):
#         print(f'{self.name} лает!')

#     def show_info(self):
#         print(f'Name: {self.name}, Age: {self.age}, color: {self.color}, ushi: {self.ushi}')
    


# rex = Dog('Rex','black')
# pluto = Dog('Pluto', 'brown')
# aktosh = Dog('Aktosh', 'gray')

# rex.show_info()
# pluto.show_info()
# aktosh.show_info()


# rex.age = 2
# pluto.age = 5
# aktosh.age = 3
# aktosh.ushi = False


# rex.show_info()
# pluto.show_info()
# aktosh.show_info()

# rex.bark()
# pluto.bark()

# ---------------

# class Human:
#     def __init__(self):
#         print('Init worked!')
#         self.raychel = 'raychel'
#         self.golod = 100

#     def eat(self, meal, doela = True):
#         print(f"{self.raychel} покушала {meal}")
#         if doela:
#             self.golod -=50
#         else:
#             self.golod -= 25
        

# obj = Human()
# print(obj.raychel, obj.golod)
# obj.eat('burger', doela = False)
# print(obj.raychel, obj.golod)
# obj.eat('kruasan')
# print(obj.raychel, obj.golod)

        





