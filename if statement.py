
is_male = False
is_tall = False
if is_male and is_tall:
    print("You are a male and tall or both")
elif is_male and not(is_tall):
    print("Your are a male but not tall")
elif not(is_male) and is_tall:
    print("Your are not a male but you are tall")
else:
    print("You neither male or tall")
# comparator> !=, ==, >=, <=

def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
print(max_num(3, 100, 5))

