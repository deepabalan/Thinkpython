# Rewrite this function so that instead of traversing the string, it
# uses the three parameter version of find from the previous section.


def my_count(word, letter, index = 0):
    count = 0
    while index < len(word):
        if word[index] == letter:
            count += 1
        index += 1
    return count

print my_count('deepa', 'e')
print my_count('malayalam', 'a')
