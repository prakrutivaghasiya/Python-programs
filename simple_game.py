import random

    guess_number = random.randint(0,30)

    i = 0
    while i < 5 :
        print ("Enter your guess")
        number = int(input())

        if guess_number < number :
            print ("Number is high. Guess low!!")
        elif guess_number > number :
            print ("Number is low. Guess high!!")
        else:
            print ("You won.")
            break
        i = i + 1

    if i == 5 :
        print ("You Lost")
        print("Number was:")
        print(guess_number)
