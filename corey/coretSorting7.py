li = [9, 1, 8, 2, 7, 3, 6, 4, 5]
s_li = sorted(li) # Sorted creates a new variable
s_li = sorted(li, reverse = True)
print("Sorted Variable:\t", s_li)
li.sort(reverse = True)   # Sorted the list in the place
print("Sorted Variable:\t", li)

tup = (9, 1, 8, 2, 7, 3, 6, 4, 5)
s_tup = sorted(tup)
print("Tuple\t", s_tup)

di = {"name":"Corey", "Job":"Programming", "age": None, "os": "Mac"}
s_di = sorted(di)
print("Dict\t", s_di)

li = [-6, -5, -4, 1, 2, 3]
s_li = sorted(li, key = abs) # absolute variable .build in function that helps to sort
print(s_li)

class Employee():
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self. salary = salary

    def __repr__(self):
        return (f"{self.name},{self.age}.{self.salary}")

from operator import attrgetter

e1 = Employee("Carl", 37, 70000)
e2 = Employee("Sarah", 54, 34000)
e3 = Employee("Karl", 23, 55000)

employees = [e1, e2, e3]
#Sort 1
def e_sort(emp):  # sort by name .build in function that helps to sort
    return emp.name

s_employees = sorted(employees, key = e_sort)
print(s_employees)

#Sort 2
s_employeeswithlambda = sorted(employees, key = lambda e: e.age)
print(s_employeeswithlambda)

#Sort 3
s_employeeswithattr = sorted(employees, key = attrgetter("salary"))
print(s_employeeswithattr)
