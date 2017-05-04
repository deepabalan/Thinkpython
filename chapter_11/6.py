# Run memoized version of fibonacci and the original with a range of
# parameters and compare their run times.

import time

# this is the original function for fibonacci


def fibo_original(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        result = fibo_original(n-1) + fibo_original(n-2)
    return result

# this is memoized version of fibonacci

known = {0: 0, 1: 1}


def fibo_memo(n):
    if n in known:
        return known[n]
    res = fibo_memo(n - 1) + fibo_memo(n - 2)
    known[n] = res
    return res


def proceed():
    a = int(raw_input('Enter the value of n: '))
    start1 = time.time()
    fibo_original(a)
    end1 = time.time() - start1
    print start1, 'sec', end1, 'sec'
    print a
    start2 = time.time()
    fibo_memo(a)
    end2 = time.time() - start2
    print start2, 'sec', end2, 'sec'

    if end1 == end2:
        print 'both takes equal time'
    elif end1 > end2:
        print 'memoized fibonacci is faster'
    elif end1 < end2:
        print 'original fibonacci is faster'
    b = int(raw_input('Do you want to continue :(1/0) '))
    if b == 1:
        proceed()
    elif b == 0:
        return


proceed()
