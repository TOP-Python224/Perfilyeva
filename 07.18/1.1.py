mail = input('Введите адрес эл почты: ')
for i in range(len(mail)):
    if mail[i] =='@' and '.' in mail[i+1:]:
        print('Верно')
        break
else:
    print('Неверно')
