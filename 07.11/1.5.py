kl_1_str, kl_1_numb = input('Буква первой клетки '), int(input('Цифра первой клетки '))
kl_2_str, kl_2_numb = input('Буква второй клетки '), int(input('Цифра второй клетки '))
str_1, str_2 = 0, 0
if kl_1_str in ('acdf'): str_1 = 1 
if kl_2_str in ('acdf'): str_2 = 1 
if (str_1+kl_1_numb)%2 == (str_2+kl_2_numb)%2: print('Да')  
else: print('Нет')  
