numb = int(input('Введите число '))
sum = 0
for i in range(1, numb+1):
    if numb%i == 0 : 
        sum += i
print('Сумма всех делителей = ', sum)
        