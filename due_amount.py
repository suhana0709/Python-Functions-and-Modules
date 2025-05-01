total = int(input("Enter the total amount of bill: "))
paid = int(input("Enter the amount paid: "))
def due(total, paid):
    return total-paid
if paid==total:
    print("The money is already paid.")
elif(paid>total):
    change = paid-total
    print("You will get Tk",change," change.")
else:
    print("Your due is Tk ",due(total, paid))