def start():
    number = int(input('Choose a number for your friend to guess: '))
    if len(str(number)) > 3 and number < 3:
        print("Number to guess has to have 3-digits.")
        number = int(input('Choose a number for your friend to guess: '))
    else:
        game(number)
def game(number):
    print("I am thinking of a 3-digit number. Try to guess what it is.\n")
    print(" Here are some clues:\n")
    print("When I say :         That means:\n")
    print("Cold                 No digit is correct.\n")
    print("Warm                 One digit is correct, but in the wrong position.\n")
    print("Hot                  One digit is correct and in the correct position.\n")
    print("I have thought up a number. You have 10 guesses to get it.\n")

    guesses = 0
    guess = 0
    while guesses < 10 and number != guess:
        print("Guess ", guesses + 1, ": ")
        guess = int(input())
        if str(guess)[0] or str(guess)[1] or str(guess)[2] not in str(number):
            print("Cold")
        elif str(guess)[0] or str(guess)[1] or str(guess)[2] in str(number):
            print("warm")
        elif str(number)[0] == str(guess)[0] or \
        str(number)[1] == str(guess)[1] or \
        str(number)[2] == str(guess)[2]:
            print("Hot")
        elif guess == number:
            print("YOU WIN! CONGRATULATIONS!!!")
            break



start()
