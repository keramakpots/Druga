l = 'a bc'
n = 'bc'

def title_case(title, minor_words=None):
    title = title.split(' ')
    try:
        exceptions = minor_words.split(' ')
    except AttributeError:
        exceptions = ''
    new = []
    for i in title:
        new.append(i.capitalize())
        out = []
        for i in new:
            out.append(i)
            if any(i == s.capitalize() for s in exceptions) and out.index(i) > 0:
                out[out.index(i)] = i.lower()
    out = ' '.join(out)
    return out




print(title_case(l,n))
