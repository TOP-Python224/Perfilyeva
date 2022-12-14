# ИСПОЛЬЗОВАТЬ: комментарии и строки документации пишутся с переносами строк по абзацам, для удобного отображения используется "мягкий" перенос слов soft wrap
"""Программа должна возвращать список слов из строки с удаленными знаками препинания, в число которых должны входить точки, запятые, восклицательный и вопросительный знаки, дефисы, апострофы, двоеточия и точки с запятыми. При этом не нужно избавляться от знаков препинания, стоящих внутри слова, таких как апостроф."""

from string import punctuation

if __name__ == '__main__':
    str_inp = input('Введите строку > ')
    # УДАЛИТЬ: метод strip() работает именно по краям целевой строки — как только метод встретит символ, не входящий в переданную методу строку, то он остановит свою работу с соответствующего края — таким образом, знаки препинания внутри целевой строки вне опасности, а замена в punctuation не нужна
    punctuation = punctuation.replace('`', '')
    res = list(map(lambda x: x.strip(punctuation), str_inp.split()))
    print(res)


# Введите строку > Contractions include: don`t, isn`t, and wouldn`t.
# ['Contractions', 'include', 'don`t', 'isn`t', 'and', 'wouldn`t']


# ИТОГ: хорошо — 3/4
