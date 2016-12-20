
sentence =  [ 'NORTH', 'SOUTH', 'WEST', 'EAST', 'SOUTH', 'WEST', 'NORTH', 'NORTH', 'SOUTH', 'WEST' ]

def dirReduc(arr):
    z = len(arr)
    while z >= 0:
        i = 1
        while i < len(arr):
            print(arr)
            if arr[i] == "WEST" and arr[i-1] == "EAST" or arr[i] == "EAST" and arr[i-1] == "WEST":
                del arr[i-1:i+1]
            elif arr[i] == "NORTH" and arr[i-1] == "SOUTH" or  arr[i] == "SOUTH" and arr[i-1] == "NORTH":
                del arr[i-1:i+1]
            i+=1
        z-=1
    print(arr)
    return arr






dirReduc(sentence)