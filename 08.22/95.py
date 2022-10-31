"""Программа запрашивает строку и расставляет в ней заглавные буквы."""


def convertStr(string: str) -> str:
    # ИСПРАВИТЬ: лишняя переменная str_res — поскольку вы нигде далее не используете исходное значение string, то смело переписывайте эту же переменную новым значением
    str_res = string.capitalize()
    # ИСПРАВИТЬ: имена i, j, k традиционно используются только для индексов — не смущайте тех, кто будет читать ваш код
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
        # СДЕЛАТЬ: очень хорошо, с ручным управлением индексами вы справились — а теперь напишите версию попроще, например, с использованием split()

        # ИСПРАВИТЬ: вряд ли есть смысл повторять эти замены на каждой итерации цикла по знакам препинания
        str_res = (str_res
                   # ИСПРАВИТЬ: это озаглавит любое слово, начинающееся на букву i (см. тест ниже)
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

# Введите строку для преобразования > i want icecream!
# I want Icecream!

# ОТВЕТИТЬ: как быть в ситуации, когда слово I окружено знаками препинания?
# Введите строку для преобразования > He said: "i'll be back"
# He said: "i'll be back"


# ИТОГ: в целом должно было быть очень хорошо, но вам действительно нужно больше тестировать свой код — 4/6
