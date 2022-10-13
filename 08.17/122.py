"""Программа переводит список введенных слов на поросячью латынь."""

# ИСПОЛЬЗОВАТЬ: в том же модуле есть строка с латинскими буквами только в нижнем регистре
from string import ascii_lowercase as a_lc

# ИСПОЛЬЗОВАТЬ: vowels — гласные
# ИСПОЛЬЗОВАТЬ: достаточно строки, оператор in прекрасно работает с любыми итерируемыми последовательностями
vowels = 'aeiou'
# ИСПОЛЬЗОВАТЬ: повторяющиеся действия с одними и теми же данными мы точно должны выполнять единожды
# ИСПОЛЬЗОВАТЬ: consonants — согласные
consonants = set(a_lc) - set(vowels)
# ИСПОЛЬЗОВАТЬ: мы можем использовать и пустую строку для конкатенации с помощью join()
consonants = ''.join(consonants)
# 'lnrbzgstdhwqvkmxjcypf'

# ИСПОЛЬЗОВАТЬ: когда переменных становится много, то весьма неудобно становится читать неочевидные имена переменных
words = input('Введите список слов для перевода > ').split()
# str_inp = ['computer', 'think', 'algorithm', 'office']
# ИСПОЛЬЗОВАТЬ: мы можем использовать встроенную функцию enumerate() в ситуации, когда индекс нам нужен в паре мест, а во всех остальных он только затрудняет чтение кода
for i, word in enumerate(words):
    if word[0] in vowels:
        words[i] += 'way'
    else:
        # КОММЕНТАРИЙ: концептуально — изящное решение, мне понравилось; реализацию поправил; надо бы, впрочем, измерить его производительность по сравнению с поиском первой гласной с помощью index()
        first_vowel = -len(word.lstrip(consonants))
        ost = word[0:first_vowel]
        words[i] = word.lstrip(consonants) + ost + 'ay'
print(words)


# Введите список слов для перевода > computer think algorithm office
# ['omputercay', 'inkthay', 'algorithmway', 'officeway']

# СДЕЛАТЬ: больше тестов на разных данных


# ИТОГ: есть немало лишних действий, но в целом код довольно неплох — 4/5
