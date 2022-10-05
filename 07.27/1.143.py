''' Программа проверяет являются ли 2 введенных слова аннограммой'''
word_1 = input('Введите первое слово > ')
word_2 = input('Введите первое слово > ')
if len(word_1) == len(word_2):
    d = dict(zip(word_1, word_2[::-1]))
    if list(d.keys()) == list(d.values()):
        print('являются ')
else:
    print('Не являются ')
        
  
