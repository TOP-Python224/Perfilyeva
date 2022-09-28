kl_1_str, kl_1_numb = input('Буква первой клетки '), input('Цифра первой клетки ')
kl_2_str, kl_2_numb = input('Буква второй клетки '), input('Цифра второй клетки ')
if kl_1_str==kl_2_str or int(kl_1_numb)==int(kl_2_numb) or abs(ord(kl_1_str)-ord(kl_2_str))== abs(ord(kl_1_numb)-ord(kl_2_numb)) : print('ДА')
else: print('НЕТ')