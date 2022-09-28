
for i in ('КУЗЬМА'):
    if i == 'К':
        s = 6
        k = 2
    elif  i == 'У':
        s = 1
        k = 5
    elif  i == 'З':
        s = 3
        k = 3
    elif  i == 'Ь':
        s = 1
        k = 1
    elif  i == 'М':
        s = 7
        k = 4
    elif  i == 'А':
        s = 1
        k = 7
    for j in range(0, s):
        for m in range(0, k):
            print(i, end = '')       
        print()
