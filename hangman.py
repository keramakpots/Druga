import random
import sys
import time
def main():
    name = input("Welcome in Hangman game. Whats your name?:")
    capitals = ("AMSTERDAM", "ANDORRA", "AMNKARA", "ATHENS", "BAKU", "BELFAST",
                "BELGRADE", "BERLIN", "BERN", "BRATISLAVA","BRUSSELS",
                "BUCHAREST", "BUDAPEST", "COPENHAGEN", "DUBLIN","HELSINKI",
                "KIEV", "LISBON", "LJUBLJANA", "LONDON", "LUXEMBOURG", "MADRID",
                "MINSK", "MONACO", "MOSCOW", "NICOSIA","OSLO", "PARIS",
                "PODGORICA","PRAGUE", "PRISTINA", "REYKJAVIK", "RIGA", "ROME",
                 "SARAJEVO","SKOPJE", "SOFIA", "STOCKHOLM",
                "TALLINN", "TBILISI", "TIRANA", "VATICAN",
                "VIENNA", "VILNIUS","WARSAW", "ZAGREB")
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
    option(guess, name, lifes, start_time,city, info, lette_wrong)
def option(guess, name, lifes, start_time,city, info, lette_wrong):
    for lette in info:
        print(lette," ",end="")
    if info == city:
        print("Congratulation",name,". You've guessed the capital in", round((time.time() - start_time)), "seconds.")
        over = input("Do you want to play again (yes for start over/no for exit) ")
        while over != 'yes' and over != 'no':
            over = input("Enter expected command(yes or no): ")
        else:
            if over.lower() == 'yes':
                main()
                pass
            elif over.lower() == 'no':
                exit()
                pass
    else:
        print("Wrong letters: ",lette_wrong)
    print(lifes)
    choice = input("Do you want to guess a letter or whole word?:Enter letter or word: ")
    if choice == 'letter':
        letter(guess, name, lifes, start_time,city, info, lette_wrong)
    elif choice == 'word':
        word(guess, name, lifes, start_time,city, info, lette_wrong)
    else:
        print("Wrong option")
        option(guess, name, lifes, start_time,city, info, lette_wrong)
def letter(guess, name, lifes, start_time,city, info, lette_wrong):

    answer = input("Please choose a letter: ")

    if answer.upper() in city:
        for ind in range(len(city)):
            if city[ind] == answer.upper():
                info[ind] = answer.upper()

        option(guess, name, lifes, start_time,city, info, lette_wrong)

    else:
        lifes = lifes - 1
        lette_wrong.append(answer.upper())
        option(guess, name, lifes, start_time,city, info, lette_wrong)


def word(guess, name, lifes, start_time,city, info, lette_wrong):
    print(lifes)
    trying = input("What's the capital?")
    if trying.upper() == guess:
        print("Congratulation",name,". You've guessed the capital. You did it in ", round((time.time() - start_time)), "seconds.")
        over = input("Do you want to play again(yes for start over/no for exit) ")
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
        lifes = lifes - 2
        if lifes > 0:
            print("Unfortunately", trying, "is not my secret capital")
            option(guess, name, lifes, start_time,city, info, lette_wrong)
        else:
            print("You loose.")
            sys.exit()






main()
