#all abstract methods must be implemented
from oop.abstract_clasess import DataBase

class MyDatabase(DataBase):
    def __init__(self, data):
        self.__dict__ = data

        self.version = 2.0
        # # super().get_name()
        self.data = {
            "students": {},
            "professors": {},
            "processes": {
                "first": 1
            }
        }

    def insert(self, person): #insert an object an insert to self.data / añadir datos to a diccionary.agarrar datos de la persona e ir poniendo al diccionario
            if person not in self.data:
                self.data.append(person)

    def delete(self):
        pass

    def select(self):
        pass

    def update(self):
        pass

#print(help(MyDatabase))
# my_database = MyDatabase("Alex", , 14232)
# my_database.insert(my_database)
# print(my_database.version)
# print(my_database.name)
# print(my_database.age)
# print(my_database.ci)
# print(my_database.get_name())

student1=MyDatabase("Jon", {23, 2323})
diictop1=MyDatabase("Jon", {22, 33535})

print(diictop1)

# "123456":{
#     "name": "juan",
#     "age": 20
# }

