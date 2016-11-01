
import sys


def doing():
    question = input("Please specify a command[list/add/mark/archive]:")
    if question == 'list':
        print ("You saved the followings to_do items: ")
        with open('lista.txt', 'r') as infile:
            data = infile.read()
            print(data)
    elif question == 'add':
        print ("Add an item:")
        answer1 = input()
        with open('lista.txt', 'a') as infile:
            infile.write('\n' + answer1)
            print ("You've added", answer1, "to to-do list.")
    elif question == 'mark':
        to_do = open('lista.txt', 'a')
        print (to_do)
        print ("Which item you want to mark as completed?:")
    elif imput() == archive:
        print("else")
    else:
        sys.exit()
doing()
