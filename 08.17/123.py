"""Программа переводит список введенных слов на поросячью латынь, не исключая знаки препинания, и заглавные буквы в начале слова."""

from string import ascii_letters as asl, punctuation

letter_v = ['a', 'e', 'i', 'o', 'u']
str_inp = input('Введите список слов для перевода > ').split()
# str_inp = ['computer', 'think', 'algorithm', 'office']
for i in range(len(str_inp)):
    flag_upper = False
    ost_p = ''
    if str_inp[i].istitle():
        flag_upper = True
    if str_inp[i].rstrip(punctuation) != str_inp[i]:
        ost_p = str_inp[i][len(str_inp[i].rstrip(punctuation)):]
    str_inp[i] = str_inp[i].lower().rstrip(punctuation)
    if str_inp[i][0] in letter_v:
        str_inp[i] += 'way' + ost_p
    else:
        j = -len(str_inp[i].lstrip(','.join(set(asl.lower()) - set(letter_v))))
        ost_l = str_inp[i][0:j]
        str_inp[i] = str_inp[i].lstrip(','.join(set(asl.lower()) - set(letter_v))) + ost_l + 'ay' + ost_p
    if flag_upper:
        str_inp[i] = str_inp[i].capitalize()
print(' '.join(str_inp))


# Введите список слов для перевода > Computer, think! Algorithm, office.
# Omputercay, inkthay! Algorithmway, officeway.
