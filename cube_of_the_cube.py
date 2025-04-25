def cube(num):
    return num*num*num

def by_three(num):
    if num %3 == 0:
        return cube(num)
    else:
        return False
num = int(input("Enter the number: "))
print("If the number is divisible by 3 then, the cube of the number will be displayed.")
print(cube(num))