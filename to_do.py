#By Marek Stopka
import sys
# I know, just i function, but is it necessery to create function
#for every option?
#Of course it wouldby easier to loop...
#choosing starting options
def doing():
    question = input("Please specify a command[list/add/mark/archive] or press x for exit:")
    if question == 'list':
        print ("You saved the followings to_do items: ")
        #reading from a file
        with open('lista.txt', 'r+') as infile:
            data = infile.readlines()
            #this way it read as a lines
            for i, item in enumerate(data):
                print(i+1, item)#making numbers for position in the list
    elif question == 'add':
        #writing in a file
        answer1 = input("Add an item:")
        with open('lista.txt', 'a') as infile:
            infile.writelines('[ ]'+ answer1 + '\n')
            #yeah, i know about the slash, but in other way it was writing
            #end of the line
            print ("You've added", answer1, "to to-do list.")
    elif question == 'mark':
        #marking finished items
        with open('lista.txt', 'r+') as infile:
            data = infile.readlines()
            for i, item in enumerate(data):
                print(i+1, item)
            numer = input("Which item you want to mark as completed: ")
            try:
                numer = int(numer)#to make sure someone is putting number
            except ValueError:
                numer = input("Choose position from a list")
                #I know, just one chance for mistake
            for index, value in enumerate(data):
                if numer == index + 1:
                    x = data[index].replace(" ","X",1)
                    data[index] = x
                    print(data[index][:-1],"is completed.")
        #Saving changes
        with open('lista.txt', 'w') as infile:
            data = infile.writelines(data)
            pass
    elif question == 'archive':
        #biggest problem - it appears it wasn't working in with option of reading a file
        print("All completed task has been delated")
        new_list = []
        data = open("lista.txt", 'r')
        data.read

        for line in data:
            if "[X]" not in line:
                new_list.append(line)
                #I've tried this or very similar version many times
                #in with opening, but I couldn't understand why is not working???
        data.close()
        #Saving
        with open('lista.txt', 'w') as infile:
            data = infile.writelines(new_list)
            pass

    elif question == "x":
        # exit with a letter "x"
        sys.exit()


doing()
