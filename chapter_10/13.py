# Two words "interlock" if taking alternating letters from each forms
# a new word. For example, "shoe" and "cold" interlock to form
# "schooled". Write a program that finds all pairs of words that
# interlock.


def interlock(w1, w2):
    inter = []
    if len(w1) == len(w2):
        list1 = list(w1)
        list2 = list(w2)
        for i in range(len(w1)):
            inter.append(list1[i])
            inter.append(list2[i])
        return ''.join(inter)
    else:
        return None

print interlock('abc', 'def')
