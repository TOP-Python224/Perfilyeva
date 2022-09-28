numb_1, numb_2 = int(input('Введите первое число: ')), int(input('Введите второе число: '))
if numb_1%numb_2==0:
    print(f'''{numb_1} делится на {numb_2} нацело
Частное {numb_1//numb_2}''')
else: print(f'''{numb_1} не делится на {numb_2} нацело
Частное: {numb_1//numb_2}
Остаток:{numb_1%numb_2}''')