"""Программа запрашивает строку у пользователя и оповещать его о том, является ли она словесным палиндромом, игнорируя знаки препинания."""

from string import punctuation

str_inp = input('Введите строку > ').lower()
str_inp = list(map(lambda x: x.strip(punctuation), str_inp.split()))
res = 'Является палиндромом'
# ИСПОЛЬЗОВАТЬ: можно проще — разверните получившийся список слов и сравните с исходным списком:
# str_inp == str_inp[::-1]
for i in range(len(str_inp)//2):
    if str_inp[i] != str_inp[-i-1]:
        res = 'Не является палиндромом'
        break
print(res)


# Введите строку > Is it crazy how saying sentences backwards creates backwards sentences saying how crazy it is?
# Является палиндромом


# ИТОГ: хорошо — 3/3
