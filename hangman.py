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
    lifes = 5
    option(guess, name, lifes)
def option(guess, name, lifes):
    choice = input("Do you want to guess a letter or whole word?:Enter letter or word: ")
    if choice == 'letter':
        letter(guess, name, lifes)
    else:
        word(guess, name, lifes)
def word(guess, name, lifes):
    trying = input("What's the capital?")
    if trying.upper() == guess:
        print("Congratulation", name,". You've guessed the capital.")
        over = input("Do you want to play again(yes for start over/no for exit)")
        if over == 'yes' or over == 'Yes' or over == 'YES':
            main()
        else:
            sys.exit()

    else:
        lifes =-1
        print("Unfortunately", trying, "is not my secret capital")
        option(guess)





main()
