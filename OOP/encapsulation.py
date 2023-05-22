# инкапсуляция :
# 1. языковая констукция которая помогает связать данные с их методами для их обработки и управления (связь между данными и методами которая управляет ими) (класс - капсула)
# 2. механизм сокрытия при помощи которого можно ограничить доступ одного компанента программы к другому


# инкапсуляция как связь

# class Phone:
#     number = '+996700700700'

#     def print_number(self):
#         print(f'Мой номер: {Phone.number}')
#         print(f'Мой номер: {self.number}')

# my_phone = Phone()
# my_phone.print_number()


# инкапсуляция как механизм закрытия 
# 3 уравня закрытия данных в питоне
#     1. публичный(public) - number, print_number
#     2. защищенный(_protected) - _number
#     3. приватный(_private) - __number

# class Car:
#     _country = 'Germany'

#     def __init__(self) -> None:
#         self.marka = 'Mersedes-Benz' # public
#         self._model = 'w140' # protected
#         self.__color = 'gray'

# obj = Car()
# print(dir(obj))
# print(obj._Car__color)
# print(obj._country)
# print(obj._model)

# class Phone:
#     username = 'John'
#     _caller = 'Jamie'
#     __count_of_calls = 15

#     def call(self):
#         print(f'{self._caller} звонит вам!')
#         question = input('Взять трубку(yes/no):')
#         if question.lower().strip() == 'yes':
#             self.turn_on()
#         else:
#             print('сбросили трубку!')

#     def __increment_calls(self):
#         self.__count_of_calls += 1

#     def turn_on(self):
#         self.__increment_calls()
#         print('Aloo!')
#         print('Count of calls with {self._caller}: {self.__count_of_calls}')

# john = Phone()
# print(john.username)
# john.call()

# ------------------------------

# class Person:
#     def __init__(self,name,age) -> None:
#         self.name = name 
#         self.age = age
    
#     def display_info(self):
#         print(f'My name is {self.name} and I\'m {self.age} year old!')

# obj = Person('John', 18)
# obj.display_info()
# obj.nationality = 'Kyrgyz'
# print(obj.nationality)
# obj.age = -18
# obj.display_info()

# getter & setter
# они нужны чтобы избежать прямого обращения к закрытым аттрибутам при этом можно добавить логику валидация(проверки) данных которые будут установлены в аттрибут

# class Person:
#     def __init__(self,name,age) -> None:
#         self.__name = name 
#         self.__age = age
    
#     def display_info(self):
#         print(f'My name is {self.__name} and I\'m {self.__age} year old!')

#     #getter
#     def name(self):
#         return self.__name
    
#     #setter
#     def set_name(self, name):
#         if not isinstance(name, str):
#             print('Name must be str object!')
#         else:
#             self.__name = name

#     #getter
#     def name(self):
#         return self.__name
    
#     #setter
#     def set_age(self, age):
#         if not isinstance(age, int) or not 0 <= age < 150:
#             print('Invalid value for age!')
#         else:
#             self.__age= age

# obj = Person('John', 24)
# print(obj.name())
# obj.set_age(-18)
# obj.display_info()
# obj.set_age(55)
# obj.display_info()
# obj.set_age('Raychel')
# obj.display_info()
# print(obj.set_age())
