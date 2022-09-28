numb = int(input('Введите число '))
sum = 0
for _ in range(numb):
    numb1 = int(input('Введите число '))
    if numb1 > 0 : 
        sum += numb1
print('Сумма положительных чисел = ', sum)
        