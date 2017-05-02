# Write a function that reads the file words.txt and builds a list with
# one element per word. Write two versions of this function, one using
# the append method and the other using the idiom t = t + [x]. Which
# one takes longer to run? Why?


import time
# import dis

def wordlist1(f):
    t = []
    filename = open(f)
    for line in filename:
        s = line.strip()
        t.append(s)
    return t


def wordlist2(f):
    t = []
    filename = open(f)
    for line in filename:
        s = line.strip()
        t = t + [s]
    return t

t1 = time.time()
wordlist1('wordslist.txt')
remain_t1 = time.time() - t1
print t1, remain_t1

t2 = time.time()
wordlist2('wordslist.txt')
remain_t2 = time.time() - t2
print t2, remain_t2

if remain_t1 > remain_t2:
    print 'append takes longer'
elif remain_t1 < remain_t2:
    print 'append is faster'
else:
    print 'both equal'

# print dis.dis(wordlist1)
# print dis.dis(wordlist2)
