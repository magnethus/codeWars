from oop.abstract_clasess import DatabaseObject
from oop.person import Person

class Professor(Person, DatabaseObject): #multiple heritage
    def get_table(self): # en que tabla se va guardar
        return "professors"

    def review_exams(self):
        print("Reviewing exams")

class Student(Person, DatabaseObject):
    def get_table(self):
        return "students"

    def present(self):
       return(f"Hi, Im a student and my name is {self._name}")

#     #Professor
# juan = Professor("Juan", 40, 123456, "Business Administrator")
# print(f"Juan: {juan}")
# print(f"{juan.present()}")
# juan.review_exams()
#
#     #Student
# luis = Student("Luis", 22, 123553)
# print(f"Luis: {luis}")
# print(luis.present())
#
# people = [luis, juan]
# print(f"{people}")
#
#     #For wednesday How to use sort in an object and make all the class that represent all the persons in Jalasoft, Selog, cafeteria, etc, etc
# people.sort()
# print(f"{people}")
#
# if juan <= luis:
#     print("Juan es menor a Luis")

# def transform(person):
#     return person.get_name()
#
# people.sort(key=lambda person: person.get_name())
# people.sort(key=transform)
#
# print(f"{people}")


