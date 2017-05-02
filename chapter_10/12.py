# Two words are a "reverse pair" if each is the reverse of the other.
# Write a program that finds all the reverse pairs in the word list.


def reverse_pair(filename):
    check_list = []
    f = open(filename)
    for word in f:
        s = word.strip()
        t = s[::-1]
        if s not in check_list:
            check_list.append(s)
        if t in check_list:
            print (t, s)

reverse_pair('12_reverse.txt')
