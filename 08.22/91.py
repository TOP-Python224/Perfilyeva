"""Программа запрашивает день, месяц и год соответственно и выводит на экран порядковый номер дня в заданном году."""


def ordinalDate(day: int, month: int, year: int) -> int:
    calendar = {1:31, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    # УДАЛИТЬ: лишняя переменная res
    res = day
    # ИСПОЛЬЗОВАТЬ: оформление, аналогичное демонстрируемому в примерах — оно практически полностью соответствует PEP8
    # ИСПОЛЬЗОВАТЬ: год является високосным, если его номер нацело делится на 4, но при этом не делится на 100 или делится на 400 — в противном случае год не является високосным
    if year%4 == 0 and year%100 != 0 or year%400 == 0:
        calendar[2] = 29
    else:
        calendar[2] = 28
    # ИСПРАВИТЬ: более оптимальным является генерация подходящей последовательности чисел, чем выполнение отдельного действия (здесь: сложения) на каждой итерации
    for i in range(month-1):
        res += calendar[i+1]
    return res


if __name__ == "__main__":
    day = int(input('Введите день > '))
    month = int(input('Введите месяц > '))
    year = int(input('Введите год > '))
    itog = ordinalDate(day, month, year)
    print(f'Порядковый день {itog}')


# Введите день > 1
# Введите месяц > 3
# Введите год > 2001
# Порядковый день 60

# Введите день > 1
# Введите месяц > 3
# Введите год > 2000
# Порядковый день 61

# КОММЕНТАРИЙ: Settings -> Keymap -> (в строке поиска:) comment -> Comment with Line Comment — изучить имеющиеся сочетания клавиш, по желанию добавить своё (например Ctrl+Q, как в Notepad++), и далее использовать только выбранное сочетание, перестав вручную неправильно вводить символ #


# ИТОГ: хорошо — 3/4
