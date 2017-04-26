# Encapsulate this code in a function named count, and generalize it so
# that it accepts the string and the letter as arguments.


def my_count(word, letter):
    count = 0
    for i in word[:]:
        if i == letter:
            count += 1;
    return count


print my_count('freedom', 'e')
print my_count('struggle', 'q')
print my_count('titfortat', 't')
