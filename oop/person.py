"""
Abstraction
Encapsulation
Hiretage
Polimorfism : With a underscore "_" allows to use a variable and overwritte, All methods has the same behavior, but
each method can do it from his own way
"""

class Person:
    def __init__(self, name, age, ci, profession = "", children = 0):
        self.__children = children
        self.__profession = profession
        self.__ci = ci
        self.__age = age
        self._name = name

    def present(self):
        return f"Hi My Name is {self._name}"

    def get_name(self):
        return f"{self._name}"

    def __repr__(self):
        """
        Unique tring representation of a person
        :return:
        """
        return f"ci: {self.__ci}, Name: {self._name}, " \
               f"age: {self.__age}"

    def __lt__(self, other):  # Less than other
        return self._name < other._name and self.__ci < other.__ci

    def __gt__(self, other): # Greather than other
        return self.__ci > other.__ci

    def __le__(self, other): #less or equals than other
        return self.__ci <= other.__ci

    def __ge__(self, other): #Great or equals than other
        return self.__ci >= other.__ci

    def __eq__(self, other): # Is equals to other
        return self.__ci == other.__ci

    def get_ci(self):
        return self.__ci

    def __str__(self):
        """
        String representation of a Person
        :return:
        """
        return f"ci: {self.__ci}, Name: {self._name}, "\
               f"age: {self.__age}, profession: {self.__profession}, "\
               f"children: {self.__children}"

# juan = Person("Juan", 23, 123456, children = 2, profession = "Lawyer")
# pedro = Person("Pedro", 35, 657890, "Business Administrator")
# luis = Person(age=15, ci=254625, name="Luis")
#
# print(f"{juan}")
# print(f"{pedro}")
# print(f"{luis}")
#
# juan.__ci = 987456   ## Encapsulation , the object variables alwasy private = with "__ "(ej, this doesn't cahge initial ci value)
# print(f"juan: {juan}")