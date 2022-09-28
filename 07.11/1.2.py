numb = int(input('Введите возраст: '))
if numb<=13:
    print("Детство")
elif 13<numb<=24:
    print("Молодость")
elif 24<numb<60:
    print("Зрелость")
else: print("Старость")