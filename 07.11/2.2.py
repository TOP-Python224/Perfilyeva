numb = int(input('Введите год: '))
if (numb%4==0 and numb%100!=0) or numb%400==0: print('ДА')
else: print('НЕТ')
