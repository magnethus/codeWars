a = [1, 2, 4]
print(a)
a.append("strgk")
print(a)
a.append([6, 7, 4])
print(a)
a.pop()
print(a)

print(a[0])
print(a[3])
a[3] = 200
print(a)

b = ["apple", "banana", "juice"]
temp = b[0]
b[0] = b[2]
b[2] = temp
print(b)

