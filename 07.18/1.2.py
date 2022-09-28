text = input('Введите текст телеграммы: ')
text_v = ''
for i in text:
    if i != ' ': text_v += i
s = len(text_v)*80
print(f"{s//100} руб. {s%100} коп.")