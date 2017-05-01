# Write a function that reads the file words.txt and builds a list with
# one element per word. Write two versions of this function, one using
# the append method and the other using the idiom t = t + [x]. Which
# one takes longer to run? Why?


import time

t1 = time.time()


def wordlist(f):
    t = []
    filename = open(f).readlines()
    for line in filename:
        t.append(line)
    return t
t2 = time.time()
t = t2 - t1
print wordlist('words.txt')
print t


s1 = time.time()


def idiom(f):
    t = []
    filename = open(f).readlines()
    for line in filename:
        t = t + [line]
    return t
s2 = time.time()
s = s2 - s1
print idiom('words.txt')
print s
