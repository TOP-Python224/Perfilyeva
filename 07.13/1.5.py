string = ''
while True:
    numb = input('Введите число: ')
    string += str(numb) + ' '
    if int(numb)%7 != 0: break
print(string)  
      