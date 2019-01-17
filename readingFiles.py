#r, a, w, r+ , readable,read,readline

#this works with employees.txt file

emfi = open("employees.txt", "r")
print(emfi.readlines()[2])
print(emfi.readline())
emfi.close()


emfi = open("employees.txt", "r")
for im in emfi.readlines():
    print(im)
emfi.close()