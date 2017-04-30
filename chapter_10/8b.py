# If there are 23 students in your class , what are the chances that
# two of you have the same birthday? You can estimate this probability
# by generating random samples of 23 birthdays and checking for matches.
# Hint: you can generate random birthdays with the randint function in
# the random module.


import random


def birthday_list():
    new_list = []
    i = 0
    j = range(23)
    for i in j:
        stud = random.randint(1, 31)
        new_list.append(stud)
    print new_list

    for day in new_list:
        if new_list.count(day) > 1:
            return True, day
    return False

print birthday_list()
