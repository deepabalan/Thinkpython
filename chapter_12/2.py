# Program that sorts words with similar length words appear in random
# order.

import random


def random_sort(words):
    t = []
    for word in words:
        t.append((len(word), random.random(), word))
    t.sort()
    print t
    res = []
    for length, _, word in t:
        res.append(word)
    return res

print random_sort(['abc', 'ab', 'bc', 'abcdef', 'def'])
