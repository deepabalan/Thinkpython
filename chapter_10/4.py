# Write a function called middle that takes a list and returns a new
# list that contains all but the first and last elements. So
# middle([1, 2, 3, 4]) should return [2, 3].


def middle(t):
#    t.pop(0)
#    t.pop(-1)
    return t[1:len(t)-1]


new_list = ['c', 'python', 'java', 'julia', 'algol']

print middle(new_list)

print new_list
