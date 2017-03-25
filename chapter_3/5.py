# Write a function that draws a grid like the following:

""" + - - - - + - - - - +
    |         |         |
    |         |         |
    |         |         |
    |         |         |
    + - - - - + - - - - +
    |         |         |
    |         |         |
    |         |         |
    |         |         |
    + - - - - + - - - - +
"""


def do_twice(f):
    f()
    f()


def do_four(f):
    do_twice(f)
    do_twice(f)


def print_row():
    print '+ - - - - + - - - - +'


def print_col():
    print '|         |         |'


def print_cols():
    do_four(print_col)


def half_grid():
    print_row()
    print_cols()


def grid():
    do_twice(half_grid)
    print_row()

grid()
