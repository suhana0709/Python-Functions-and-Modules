try:
    num= int(input("Enter a number: "))
    if num%2 == 0:
        print("Number is even.")
    else:
        print(("Number is odd."))

except ValueError as ex:
    print("It is said to enter a number.")

