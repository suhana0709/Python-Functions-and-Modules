def sum(num1, num2):
    return num1 + num2
def sub(num1, num2):
    return num1 - num2
def mul(num1, num2):
    return num1*num2
def div(num1, num2):
    if num2 != 0:
        return num1/num2
    else:
        print("Division by zero is not allowed.")

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
print("\n Addition:", sum(num1, num2))
print("Subtraction:", sub(num1, num2))
print("Multiplication:", mul(num1, num2))
print("Division", div(num1, num2))
