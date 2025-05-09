import random
playing = True
number = str(random.randint(10,20))

print("I will guess a number from 10 to 20 and you will have to guess it.")

while playing:
    guess = int(input("Enter your guess: "))
    if number == guess:
        print("Yay! You WON!🏳️‍🌈🚩🏁🏁🏁❗❗❗🥳🥳🥳 ")
        print("The number was ", number)
        break
    else:
        print("Your guess is wrong!!!!!!!!!!! TRY AGAIN!!!!!")
