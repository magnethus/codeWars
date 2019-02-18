# Abstract Base Class
from abc import ABC, abstractmethod

class DataBase(ABC):
    def __init__(self):
        self.version = 1.0

    def get_name(self):
        return "Abstract Database"

    @abstractmethod
    def insert(self): ...

    @abstractmethod
    def update(self): ...

    @abstractmethod
    def delete(self): ...

    @abstractmethod
    def select(self): ...


class DatabaseObject(ABC):
    @abstractmethod
    def get_table(self): ...


#database = DataBase()