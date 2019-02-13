def hello_func():
    print("Hello function!")

hello_func()


def hello_funct():
    return "Hello functionality!"

print(hello_funct().upper())

print(len("This is a test"))
print(range(len("This is a test")))

#Format 1
def hello_functi(greeting, name = "You"):
    return "{}, {}".format(greeting, name)

print(hello_functi("Hi", name = "Alex"))

#Format 2 , more cool :)
def hello_functio(greeting, name = "You"):
    return f"{greeting}, {name}"

print(hello_functio("Hi", name = "Arminda"))

#Return a tuple and a diccionary
def studen_info(*args, **kwargs):
    print(args)
    print(kwargs)

studen_info("History", "Math", name = "Roland", age = 21)


#Return a tuple and a diccionary in another way
def studen_info(*args, **kwargs):
    print(args)
    print(kwargs)

courses = ('English', 'Literature')
info = {'name': 'Liam', 'age': 2}

studen_info(*courses, **info)