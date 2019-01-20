import string
def toJadenCase(string):
    for i in string:
         print (i)
         return;

a = "ow can mirrors be real if our eyes aren't real"

toJadenCase(string.capwords(a))


string.capwords("they're bill's friends from the UK")


friends = ['Broken', 'Master', 'BlackStar', 'This is a list element']

print(friends[1:2]) # Two is not included
friends[1]= 'Katherin'
friends[2]= 78
print(friends[1])
print(friends[2])

lucky_numbers = [5, 8, 15, 48, 66, 89]
friends = ['Broken', 'Master', 'BlackStar', 'Legend', 'Topson']
friends.extend(lucky_numbers) # concatenate two lists
print(friends)
friends.append("Huskar") # Insert the element Huskar to the list
friends.insert(5, "Axe") # Insert the element Axe in 5 index
friends.remove('Huskar') # Remove the Huskar element
# friends.clear() this only with python 3.3. above
print(friends)
print(friends.index('BlackStar')) #If Master is in the list return the index

friends = ['Broken', 'Master', 'Master', 'BlackStar', 'Legend', 'Topson']
print(friends.count('Master'))  # Count how many times appears Master in the list
friends.pop() # Delete the last element in the list
print(friends)
friends.sort()
lucky_numbers.sort()
print(friends)
print(lucky_numbers)
friends.reverse()
lucky_numbers.reverse()
print(friends)
print(lucky_numbers)

friends = ['Broken', 'Master', 'Master', 'BlackStar', 'Legend', 'Topson']

def phrases_test(phrase):
    change = ""
    for i in phrase:
        if i in "aeiou":
            change = change + "P"
        else:
            change = change + i
    return change

print(phrases_test("This is a test for phrase"))


#name = input("Enter your name: ")
#new_letter = ""
#verif = "Rambo"
#for i in name:
#    if i not in verif:
#        new_letter += i
#        print("A new letter is created", new_letter)
#print("your name is: " + new_letter)
#print("")
#print("Enter to exit")

Pep = "This is a test"
print(str(Pep))
print(Pep)

count = 0
while count < 2:
    print("This is a test for a while statement")
    count +=1
else:
    print("Your pass number 2")

l = ["apple", "banana", "pine"]
for i in l:
    print(i)

l = ["Rain", "snow", "wind"]
for i in range(len(l)):
    print(l[i])
---------------------------------EXERCICIEs-----------------

1. the max and the mix
