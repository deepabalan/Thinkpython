# Write a function that reads the words in words.txt and stores them as
# keys in a dictionary. It doesn't matter what the values are. Then you
# can use the in operator as a fast way to check whether a string is in
# dictionary.


def read_word(filename):
    t = {}
    f = open(filename)
    for word in f:
        s = word.strip()
        t[s] = ' '
    print 'abacus' in t

read_word('wordslist.txt')
