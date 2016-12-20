#This program is a simple game in which player should guess a randomly choosen number beetwen 1 and 20.
import random#From python library it imports module with functions which can choose random elements

guessesTaken = 0 #it means that 0 has been assign to variable guessesTaken

print('Hello! What is your name?')#it will write message from parenthesis when program will be run
myName = input()#it assigning (as a string) what player will write in command line to variable myName

number = random.randint(1, 20)#it asssigning random int (above zero, full number) to variable number
print('Well, ' + myName + ', I am thinking of a number between 1 and 20.')#it will write what's written in paranthesis, as a myName it will be placed what player wrote in command line when program was assigning this to value of variable myName
#program will write what's written in a paranthesis, but in place of myName it will placed what player wrote when program asked about players name
while guessesTaken < 6:#it starting a while loop ralated to variable guessesTaken. every command in while (under while by tab separation) will be done until variable guessesTaken reach 6.
    print('Take a guess.')#program write's what's written in paranthesis into command line
    guess = input()#it assigning what player wrote in command line as a string to variable guess
    guess = int(guess)#variable guess changing type for int. It can show Valueerror if variable guess was written as a letters

    guessesTaken += 1#Variable value will be growing by 1 every time when commands in while loop will be done. So every command in while loop will be done 6 times.

    if guess < number:#every time when while is run checks if statement in which variable guess(int) is lower than variable number(int between 1 and 20). program checks if condition is true it will do what's saparated by tab under this if statement
        print('Your guess is too low.')#if condition from if statement is true program will write what's written in a paranthesis

    if guess > number:#every time when while is run Checks if if statement is true or false. If statement is True it will do what's written under this statement
        print('Your guess is too high.')#if condition from if statement is true program will write what's written in a paranthesis

    if guess == number:# every time when while is run Checks if if statement is true or false. If statement is True it will do what's written under this statement. In this case only one if can be run, because if statements are excluding
        break#it stopping the loop. program is doing out of loop no mather if condition from while loop would stop the loop when variable guessesTaken reached 6.

if guess == number:#after quiting the loop it checks true about this statement, if is true it will do what's written below this if statement separeted by tabs. This if will run only if player will win by guessing the number and breaking the loop with third if in while loop
    guessesTaken = str(guessesTaken)#It changing type of variable guessesTaken for a string.(generaly words, letters, could be numbers as well with no maths operations on it. Numbers are threted as a words as well).
    print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')#if condition from if statement is true program will write what's written in a paranthesis in a place of myName it will place what was written by player as a string, and in the place of guessTaken it will write value of guessTaken variable

if guess != number:#after quiting the loop it checks if statement is true - this if will run only if player will use 6 guesses
    number = str(number)#when this if will run it will change type of variable number for a string
    print('Nope. The number I was thinking of was ' + number)#program will write what's written in a paranthesis, but in place of number it will write randomly choosen number which was choosen at the beggining
