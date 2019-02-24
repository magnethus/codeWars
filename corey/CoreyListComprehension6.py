nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#I want  "n" for each "n" in nums

my_list = []
for n in nums:
    my_list.append(n)
print(my_list)

my_list = [n for n in nums]
print(my_list)

# I want "n*n" for each "n" in nums

my_list = []
for n in nums:
    my_list.append(n*n)
print(my_list)

my_list2 = [n*n for n in nums]
print(my_list2)

# my_list = []
# my_list3 = map(lambda n: n*n, nums)
# my_list3lamda = my_list3
# print(my_list3lamda)

# I want "n" for each "n" in nums if "n" is even
my_list = []
for n in nums:
    if n%2 == 0:
        my_list.append(n)
print(my_list)

my_list = [n for n in nums if n%2 == 0]
print (my_list)

# my_list = filter(lambda n: n%2 == 0, nums)
# print (my_list)

# I want a (letter, num) pair for each letter  in "abcd" and each number in "0123"

my_list = []
for letter in "abcd":
    for num in range(4):
        my_list.append((letter, num))
print (my_list)

my_list = [(letter, num) for letter in "abcd" for num in range(4)]
print (my_list)

#Diccionary comprehensions:
names = ["Bruce", "Clarck", "Peter", "Logan", "Wade"]
heros = ["Batman", "Superman", "Spiderman", "Wolverine", "Deadpool"]
# print (zip(names, heros))
# I want a dict{"name", "hero"} for each name,hero in zip(names, heros)
#my_dict = {}

#Set comprehensions
nums = [1,1,2,1,3,4,3,4,5,5,6,7,8,7,9,9]
my_set = set()
for n in nums:
    my_set.add(n)
print(my_set)

my_set = {n for n in nums}
print(my_set)

#Generator expressions
#I want to yield "n*n" for each "n" in nums
nums = [1,2,3,4,5,6,7,8,9,10]

#Generator 1
def gen_func(nums):
    for n in nums:
        yield n*n

my_gen = gen_func(nums)
for i in my_gen:
    print (i)
    
#Generator 2
my_gen2 = (n*n for n in nums)
for i in my_gen2:
    print (i)
