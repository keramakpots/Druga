import random
import time
import sys
def trying(guessing, number, number_guess):
    guessing = input("What is your guess?")
    start_czas = time.time()
    if int(guessing) == number:
        number_guess += 1
        fin_time = round((time.time() - start_czas),[2])
        print("YES!!! "+ str(number) + " is my secret number! \n"
        "You quessed my number in  " + str(number_guess) + " guesses. Congratulations!!!"
        "It took you" + str(fin_time))

        exit = input("Do you want to play again? (yes or no)")
        if exit == 'yes' or exit == "Yes":
            guess(0,0)
        else:
            sys.exit()

    elif int(guessing) < number:
        print(str(guessing) + " is to low.")
        number_guess += 1
        trying(guessing,number, number_guess)
    elif int(guessing) > number:
        print(str(guessing) + " is to high.")
        number_guess += 1
        trying(guessing, number, number_guess)
def guess(quessing, number):
    print("Welcome in ***Guess the number*** game!")
    name = input("What is your name?")
    print("Well, " + name + " ,I'm thinking of a number between 1 and 30...")
    number = random.randrange(1,31)
    print(number)
    guessing = 0
    number_guess = 0

    trying(guessing,number, number_guess)




guess(0, 0)
