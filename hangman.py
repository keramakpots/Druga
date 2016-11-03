import random
import sys
def main():
    name = input("Welcome in Hangman game. Whats your name?:")
    capitals = ("AMSTERDAM", "ANDORRA", "AMNKARA", "ATHENS", "BAKU", "BELFAST",
                "BELGRADE", "BERLIN", "BERN", "BRATISLAVA","BRUSSELS",
                "BUCHAREST", "BUDAPEST", "COPENHAGEN", "DUBLIN","HELSINKI",
                "KIEV", "LISBON", "LJUBLJANA", "LONDON", "LUXEMBOURG", "MADRID",
                "MINSK", "MONACO", "MOSCOW", "NICOSIA","OSLO", "PARIS",
                "PODGORICA","PRAGUE", "PRISTINA", "REYKJAVIK", "RIGA", "ROME",
                "SAN MARINO", "SARAJEVO","SKOPJE", "SOFIA", "STOCKHOLM",
                "TALLINN", "TBILISI", "TIRANA", "VIENNA", "VILNIUS","WARSAW",
                "ZAGREB")
    guess = random.choice(capitals)
    print(guess)
    print("Try to guess a european capital")
    option(guess)
    lifes = 5
def option(guess):
    choice = input("Do you want to guess a letter or whole word?:Enter letter or word: ")
    if choice == 'letter':
        letter(guess)
    else:
        word(guess)
def word(guess):
    trying = input("What's the capital?")
    if trying == guess:
        print("Congratulation! You've guessed the capital.")
        Over = input("Do you want to play again(yes for start over/no for exit)")
        if over == 'yes' or over == 'Yes' or over == 'YES':
            main()
        else
            sys.exit()

    else:
        lifes =-1
        print("Unfortunately", trying, "is not my secret capital")
        option(guess)





main()
