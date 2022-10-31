# ИСПРАВИТЬ: что-то не сходится...
"""Программа запрашивает строку и расставляет в ней заглавные буквы"""

from functools import reduce
from random import uniform


def average(data: str | list | tuple) -> dict | None:
    res = dict()
    try:
        if type(data) == str: 
            data = data.split(' ')
        data_res = list(map(float, data))
        # КОММЕНТАРИЙ: любителям каждое шевеление в коде заключать в скобки я советую идти изучать LISP — в Python мы совсем не приветствуем лишние скобки, которые уменьшают скорость чтения и восприятия кода
        # СДЕЛАТЬ: а для того, чтобы не возникало непонимания, изучите таблицу приоритетов операторов https://docs.python.org/3/reference/expressions.html#operator-precedence
        res['arifm'] = reduce(lambda a, b: a + b, data_res) / len(data_res)
        res['geometr'] = reduce(lambda a, b: a * b, data_res)**(1/len(data_res))
        res['qwadr'] = (reduce(lambda a, b: a**2 + b**2, data_res) / len(data_res))**(1/2)
        res['garmon'] = len(data_res) / reduce(lambda a, b: 1/a + 1/b, data_res)
        # res = sorted(res[1])
        res = dict(sorted(res.items(), key=lambda item: item[1]))
    except:
        res = None
    return res


if __name__ == "__main__":
    print(average([uniform(1, 10.5) for i in range(0, 5)]))
    print(average((uniform(1, 10.5) for i in range(0, 5))))


# {'garmon': 2.0554629117165044, 'geometr': 5.183123474301442, 'arifm': 6.017481229789175, 'qwadr': 85130877.81551962}
# {'geometr': 4.034991223140904, 'arifm': 5.286275467899324, 'garmon': 5.424434441461225, 'qwadr': 4090049.6023822855}
