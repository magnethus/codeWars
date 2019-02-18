import unittest
from oop.university import Professor
from oop.university_database import UniversityDatabase


class MyTestCase(unittest.TestCase):
    def test_insert_when_database_is_empty(self):
        #AAA - Arrange, Act, Assert
        #Arrange
        university_database= UniversityDatabase()
        juan = Professor("juan", 10, 653232)

        #Act - que es lo que queremos probar - just one action
        university_database.insert(juan)

        #Assert - comprobar q la accion hizo lo que tenia q hacer
        actual = university_database.select(653232)
        self.assertEqual(juan, actual)

    # def test_something(self):
    #     self.assertEqual(True, False)

    def test_select_when_database_is_not_empty(self):
        #AAA - Arrange, Act, Assert
        #Arrange
        juan = Professor("juan", 10, 653232)

        #Act - que es lo que queremos probar - just one action
        university_database.select(juan)

        #Assert - comprobar q la accion hizo lo que tenia q hacer
        actual = university_database.select(653232)
        self.assertEqual(juan, actual)

    # def test_something(self):
    #     self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()