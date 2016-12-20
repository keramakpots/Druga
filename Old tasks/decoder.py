import string

alpha = string.ascii_letters
text = open('riddle.txt', 'r')
code = text.read()
def decoder(alpha, code):
    for i in range(len(code)-1):
        if code[i] == ' ':
            print(' ', end='')
        elif code[i] == '\n':
            print('\n', end='')
        else:
            asc = ord(code[i])
            if  96<asc<123:
                print(chr(122 - (asc - 97)), end='')
            elif 66<asc<91:
                print(chr(90 - (asc - 65)), end='')
    #if 'exclamation mark' in code:
        #code.replace('exclamation mark', '!')
    #elif 'apostrophe' in code:
        #code.replace('apostrophe', "'")
    #elif 'question mark' in code:
        #code.replace('question mark', '?')
    print('\n')
    return code
decoder(alpha, code)
