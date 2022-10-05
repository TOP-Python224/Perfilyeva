''' Программа выводит введенное число прописью на английском языке. 
   Для выхода - пустой ввод'''
d_1 = { 0:'', 1:' one ', 2:' two ', 3:' three ', 4:' four ', 5:' five ', 6:' six', 7:' seven', 8:' eight ', 9:' nine'}
iskl= {0:'', 10:' teen', 11:' eleven ', 12:' twelve ', 13:' thirteen ', 14:' fourteen ', 15:' fifteen ', 16:' sixteen ', 17:' seventeen ', 18:' eighteen ', 19:' nineteen ',
    10:' ten ', 20:' twenty ', 30:' thirty ', 40:' forty ', 50:' fifty ', 80:' eighty ', 60:' sixty ', 70:' seventy ', 90:' ninety '}
while val:=input('Введите число > ') :
        res = ''
        val = int(val)
        if val//100>0:
            res = d_1[val//100] + ' hundred '
        if val%100 in iskl.keys():
            res += iskl[val%100] 
        else:
            res += iskl[val%100-val%10] + d_1[val%10]          
        print(res)            
        
