cnt = 0
for i in range(100, 10000):
    if i < 1000:
        a = i//100
        b = (i%100)//10
        c = i%10
        if a != b and a != c and b != c :
            cnt += 1
    else: 
        a = i//1000
        b = (i%1000)//100
        c = (i%100)//10
        d = i%10
        if a != b and a != c and a != d and  b != c and b != d and c != d:
            cnt += 1
print(cnt)        