mixed = 'cedewaraaossoqqyt'
word = 'codewars'
def scramble(s1,s2):
    x = 0
    new = []
    lis = list(s1)
    while x < len(s2):
        if s2[x] not in lis:
            return False
        if s2[x] in lis:
            y = lis.index(s2[x])
            new.append(lis[y])
            del lis[y]
        x +=1
    new = ''.join(new)
    print(new)
    if new == s2:
        return True




scramble(mixed, word)
