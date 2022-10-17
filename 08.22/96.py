'''Программа запрашивает строку и расставляет в ней заглавные буквы'''

def isInteger(string: str) -> str:
    str_res = ''
    flag = True
    for i in string:
        if i != ' ':
            str_res += i
    if str_res[0] not in ('+-0123456789'):
        flag = False
    else:        
        for i in str_res[1:]:
            if i not in ('0123456789'):
                flag = False
                break
    return flag
    
if __name__ == "__main__":
    str_inp = input('Введите строку > ')
#    str_inp = 'what time do i have to be there? what`s the address? this time i`ll try to be on time!'
    if isInteger(str_inp):
        print('Введенную строку можно считать целым числом')
    else:
        print('Введенную строку нельзя считать целым числом')



#Введите строку >   -98568
#Введенную строку можно считать целым числом

#Введите строку >   -в458
#Введенную строку нельзя считать целым числом
    