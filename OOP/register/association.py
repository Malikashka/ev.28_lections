# Ассоциация - принцип ООП в котором два класса связаны друг с другом. Связь обозначает то что внутри одного объекта будет существовать другой объект от другого класса
# агрегация - слабая связь
# композиция - сильная связь

# class Battery:
#     _power = 100

#     def charge(self):
#         if self._power < 100:
#             self._power = 100

# class Iphone:
#     def __init__(self,color) -> None:
#         self.color = color
#         self.battery = Battery()
#         # когда мы создаем внутри класса объект от другого класса - композиция

# a = Iphone('gold')
# a.battery._power -= 50
# print(a.battery._power)
# a.battery.charge()
# print(a.battery._power)


# class Nokia:
#     def __init__(self,battery: Battery,color: str):
#         self.color = color
#         self.battery = battery
#         # когда объект сохздается из вне класса и передается внутрь - агрегация

# battery = Battery()
# nokia1 = Nokia(battery,'gray')
# print(nokia1.battery._power)
# del nokia1

# nokia2 = Nokia(battery, 'black')
# # при удалении объекта Nokia батарейка остается

#--------------------------------

# Композиция
# class Wall:
#     def __init__(self, direction) -> None:
#         self.type = direction

#     def __str__(self) -> str:
#         return f'{self.type}'

# class Room:
#     def __init__(self):
#         self.west_wall = Wall('west')
#         self.east_wall = Wall('east')
#         self.south_wall = Wall('south')
#         self.north_wall = Wall('north')

# obj = Room()
# print(obj.west_wall)

#--------------------------
# Агрегация
# class Stream:
#     def __str__(self) -> str:
#         return 'Stream object'
    
# class Logger:
#     def __init__(self, stream=None) -> None:
#         self.stream = stream

#     def print_the_logs(self):
#         if self.stream:
#             print(f'Stream from class: {self.stream}')
#         else:
#             print('None stream')

# stream1 = Stream()
# logger1 = Logger(stream1)
# logger2 = Logger(stream1)

# logger3 = Logger(stream=Stream())

# logger1.print_the_logs()
# logger2.print_the_logs()

#----------------------------

# class Engine:
#     country = 'Germany'

#     def __init__(self, power) -> None:
#         self.power = power

#     def __str__(self) -> str:
#         return f'Power: {self.power}'
    
# class AudiCar:
#     brand = 'Audi'
#     country = 'Germany'

#     def __init__(self,model,power) -> None:
#         self.engine = Engine(power)
#         self.model = model

#     def __str__(self) -> str:
#         return f'{self.brand}{self.model} -> Engine: {self.engine} -> engine country: {self.engine.country}'
    
# car = AudiCar('A8', 400)
# print(car)





list_ = [1, 2, 3, 4, 5] 
new_list = [] 
for x in list_: 
    if x % 2 == 0: 
        x = 'четное' 
    new_list.append(x) 
else:
        x = 'нечетное' 
new_list.append(x) 
print(new_list)