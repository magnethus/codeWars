# Abstract Base Class
from abc import ABC, abstractmethod

class DataBase(ABC):
    def __init__(self, name, age, ci):
        self.name = name
        self.age = age
        self.ci = ci
        self.version = 1.0

    def get_name(self):
        return "Abstract Database"

    @abstractmethod
    def insert(self, person): ...

    @abstractmethod
    def update(self): ...

    @abstractmethod
    def delete(self): ...

    @abstractmethod
    def select(self): ...

#database = DataBase()