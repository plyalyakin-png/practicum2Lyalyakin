import math
N = int(input())
C = int(input())
num = int(input())
page = math.ceil((num / (N * C)))
string_1 = ((num - (page-1)*C*N) % N)
if string_1 == 0:
    string_1 = N
column = math.ceil((num - (page-1)*C*N) / N)
print('страница',page,'столбец', column,'строка', string_1)