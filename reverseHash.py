LETTERS = "acdegilmnoprstuw"
def _hash (s):
    h = 7
    for i in range(len(s)):
        h = (h * 37 + LETTERS.index(s[i]))
    return h


def revHash (h):
    the_string = "" 
    while h != 7:
        index = h % 37
        the_string = the_string + LETTERS[int(index)]
        h = h - index
        h = h / 37

    return the_string[::-1]

print(revHash(930846109532517))

