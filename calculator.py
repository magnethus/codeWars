#imput tries to evaluate the string in python2
#in python 2 raw_input doesn't evaluate the user entering
#this is made with python 2
#for python 3 use just input()

num1 = float(input("Enter your first number: "))
op = raw_input("Enter your operator: ")
num2 = float(input("Enter your second number: "))

if op == "+":
    print(num1 + num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    print(num1 / num2)
elif op == "-":
    print(num1 - num2)
else:
    print("Invalid operator")


