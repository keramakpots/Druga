import sys
numb = open(sys.argv[1], 'r')
lines = numb.readlines()
to_sort = []


for i in lines:
    to_sort.append(int(i))

x = 0
while x < len(to_sort):
    for i in range(len(to_sort)-1):
        if to_sort[i] > to_sort[i + 1]:
            to_sort.insert(to_sort.index(i), to_sort[i+1])
    x += 1

print(to_sort)
