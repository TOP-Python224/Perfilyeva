"""Программа принимает на вход список из строк и возвращает собранную строку из его элементов в описанной выше манере."""

print('Введите список слов по одному слову, через Enter, завершение ввода - пустой ввод ')
# ИСПОЛЬЗОВАТЬ: 1) транслитерация — неудачный способ задания имени; 2) используйте имена, отражающие ожидаемое содержимое переменной: например, здесь вы ожидаете получить список слов — используйте имя words
words = list()
while str_inp := input('>>> '):
    words.append(str_inp)

for i in range(len(words)):
    for j in range(i+1):
        # ИСПОЛЬЗОВАТЬ: скобки вокруг условных выражений нужны только для переопределения приоритетов операций — здесь приоритет не был изменён скобками
        if j == 0 and i == 0 or j == i:
           end = ''
        elif j == i - 1:
            end = ' и '
        else:
            end = ', '
        print(words[j], end=end)
    print()


# Введите список слов по одному слову, через Enter, завершение ввода - пустой ввод
# >>> яблоко
# >>> персик
# >>> арбуз
# >>> вишня
# >>>
# КОММЕНТАРИЙ: в условии задачи таким образом перечислялись варианты вывода для различного количества слов в исходном списке — не нужно было выводить все, а нужно было сформировать один, в зависимости от количества слов в исходном списке
# яблоко
# яблоко и персик
# яблоко, персик и арбуз
# яблоко, персик, арбуз и вишня


# ИТОГ: хорошо — 3/4
