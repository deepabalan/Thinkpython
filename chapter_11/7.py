# Memoize the Ackermann function and see if memoization makes it
# possible to evaluate the function with bigger arguments.

import time

known = {}


def ack_memo(m, n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ack_memo(m-1, 1)
    elif m > 0 and n > 0:
        res = ack_memo(m-1, ack_memo(m, n-1))
        known[(m, n)] = res
        return res
    elif (m, n) in known:
        return known[(m, n)]


def ack(m, n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ack(m-1, 1)
    elif m > 0 and n > 0:
        return ack(m-1, ack(m, n-1))
    else:
        return

start1 = time.time()
ack_memo(3, 4)
end1 = time.time() - start1

print start1, end1

start2 = time.time()
ack(3, 4)
end2 = time.time() - start2

print start2, end2

if end1 > end2:
    print 'Ackermann memoized takes longer'
else:
    print 'Ackermann memoized takes less time'
