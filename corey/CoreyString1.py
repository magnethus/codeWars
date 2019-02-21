message = "This is a test for strings"
print(message[3:10])
print(message.lower())
print(message.upper())
print(message.count("t"))
print(message.find("i"))
print(message.replace("strings", "Fun"))

first = "Hi"
second = "Im learning"
test1 = "{}, {}.Python!;".format(first, second)  # format
test2 = f"{first}, {second.upper()}.Python!;"   # f format and upper
print(test1)
print(test2)
print(dir(first)) # What does this method , Another form: print(help(str))
print(help(str.split)) # exactly what the method do