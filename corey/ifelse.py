# Comparision
# Equal ==
# Not equal !=
# Greather than >
# Leass Than <
# Greather or Equal >=
# Less or Equal <=
# Object identifier is
# and
# or
# not

languaje = "Java"
if languaje == "Python":
    print("Languaje is Python")
elif languaje == "Java":
    print("Languaje is Java")
elif languaje == "JavaScript":
    print("Languaje is JavaScript")
else:
    print("No match")

user = "Admin"
logged_in = False

if not logged_in:
    print("Admin page")
else:
    print("Bad Creds")

a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)
print(a is b)
print(id(a))
print(id(b))

# False values:
# -False
# -None
# -Zero of any numeric  type
# -Any empty sequence, for example "". {}. []
# -Any empty mapping, for example {}

condition = {}

if condition:
    print("Evaluate to True")
else:
    print("Evaluate to False")