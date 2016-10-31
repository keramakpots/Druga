doors = [False] * 100
opened=[]

for i in range(0, len(doors)):
    for j in range(i, len(doors), i + 1):
        doors[j] = not doors[j]
#Showing elements with 
for i in range(len(doors)):
    if doors[i] == True:
        opened.append(i+1)
print("Following doors are open:")
print(opened)
