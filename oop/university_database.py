from oop.abstract_clasess import DataBase
from oop.university import Professor

class UniversityDatabase(DataBase):
    def __init__(self):
        self.__data = {}
        # {"12312312": person}
        # {"professors": [],
        #     "students":[]
        # }



    def insert(self, university_person):
        table = university_person.get_table()
        if table in self.__data:
            self.__data[table].append(university_person)
        else:
            self.__data[table] = [university_person]

    def update(self): ...


    def delete(self): ...


    def select(self, database): ... # make work this for monday-- Insertar un diccionario dentro de otro diccionario
        professors

    def print_data(self):
        print(f"Data: {self.__data}")

database = UniversityDatabase()
professor = Professor(name="Liu", age=33, ci= 123123, profession="Ing. Sistemas")
professor2 = Professor(name="Max", age=55, ci= 645566, profession="Business Administrator")
database.insert(professor)
database.insert(professor2)
print(database.print_data())
database.select()
print(database.print_data())