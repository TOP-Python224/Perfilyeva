d_1 = {1 : 'a', 2 : 'b', 3 : 'c', 4 :'a'}
print(d_1)
while True:
    res = []
    valFind = input('Введите что будем искать > ')
    if valFind:
        for k in d_1.keys():
            if d_1.get(k) == valFind:
                res += [k]
    else: break
    print(res)            
        
