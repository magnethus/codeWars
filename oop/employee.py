"""
Abstraction
Encapsulation
Hiretage
Polimorfism : With a underscore "_" allows to use a variable and overwritte, All methods has the same behavior, but
each method can do it from his own way
"""

class Employee:
    def __init__(self, name, age, ci, area="", workhour=0):
        self.__area = area
        self.__workhour = workhour
        self.__ci = ci
        self.__age = age
        self._name = name

    def present(self):
        return f"Hi My Name is {self._name}"

    def __repr__(self):
        """
        Unique tring representation of a person
        :return:
        """
        return f"{self._name}"

    def get_my_key(customobj):
        return customobj["name"]

    def __str__(self):
        """
        String representation of a Person
        :return:
        """
        return f"ci: {self.__ci}, Name: {self._name}, "\
               f"age: {self.__age}, area: {self.__area}, "\
               f"workours: {self.__workhour}"