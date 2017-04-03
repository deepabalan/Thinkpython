# Write a function called do_n that takes a function object and a
# number, n, as arguments, and that calls the given function n times.


def fun():
    print 'Inside fun() ...'


def do_n(f, n):
    if n >= 1:
        fun()
        do_n(f, n-1)
    else:
        return

do_n(fun, 4)
