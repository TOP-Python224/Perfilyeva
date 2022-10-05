''' Программа получает на входе строку, содержащую имена файлов, разделенные символом пробела.
 Выводит исправленную строку, не содержащую дубликатов сохранив при этом исходный порядок.'''

str_inp = input('Введите строку > ')
res = str_inp.split(' ')
for name in set(str_inp.split(' ')):
    n = 2
    while str_inp.split(' ').count(name)>1:
        poz = str_inp.index(name, str_inp.index(name)+1)
        str_inp = str_inp[:poz] + str_inp[poz:poz+len(name)].replace('.', '_'+str(n)+'.') + str_inp[poz+len(name):]
        n += 1
print(str_inp)
    
#Введите строку > 1.py 1.py aux.h main.cpp functions.h main.cpp 2.py main.cpp
# 1.py 1_2.py aux.h main.cpp functions.h main_2.cpp 2.py main_3.cpp    

        
  
