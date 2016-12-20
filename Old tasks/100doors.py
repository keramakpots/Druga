doors = [False] * 5
opened=[]

for i in range(0, len(doors)):
    #changing variables statement by increasing steps
    for j in range(i, len(doors), i + 1):
        doors[j] = not doors[j]
#Showing elements with True statement about opened doors.
for i in range(len(doors)):
    if doors[i] == True:
        opened.append(i+1)
print("Following doors are open:")
print(opened)
