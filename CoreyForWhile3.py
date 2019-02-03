
nums = [1, 2, 3]

for num in nums:
    if num == 2:
        print("Found!")
        continue
    print(num)

for num in nums:
    for letter in "a":
        print(num, letter)

for i in range(10):
    print(i)

x = 0
while x <= 10:
    if x == 5:
        break
    print(x)
    x += 1