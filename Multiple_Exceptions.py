try:
 num1, num2 = eval(input("Enter two numbers, and seperate it with a comma: "))
 result = num1/num2
 print(result)

except ZeroDivisionError:
 print("Division by zero is not allowed.")

except SyntaxError:
 print("Must put comma to seperate the numbers.\nLike this: 1, 2")

else:
 print("No error.")

finally:
 print("Thank you!😁🥳")