"""Программа запрашивает порядковый день, год и период соответственно и выводит на экран дату конца периода."""


def convertDate(day_por: int, year: int, period: int):
    calendar = {1:31, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    if year%100 == 0 and year%4 == 0 or year%400 == 0:
        calendar[2] = 29
    else:
        calendar[2] = 28
    if day_por + period > 337 + calendar[2]:
        year += 1
        day_por = day_por + period - 337 - calendar[2]
    else:
        day_por += period
    i = 1
    while day_por >= calendar[i]:
        day_por -= calendar[i]
        i += 1
    day = day_por
    month = i
    return day, month, year


if __name__ == "__main__":
    day_por = int(input('Введите порядковый день > '))
    year = int(input('Введите год > '))
    period = int(input('Введите период > '))    
    day_res, month_res, year_res = convertDate(day_por, year, period)
    print(f' Дата конца периода: день {day_res}, месяц {month_res}, год {year_res}')


# Введите порядковый день > 61
# Введите год > 2000
# Введите период > 366
# Дата конца периода: день 1, месяц 3, год 2001
