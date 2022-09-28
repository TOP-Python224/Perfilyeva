count = 0
for i in range(1000, 1000000):
    numb_str = str(i)
    if len(numb_str)<6:
        numb_str = (6-len(numb_str))*'0' + numb_str
    if int(numb_str[0]) + int(numb_str[1]) + int(numb_str[2]) == int(numb_str[3]) + int(numb_str[4]) + int(numb_str[5]):
        count +=1       
print(count)
