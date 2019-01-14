

try:
    value = 10 / 0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError:
    print("Division by cero, this is not allowed")
except ValueError:
    print("Invalid Error")

#best practice is caching all

try:
    value = 10 / 0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("Invalid Error")
