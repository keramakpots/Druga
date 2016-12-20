import random
import sys
print("Welcome in a ***Guess the number*** game!")

name = input("What's your name?")
def game():
    print("I'm thinking", name," of a number between 1 and 30.")
    numbers = list(range(1,31))
    number = random.choice(numbers)
    guess = input()
    while True:
        try:
            guess = int(guess)
            if guess == number:
                print("Yes!", guess,"is my secret number! Congratulation!\n")
                new_game = input("Do you want to play again? yes/no:")
                if new_game == 'yes':
                    game()
                else:
                    exit = input("Press any key to exit:")
                    if exit or not exit:
                        sys.exit()
            elif guess < number:
                print("=>", guess,"is to low.")
                guess = input()
            elif guess > number:
                print("=>", guess, "is to high.")
                guess = input()

        except ValueError:
            print("You must enter a number")
            guess = input()
game()
