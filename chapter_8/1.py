# Write a function that takes a string as an argument and displays the
# letters backward, one per line.


def backward(s):
    index = len(s)
    while index > 0:
        letter = s[index-1]
        print letter
        index = index -1

backward('pomegranate')
