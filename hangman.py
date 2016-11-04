import random
import sys
import time


def main():
    """Main function containing list of cities and main variables."""
    name = input("Welcome in Hangman game. Whats your name?: ")
    capitals = ("AMSTERDAM", "ANDORRA", "ANKARA", "ATHENS", "BAKU", "BELFAST",
                "BELGRADE", "BERLIN", "BERN", "BRATISLAVA","BRUSSELS",
                "BUCHAREST", "BUDAPEST", "COPENHAGEN", "DUBLIN","HELSINKI",
                "KIEV", "LISBON", "LJUBLJANA", "LONDON", "LUXEMBOURG", "MADRID",
                "MINSK", "MONACO", "MOSCOW", "NICOSIA","OSLO", "PARIS",
                "PODGORICA","PRAGUE", "PRISTINA", "REYKJAVIK", "RIGA", "ROME",
                 "SARAJEVO","SKOPJE", "SOFIA", "STOCKHOLM",
                "TALLINN", "TBILISI", "TIRANA", "VATICAN",
                "VIENNA", "VILNIUS","WARSAW", "ZAGREB")
                #"""Without San Marino"""
    guess = random.choice(capitals)
    city = list(guess)
    info = city[:]
    for lette in info:
        b = info.index(lette)
        info[b] = "_"
    print(guess)
    print("Try to guess a european capital")
    start_time = time.time()
    lifes = 5
    lette_wrong = []
    guesses = 0
    option(guess, name, lifes, start_time,city, info, lette_wrong,guesses)


def option(guess, name, lifes, start_time,city, info, lette_wrong, guesses):
    """Function that serves selecting option: guessing whole word or by each
    letter.
    """
    for lette in info:
        print(lette," ",end="")
    if info == city:    #if player guess city by guessing letters
        print("Congratulation",name,"."," You've guessed the capital in",
              round((time.time() - start_time)), "seconds with ",guesses+1,
              " guesses.")
        over = input("\nDo you want to play again (yes for start over/no"
                     " for exit) ")
        while over != 'yes' and over != 'no':   #input control
            over = input("Enter expected command(yes or no): ")
        else:
            if over.lower() == 'yes':
                main()
                pass
            elif over.lower() == 'no':
                sys.exit()
                pass
    else:
        print("Wrong letters: ",lette_wrong)
    print("Lifes: ",lifes)
    choice = input("Do you want to guess a letter or whole word? Enter letter or"
                   " word: ")
    if choice == 'letter':
        letter(guess, name, lifes, start_time,city, info, lette_wrong,guesses)
    elif choice == 'word':
        word(guess, name, lifes, start_time,city, info, lette_wrong, guesses)
    else:
        print("Wrong option")
        option(guess, name, lifes, start_time,city, info, lette_wrong,guesses)


def letter(guess, name, lifes, start_time,city, info, lette_wrong,guesses):
    """Function that check letters given by the player."""
    answer = input("Please choose a letter: ")

    if answer.upper() in city:
        guesses = guesses + 1
        for ind in range(len(city)):
            if city[ind] == answer.upper():
                info[ind] = answer.upper()
        option(guess, name, lifes, start_time,city, info, lette_wrong,guesses)

    else:
        guesses = guesses + 1
        lifes = lifes - 1
        lette_wrong.append(answer.upper())
        option(guess, name, lifes, start_time,city, info, lette_wrong,guesses)


def word(guess, name, lifes, start_time,city, info, lette_wrong,guesses):
    """Function that checks words given by the player."""
    print(lifes)
    trying = input("What's the capital? ")

    if trying.upper() == guess:
        print("Congratulation",name,". You've guessed the capital."
              "You did it in ", round((time.time() - start_time)),
              "seconds with ", guesses + 1," guesses.")
        over = input("Do you want to play again (yes for start over/no"
                     " for exit) ")
        while over != 'yes' and over != 'no':
            over = input("Enter expected command(yes or no): ")
        else:
            if over.lower() == 'yes':
                main()
                pass
            elif over.lower() == 'no':
                sys.exit()
                pass

    elif trying.upper()!= guess:
        guesses = guesses + 1
        lifes = lifes - 2
        if lifes > 0:
            print("Unfortunately", trying, " is not my secret capital.")
            option(guess, name, lifes, start_time,city, info, lette_wrong,guesses)
        else:
            print("You loose.")
            sys.exit()


main()
