# Modify find so that it has a third parameter, the index in word where
# it should start looking.


def find(word, letter, index = 0):
    while index < len(word):
        if word[index] == letter:
            return index
        index += 1
    return -1

print find('ubuntu', 'u', 2)

print find('malayalam', 'm', 4)

print find('eye', 'i', 0)
