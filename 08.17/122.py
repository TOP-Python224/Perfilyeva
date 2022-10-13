"""Программа переводит список введенных слов на поросячью латынь."""

from string import ascii_letters as asl

letter_v = ['a', 'e', 'i', 'o', 'u']
str_inp = input('Введите список слов для перевода > ').split()
# str_inp = ['computer', 'think', 'algorithm', 'office']
for i in range(len(str_inp)):
    if str_inp[i][0] in letter_v:
        str_inp[i] += 'way'
    else:
        j = -len(str_inp[i].lstrip(','.join(set(asl.lower()) - set(letter_v))))
        ost = str_inp[i][0:j]
        str_inp[i] = str_inp[i].lstrip(','.join(set(asl.lower()) - set(letter_v))) + ost + 'ay'
print(str_inp)


# Введите список слов для перевода > computer think algorithm office
# ['omputercay', 'inkthay', 'algorithmway', 'officeway']
