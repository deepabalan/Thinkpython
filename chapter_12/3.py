# Write a function called most_frequent that takes a string and prints
# the letters in decreasing order of frequency. Find text samples from
# several different languages and see how letter frequency varies
# between languages.


def most_frequent(word):
    d = {}
    for i in word:
        d[i] = d.get(i, 0) + 1
    t = []
    for key, value in d.items():
        t.append((value, key))
    return max(t)

print 'most frequent ', most_frequent('deepa')
