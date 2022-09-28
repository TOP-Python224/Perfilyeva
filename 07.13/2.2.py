cnt = 0
for i in range(100, 1000):
    if i//100 == (i%100)//10 or i//100 == i%10 or (i%100)//10==i%10:
        cnt +=1
print(cnt)        