from oop.employee import Employee


class Selog(Employee):
    def reviewing_tasks(self):
        print("Doing tasks")


class Manager(Employee):
    def present(self):
        return (f"Hi, Im a manager, my name is {self._name}")


class Lead(Employee):
    def present(self):
        return (f"Hi, Im a lead, my name is {self._name}")


class Manual(Employee):
    def present(self):
        return (f"Hi, Im a BQE, my name is {self._name}")


class Automation(Employee):
    def present(self):
        return (f"Hi, Im an automation employee, my name is {self._name}")


# Selog
Irving = Selog("Juan", 40, 123456, "Cafeteria", 5)
print(f"Juan: {Irving}")
print(f"{Irving.present()}")
Irving.reviewing_tasks()

# Manager
Michelle = Manager("Michelle", 22, 123553, "Softlayer", 4)
print(f"Michelle: {Michelle}")
print(Michelle.present())

# Lead
Magdalena = Lead("Magdalena", 23, 343455, "Softlayer", 3)
print(f"Magdalena: {Magdalena}")
print(Magdalena.present())

# BQE
Alex = Manual("Alex", 21, 3454545, "Soflayer", 6)
print(f"Alex: {Alex}")
print(Alex.present())

# Automation
Ruber = Automation("Ruber", 25, 454645, "Softlayer", 5)
print(f"Ruber: {Ruber}")
print(Ruber.present())

# People
employees = [Irving, Michelle, Magdalena, Ruber, Alex]
print(f"{employees}")

# For wednesday How to use sort in an object and make all the class that represent all the persons in Jalasoft, Selog, cafeteria, etc, etc
employees.sort()
print(f"{employees}")




