# Write a function called rotate_word that takes a string and an
# integer as parameters, and that returns a new string that contains
# the letters from the original string "rotated" by the given amount.


def rotate_word(word, amount = 0):
    for letter in word:
        new_code = ord(letter) + amount
        new_word = chr(new_code)
        print new_word,

rotate_word('cheer', 7)
rotate_word('melon', -10)
