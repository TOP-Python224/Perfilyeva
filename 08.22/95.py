"""Программа запрашивает строку и расставляет в ней заглавные буквы."""


def convertStr(string: str) -> str:
    str_res = string.capitalize()   
    for j in '.!?':
        pos = 0
        if str_res.count(j) > 0:
            # КОММЕНТАРИЙ: двойные, тройные и более равенства и неравенства никто не отменял
            while 0 < str_res.find(j, pos) < len(str_res) - 1:
                for i in range(str_res.find(j, pos), len(str_res)-1):
                    if str_res[i+1] not in (' ', ''):
                        str_res = str_res[:i+1] + str_res[i+1].upper() + str_res[i+2:]
                        pos += i+2
                        break
        str_res = (str_res
                   .replace(' i', ' I')
                   .replace('i ', 'I ')
                   .replace('i.', 'I.')
                   .replace('i!', 'I!')
                   .replace('i?', 'I?'))
    print(str_res)
    return str_res


if __name__ == "__main__":
    str_inp = input('Введите строку для преобразования > ')
    convertStr(str_inp)


# Введите строку для преобразования > what time do i have to be there? what`s the address? this time i`ll try to be on time!
# What time do I have to be there? What`s the address? This time I`ll try to be on time!
    