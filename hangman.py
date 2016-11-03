import random
def main():
    name = input("Welcome in Hangman game. Whats your name?:")
    capitals = ("Amsterdam", "Andorra", "Amnkara", "Athens", "Baku", "Belfast", "Belgrade", "Berlin", "Bern", "Bratislava",
    "Brussels","Bucharest", "Budapest", "Copenhagen", "Dublin","Helsinki", "Kiev", "Lisbon",
    "Ljubljana", "London", "Luxembourg", "Madrid", "Minsk", "Monaco", "Moscow", "Nicosia","Oslo",
    "Paris", "Podgorica","Prague", "Pristina", "Reykjavik", "Riga", "Rome", "San Marino", "Sarajevo",
    "Skopje", "Sofia", "Stockholm", "Tallinn", "Tbilisi", "Tirana", "Vienna", "Vilnius",
    "Warsaw", "Zagreb")
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
    else:
        lifes =-1
        print("Unfortunately", trying, "is not my secret capital")
        option(guess)





main()
