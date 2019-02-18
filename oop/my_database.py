#all abstract methods must be implemented
from oop.abstract_clasess import DataBase
from oop.person import Person

class PersonDatabase(DataBase):
    def __init__(self):
        super().__init__()   # super can be called from any place byt be carefull #call the father methods
        self.version = 2.0
        super().get_name()
        self.__data = {
            # "students": [],
            # "professors": [],
            # "processes": {
            #     "first": 1
            # }
        }

    def insert(self, person): #insert an object an insert to self.data / añadir datos to a diccionary.agarrar datos de la persona e ir poniendo al diccionario
        self.__data[person.get_ci()] = person

    def delete(self, person):
        self.__data.pop(person.get_ci())

    def select(self, ci):
        return self.__data.get(ci)

    def update(self, person):
        self.__data[person.get_ci()] = person

    def print_data(self):
        print(f"Data: {self.__data}")

my_database = MyDatabase()
print(my_database.print_data())
juan = Person(name="Juan", ci=12312, age=30)
Jon = Person(name="Jon", ci=4534534, age=12)
my_database.insert(juan)
my_database.insert(Jon)
print(my_database.print_data())
my_database.delete(juan)
print(my_database.print_data())
my_database.select(4534534)

# my_database = MyDatabase()
# print(my_database.version)
# print(my_database.get_name())

#
# "123456":{
#     "name": "juan",
#     "age": 20
# }