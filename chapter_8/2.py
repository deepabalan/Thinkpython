# program to print Jack, Kack, Lack, Mack, Nack, Ouack, Pack, and Quack.


prefix = 'JKLMNOPQ'
suffix_1 = 'ack'
suffix_2 = 'uack'

for letter in prefix:
    if letter == 'O' or letter == 'Q':
        print letter + suffix_2
    else:
        print letter + suffix_1
