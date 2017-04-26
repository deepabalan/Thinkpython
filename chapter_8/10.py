# Write a one-line version of is_palindrome.


def is_palindrome(word):
    return word[:] == word[::-1]

print is_palindrome('malayalam')
print is_palindrome('string')
