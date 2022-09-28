numb = int(input('Введите число: '))
n, m = 0, 1
for _ in range(numb):
    print(m, end = ' ')
    n, m  = m, m+n
    
      