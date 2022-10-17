'''Программа запрашивает строку и расставляет в ней заглавные буквы'''

from functools import reduce
import random

def average(data: str|list|tuple) -> dict|None:    
    res = dict()
    try:
        if type(data) == str: 
            data = data.split(' ')
        data_res = list(map(float, data))
        res['arifm'] = (reduce(lambda a, b: a+b, data_res))/len(data_res)
        res['geometr'] = (reduce(lambda a, b: a*b, data_res))**(1/len(data_res))
        res['qwadr'] = (reduce(lambda a, b: a**2 +b**2, data_res)/len(data_res))**(1/2)
        res['garmon'] = len(data_res)/ (reduce(lambda a, b: 1/a +1/b, data_res))
#        res = sorted(res[1])
        res = dict(sorted(res.items(), key=lambda item: item[1]))
    except:
        res = None
    return res
    
if __name__ == "__main__":

    print(average([random.uniform(1, 10.5)  for i in range(0, 5)]))
    print(average((random.uniform(1, 10.5)  for i in range(0, 5))))



#{'garmon': 2.0554629117165044, 'geometr': 5.183123474301442, 'arifm': 6.017481229789175, 'qwadr': 85130877.81551962}
#{'geometr': 4.034991223140904, 'arifm': 5.286275467899324, 'garmon': 5.424434441461225, 'qwadr': 4090049.6023822855}
  