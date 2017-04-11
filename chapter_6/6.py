# Write a function called is_palindrome that takes a string argument
# and returns True if it is a palindrome and False otherwise.


def first(word):
    return word[0]


def last(word):
    return word[-1]


def middle(word):
    return word[1:-1]

print middle('as')
print middle('a')
print middle('')

def is_palindrome(word):
    return word[:] == word[::-1]


print is_palindrome('noon')
print is_palindrome('redivider')
print is_palindrome('palindrome')
