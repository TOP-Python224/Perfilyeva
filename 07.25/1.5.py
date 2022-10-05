''' Программа  выводит слово, которое встречается реже всего, без учета регистра. 
Если таких слов несколько, выведит то, которое меньше в лексикографическом порядке.'''
from string import punctuation
str_inp = input('Введите строку > ').lower()
res = dict()
words = str_inp.split()
words = list(map(lambda x: x.strip(punctuation), words))
word = set(words)
for word in words:
    res[word] = words.count(word)    
ress = sorted(res.items(), key = lambda x: (x[1], x[0]))
print(ress[0][0])
    
    

#Введите строку > old OLD, pol, kol, kol plo paj
#paj        
  
