''' Программа должна возвращать список слов из строки с удаленными 
знаками препинания, в число которых должны входить точки, 
запятые, восклицательный и вопросительный знаки, дефисы, апострофы,
двоеточия и точки с запятыми. При этом не нужно избавляться от знаков
препинания, стоящих внутри слова, таких как апостроф'''

from string import punctuation

if __name__ == '__main__':
    str_inp = input('Введите строку > ')
    punctuation = punctuation.replace('`', '')
    res = list(map(lambda x: x.strip(punctuation), str_inp.split()))
    print(res)
    
#Введите строку > Contractions include: don`t, isn`t, and wouldn`t.
#['Contractions', 'include', 'don`t', 'isn`t', 'and', 'wouldn`t']