"""Программа переводит список введенных слов на поросячью латынь, не исключая знаки препинания, и заглавные буквы в начале слова."""

# СДЕЛАТЬ: откорректируйте код здесь, используя мои правки из предыдущей задачи

from string import ascii_letters as asl, punctuation

letter_v = ['a', 'e', 'i', 'o', 'u']
# ИСПРАВИТЬ: здесь уже не список слов, а предложение(-я)
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
    # ИСПРАВИТЬ: а если в предложении есть слово в кавычках или скобках? (см. тест ниже)
    if flag_upper:
        str_inp[i] = str_inp[i].capitalize()
print(' '.join(str_inp))


# Введите список слов для перевода > Computer, think! Algorithm, office.
# Omputercay, inkthay! Algorithmway, officeway.

# СДЕЛАТЬ: тестируйте на большем количестве данных — как, например, быть с самостоятельными знаками препинания, как тире, длинное тире (отсутствуют в punctuation), амперсанд и прочие?
# Введите список слов для перевода > What did he say?! "Be gone", — that's the quote.
# Atwhay idday ehay aysay?! "beay onegay", —ay at'sthay ethay uoteqay.

# Введите список слов для перевода > "Fritz & Thompson" was written on the bronze label near the door.
# ... IndexError: string index out of range


# ИТОГ: частично работает, но нет больше тех изящности и универсальности, которые были в предыдущей задаче, и мало тестов — 3/6
