
import sys


def doing():
    question = input("Please specify a command[list/add/mark/archive] or press x for exit:")
    if question == 'list':
        print ("You saved the followings to_do items: ")
        with open('lista.txt', 'r') as infile:
            data = infile.readlines()
            for i, item in enumerate(data):
                print(i+1, item)
    elif question == 'add':
        print ("Add an item:")
        answer1 = input()
        with open('lista.txt', 'a') as infile:
            infile.write('[ ]'+ answer1 + '\n')
            print ("You've added", answer1, "to to-do list.")
    elif question == 'mark':
        with open('lista.txt', 'r') as infile:
            data = infile.readlines()
            for i, item in enumerate(data):
                print(i+1, item)
            numer = input("Which item you want to mark as completed:")
            try:
                numer = int(numer)
            except ValueError:
                print("Choose position from a list")
                doing()
            for index, value in enumerate(data):
                if numer == index + 1:
                    x = data[index].replace(" ", "X", 1)
                    data[index] = x
                    print(data[index][3:], "is completed.")
                    pass

    elif question == 'archive':
        with open('lista.txt', 'w+') as infile:
            data = infile.readlines()
            if data[i] == '[x]':
                del data[i]
        print("All completed task has been delated")
    elif question == "x":
        sys.exit()


doing()
