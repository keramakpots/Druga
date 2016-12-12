import random
def main():
    l = []
    x = 0
    while len(l) < 3:
        x = random.randint(0,9)
        if x not in l:
            l.append(x)
        else:
            pass
    print(type(l))
    print(l)
    start(l)
    return l

def start(l):
    print("Hello in Hot/Cold game!")
    print("i'm thinking of a 3-digit number")
    print("try to guess.")
    print(l)
    while True:
        guess = input(" What's your guess: ")
        try:
            i = 0
            while i <= 2:
                if guess[i] == l[i]:
                    print("hot")
                    i += 1
                    pass
                elif guess[i] in l:
                    print('warm')
                    i += 1
                    pass
                else:
                    print('cold')
                    i += 1
                    pass
        except guess == l:
            pass
    print("You win")













main()
